#!/usr/bin/env python3
"""Build only the college static site; never modify the GitHub Pages source."""
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '_vercel_site'
TEXT = {'.html', '.json', '.js', '.css', '.md'}
RUNTIME = {'.html', '.json', '.js', '.css', '.png', '.webp', '.jpg', '.jpeg',
           '.svg', '.gif', '.ico', '.pdf', '.woff', '.woff2', '.ttf', '.md', '.csv', '.txt'}
LEGACY = {'study', 'ncert', 'image', 'files', 'questionbank'}


def references(path):
    text = path.read_text(encoding='utf-8')
    if path.suffix == '.json':
        def strings(value):
            if isinstance(value, str):
                yield value
            elif isinstance(value, dict):
                for item in value.values():
                    yield from strings(item)
            elif isinstance(value, list):
                for item in value:
                    yield from strings(item)
        return list(strings(json.loads(text)))
    return [m.group(2) for m in re.finditer(r'''(["'])(.*?)\1''', text, re.S)] + re.findall(r'url\(([^)]+)\)', text)


def dependencies(path):
    # HTML uses <base href="/">; JSON renderers resolve paths against subject.json
    # or the site base. CSS and module imports resolve relative to their own file.
    bases = [ROOT, path.parent]
    if 'kb' in path.parts:
        bases.append(Path(*path.parts[:path.parts.index('kb')]))
    for value in references(path):
        value = html.unescape(value.strip(' \t\n\"\''))
        if not value or value.startswith(('#', '//')):
            continue
        url = urlsplit(value)
        if url.scheme or url.netloc:
            continue
        for base in bases:
            candidate = (base / unquote(url.path).lstrip('/')).resolve()
            if candidate.suffix.lower() in RUNTIME and len(value) < 500 and candidate.is_relative_to(ROOT) and candidate.is_file():
                yield candidate


def build():
    selected = {ROOT / 'index.html', ROOT / 'navbar_new.html'}
    # Keep every college shell and data contract, including future semesters.
    selected.update(p for p in (ROOT / 'college').rglob('*') if p.suffix in {'.html', '.json'})
    for folder in ('scripts/new', 'styles/new'):
        selected.update(p for p in (ROOT / folder).rglob('*') if p.suffix in {'.js', '.css'})
    pending = list(selected)
    while pending:
        path = pending.pop()
        if path.suffix not in TEXT:
            continue
        for dep in dependencies(path):
            if dep.name == 'index_old.html':
                continue
            if dep.relative_to(ROOT).parts[0] in LEGACY:
                raise RuntimeError(f'College dependency crosses into legacy site: {dep}')
            if dep not in selected:
                selected.add(dep)
                pending.append(dep)
    if OUT.is_symlink():
        raise RuntimeError('Refusing to replace a symlink output directory')
    if OUT.exists():
        shutil.rmtree(OUT)
    for source in sorted(selected):
        target = OUT / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    # The old site is intentionally unavailable only on Vercel. Keep Pages intact.
    home = OUT / 'index.html'
    markup = home.read_text()
    markup, count = re.subn(r'\s*<section class="old-site">.*?</section>', '', markup, flags=re.S)
    if count != 1:
        raise RuntimeError('Expected exactly one legacy homepage section')
    home.write_text(markup)
    files = [p for p in OUT.rglob('*') if p.is_file()]
    size = sum(p.stat().st_size for p in files)
    if size > 350 * 1024 * 1024:
        raise RuntimeError('College output exceeds the 350 MiB deployment budget')
    entries = subprocess.check_output(
        ['git', 'ls-tree', '-r', '-l', '-z', 'HEAD'], cwd=ROOT).decode().split('\0')
    tracked = [(entry.split('\t', 1)[1], int(entry.split('\t', 1)[0].split()[3]))
               for entry in entries if entry and entry.split()[1] == 'blob']
    # Starting configuration: root static output with the five .vercelignore trees.
    previous = [(name, size) for name, size in tracked if name.split('/')[0] not in LEGACY]
    report = {
        'tracked_repository': {'files': len(tracked), 'bytes': sum(size for _, size in tracked)},
        'previous_vercel_static_output': {'files': len(previous), 'bytes': sum(size for _, size in previous)},
        'optimized_output': {'files': len(files), 'bytes': size},
    }
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    build()
