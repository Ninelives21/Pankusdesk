#!/usr/bin/env python3
"""Copy the college browsing dependency closure into Vercel's static output."""
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
ENTRIES = {'index.html', 'navbar_new.html'}
CURRENT_TREES = ('college/', 'scripts/new/', 'styles/new/')


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
    # HTML uses the site base; JSON renderers use the site or subject base.
    # CSS and module imports can resolve relative to their own file.
    bases = [ROOT, path.parent]
    if 'kb' in path.parts:
        bases.append(Path(*path.parts[:path.parts.index('kb')]))
    for value in references(path):
        value = html.unescape(value.strip(' \t\n\"\''))
        if not value or len(value) >= 500 or value.startswith(('#', '//')):
            continue
        try:
            url = urlsplit(value)
        except ValueError:
            continue  # Arbitrary prose/metadata strings are not necessarily URLs.
        if url.scheme or url.netloc:
            continue
        for base in bases:
            candidate = (base / unquote(url.path).lstrip('/')).resolve()
            if (candidate.suffix.lower() in RUNTIME
                    and candidate.is_relative_to(ROOT) and candidate.is_file()):
                yield candidate


def source_files():
    """Inventory this checkout, without accidentally reading a parent Git repo."""
    try:
        repo = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'], cwd=ROOT,
            capture_output=True, text=True, check=True)
        if Path(repo.stdout.strip()).resolve() == ROOT:
            names = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
            return [ROOT / name for name in names if name and (ROOT / name).is_file()]
    except (OSError, subprocess.CalledProcessError):
        pass
    # Source archives used for local verification need no Git installation/metadata.
    excluded = {'.git', '.vercel', '_vercel_site', 'work', 'node_modules'}
    return [p for p in ROOT.rglob('*') if p.is_file()
            and p.relative_to(ROOT).parts[0] not in excluded
            and '__pycache__' not in p.parts and p.name != '.DS_Store']


def inventory(files):
    return {'files': len(files), 'bytes': sum(p.stat().st_size for p in files)}


def build():
    selected = {ROOT / name for name in ENTRIES}
    # Keep every college shell and JSON contract, including future semesters.
    selected.update(p for p in (ROOT / 'college').rglob('*') if p.suffix in {'.html', '.json'})
    for folder in ('scripts/new', 'styles/new'):
        selected.update(p for p in (ROOT / folder).rglob('*') if p.suffix in {'.js', '.css'})
    pending = list(selected)
    while pending:
        path = pending.pop()
        if path.suffix not in TEXT:
            continue
        for dep in dependencies(path):
            relative = dep.relative_to(ROOT).as_posix()
            if relative not in ENTRIES and not relative.startswith(CURRENT_TREES):
                raise RuntimeError(f'College dependency outside current runtime roots: {relative}')
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
    # Preserve every file byte-for-byte, including the external legacy landing link.
    files = [p for p in OUT.rglob('*') if p.is_file()]
    if inventory(files)['bytes'] > 350 * 1024 * 1024:
        raise RuntimeError('College output exceeds the 350 MiB deployment budget')
    sources = source_files()
    eligible = [p for p in sources if p.relative_to(ROOT).parts[0] not in LEGACY]
    report = {
        'source_input': inventory(sources),
        'source_after_existing_vercel_tree_exclusions': inventory(eligible),
        'optimized_output': inventory(files),
    }
    print(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    build()
