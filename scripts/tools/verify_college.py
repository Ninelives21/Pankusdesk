#!/usr/bin/env python3
"""Generic PankusDesk college architecture verifier.

Run from repository root:
    python3 scripts/tools/verify_college.py

Optional subject root(s):
    python3 scripts/tools/verify_college.py college/1-1/basic-electrical-engineering

This verifier intentionally checks cross-subject architectural invariants only.
Subject-specific source counts/anomalies remain the responsibility of each
subject's own kb/tools/verify_kb.py (or equivalent).
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse, parse_qs
import argparse
import json
import re
import sys

REPO = Path(__file__).resolve().parents[2]
ALLOWED_TOPIC_STATUS = {"core", "supporting", "core-gap-filled"}
ALLOWED_PUBLICATION = {"ready", "scaffold"}
META_PATTERNS = [
    r"\bthe class notes?\b",
    r"\bthe \d{1,2} [A-Za-z]+ class\b",
    r"\bthe prescribed textbook\b",
    r"\bthe textbook says\b",
    r"\bthe lecture (?:says|explains|notes?)\b",
    r"\bthe source material\b",
    r"\bthe supplied source\b",
    r"\bat the level needed here\b",
    r"\bR\d+ Unit [IVX0-9]+\b",
    r"\bR\d+ requirement\b",
    r"\bthis course (?:requires|covers|uses)\b",
    r"\bthis page (?:keeps|retains|shows|uses)\b",
    r"\bwe (?:retain|include|use|have kept)\b",
]
META_RE = re.compile("|".join(f"(?:{p})" for p in META_PATTERNS), re.I)

errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON: {rel(path)}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON {rel(path)}: line {exc.lineno}: {exc.msg}")
    return None


def resolve_repo_asset(value: str) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        return None
    parsed = urlparse(value)
    if parsed.scheme or value.startswith("#"):
        return None
    clean = parsed.path.lstrip("/")
    return REPO / clean


def visible_topic_strings(topic: dict):
    for key in ("intro",):
        if isinstance(topic.get(key), str):
            yield f"{key}", topic[key]
    for key in ("learn", "formulas", "method", "cautions"):
        for i, text in enumerate(topic.get(key, []) or []):
            if isinstance(text, str):
                yield f"{key}[{i}]", text
    for si, section in enumerate(topic.get("sections", []) or []):
        if not isinstance(section, dict):
            continue
        if isinstance(section.get("heading"), str):
            yield f"sections[{si}].heading", section["heading"]
        for key in ("paragraphs", "bullets"):
            for i, text in enumerate(section.get(key, []) or []):
                if isinstance(text, str):
                    yield f"sections[{si}].{key}[{i}]", text
    for qi, item in enumerate(topic.get("self_checks", []) or []):
        if isinstance(item, dict):
            for key in ("question", "answer"):
                if isinstance(item.get(key), str):
                    yield f"self_checks[{qi}].{key}", item[key]


def collect_topic_figures(topic: dict):
    for si, section in enumerate(topic.get("sections", []) or []):
        if not isinstance(section, dict):
            continue
        paragraphs = section.get("paragraphs", []) or []
        bullets = section.get("bullets", []) or []
        for fi, fig in enumerate(section.get("figures", []) or []):
            yield si, fi, fig, len(paragraphs), len(bullets)


def load_question_ids(subject_dir: Path, subject: dict) -> tuple[set[str], dict | None]:
    qcfg = (subject.get("practice") or {}).get("unitQuestions") or {}
    data_path = qcfg.get("data")
    if not data_path:
        return set(), None
    data = load_json(subject_dir / data_path)
    if not isinstance(data, dict):
        return set(), data
    ids: set[str] = set()
    for unit in (data.get("units") or {}).values():
        if not isinstance(unit, dict):
            continue
        for group in unit.get("groups", []) or []:
            for q in group.get("questions", []) or []:
                qid = q.get("id") if isinstance(q, dict) else None
                if not qid:
                    errors.append(f"question without id in {rel(subject_dir / data_path)}")
                elif qid in ids:
                    errors.append(f"duplicate question id {qid} in {rel(subject_dir / data_path)}")
                else:
                    ids.add(qid)
                if isinstance(q, dict):
                    ans = q.get("answer") or {}
                    for fig in ans.get("figures", []) if isinstance(ans, dict) else []:
                        check_figure(fig, f"question {qid or '?'}", None, None)
    return ids, data


def check_figure(fig, context: str, paragraph_count: int | None, bullet_count: int | None):
    if not isinstance(fig, dict):
        errors.append(f"{context}: figure is not an object")
        return
    src = fig.get("src")
    alt = fig.get("alt")
    if not isinstance(src, str) or not src.strip():
        errors.append(f"{context}: figure missing src")
    else:
        path = resolve_repo_asset(src)
        if path is not None and not path.exists():
            errors.append(f"{context}: missing figure asset {src}")
    if not isinstance(alt, str) or len(alt.strip()) < 8:
        errors.append(f"{context}: figure needs descriptive alt text")
    after = fig.get("after")
    if after is not None:
        if not isinstance(after, dict) or after.get("type") not in {"paragraph", "bullet", "end"}:
            errors.append(f"{context}: invalid figure insertion anchor")
        else:
            typ = after.get("type")
            idx = after.get("index")
            if typ != "end" and (not isinstance(idx, int) or idx < 0):
                errors.append(f"{context}: invalid figure insertion index")
            if typ == "paragraph" and paragraph_count is not None and isinstance(idx, int) and idx >= paragraph_count:
                errors.append(f"{context}: paragraph anchor index {idx} out of range ({paragraph_count})")
            if typ == "bullet" and bullet_count is not None and isinstance(idx, int) and idx >= bullet_count:
                errors.append(f"{context}: bullet anchor index {idx} out of range ({bullet_count})")


def check_class_logs(subject_dir: Path, subject: dict, topic_ids: set[str]):
    class_root = subject_dir / "kb" / "class-log"
    if class_root.exists():
        for entry_path in sorted(class_root.glob("*/entry.json")):
            entry = load_json(entry_path)
            if not isinstance(entry, dict):
                continue
            date = entry.get("date")
            if date and entry_path.parent.name != date:
                errors.append(f"{rel(entry_path)}: date does not match directory name")
            for mapped in entry.get("mapped_topics", []) or []:
                tid = mapped.get("topic_id") if isinstance(mapped, dict) else None
                if tid not in topic_ids:
                    errors.append(f"{rel(entry_path)}: mapped topic does not exist: {tid}")
            for page in entry.get("pages", []) or []:
                for block in page.get("blocks", []) if isinstance(page, dict) else []:
                    if isinstance(block, dict) and block.get("type") == "figure":
                        check_figure(block, f"{rel(entry_path)} class figure", None, None)

    raw_dirs = list((subject_dir / "assets" / "class").glob("**/raw")) if (subject_dir / "assets" / "class").exists() else []
    for raw_dir in raw_dirs:
        binaries = [p for p in raw_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".heic", ".tif", ".tiff"}]
        if binaries:
            errors.append(f"raw notebook binaries must stay outside website assets: {rel(raw_dir)} ({len(binaries)} file(s))")


def verify_subject(subject_dir: Path):
    subject_path = subject_dir / "subject.json"
    subject = load_json(subject_path)
    if not isinstance(subject, dict):
        return

    label = f"{subject.get('semester','?')} / {subject.get('shortName') or subject.get('name') or subject_dir.name}"
    required = ("code", "name", "shortName", "regulation", "semester", "kb", "syllabus", "units")
    for key in required:
        if key not in subject:
            errors.append(f"{label}: subject.json missing {key}")

    units = subject.get("units") or []
    unit_numbers: set[int] = set()
    ready_units: set[int] = set()
    for u in units:
        if not isinstance(u, dict):
            errors.append(f"{label}: unit metadata is not an object")
            continue
        n = u.get("number")
        if not isinstance(n, int) or n < 1:
            errors.append(f"{label}: invalid unit number {n}")
            continue
        if n in unit_numbers:
            errors.append(f"{label}: duplicate unit number {n}")
        unit_numbers.add(n)
        status = u.get("publicationStatus")
        if status not in ALLOWED_PUBLICATION:
            errors.append(f"{label}: Unit {n} invalid publicationStatus {status!r}")
        if status == "ready":
            ready_units.add(n)

    topics_path = subject_dir / str(subject.get("kb", ""))
    topics = load_json(topics_path)
    if not isinstance(topics, list):
        return

    topic_ids: set[str] = set()
    topics_by_unit: dict[int, int] = {}
    question_ids, _ = load_question_ids(subject_dir, subject)

    for t in topics:
        if not isinstance(t, dict):
            errors.append(f"{label}: topic record is not an object")
            continue
        tid = t.get("id")
        unit = t.get("unit")
        if not isinstance(tid, str) or not tid:
            errors.append(f"{label}: topic without id")
            continue
        if tid in topic_ids:
            errors.append(f"{label}: duplicate topic id {tid}")
        topic_ids.add(tid)
        if not isinstance(unit, int) or unit not in unit_numbers:
            errors.append(f"{label}: {tid} points to undefined Unit {unit}")
        else:
            topics_by_unit[unit] = topics_by_unit.get(unit, 0) + 1
        if t.get("status") not in ALLOWED_TOPIC_STATUS:
            errors.append(f"{label}: {tid} invalid topic status {t.get('status')!r}")
        refs = t.get("source_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{label}: {tid} has no provenance source_refs")

        for si, section in enumerate(t.get("sections", []) or []):
            if not isinstance(section, dict):
                errors.append(f"{label}: {tid} section {si} is not an object")
                continue
            srefs = section.get("source_refs")
            if not isinstance(srefs, list) or not srefs:
                errors.append(f"{label}: {tid} section {si} has no source_refs")

        if unit in ready_units:
            if not (t.get("sections") or []):
                errors.append(f"{label}: ready-unit topic {tid} has no detailed sections")
            for location, text in visible_topic_strings(t):
                if META_RE.search(text):
                    errors.append(f"{label}: student-facing meta commentary in {tid}.{location}: {text[:100]!r}")
            for si, fi, fig, pc, bc in collect_topic_figures(t):
                check_figure(fig, f"{label}: {tid} section {si} figure {fi}", pc, bc)

        for pi, practice in enumerate(t.get("practice", []) or []):
            if not isinstance(practice, dict):
                continue
            anchor = practice.get("anchor")
            if anchor and question_ids and anchor not in question_ids:
                errors.append(f"{label}: {tid} practice[{pi}] anchor {anchor} does not resolve to a textbook question")

    for n in sorted(ready_units):
        if topics_by_unit.get(n, 0) == 0:
            errors.append(f"{label}: Unit {n} is ready but has no topics")
        unit_shell = subject_dir / f"unit-{n}.html"
        if not unit_shell.exists():
            errors.append(f"{label}: ready Unit {n} missing shell {rel(unit_shell)}")

    # Verify configured question availability.
    qcfg = (subject.get("practice") or {}).get("unitQuestions") or {}
    for n in qcfg.get("availableUnits", []) or []:
        shell = subject_dir / str(qcfg.get("hrefPattern", "unit-{unit}-questions.html")).replace("{unit}", str(n))
        if not shell.exists():
            errors.append(f"{label}: Unit {n} marked as having textbook questions but shell is missing: {rel(shell)}")

    check_class_logs(subject_dir, subject, topic_ids)


def verify_calendar_indexes(subject_dirs: list[Path]):
    # Validate only links that are explicitly present; older calendar entries may intentionally have link=null.
    for index_path in sorted(REPO.glob("college/*/data/class-log.json")):
        data = load_json(index_path)
        if not isinstance(data, dict):
            continue
        for date, entries in data.items():
            for entry in entries if isinstance(entries, list) else []:
                if not isinstance(entry, dict) or not entry.get("link"):
                    continue
                link = entry["link"]
                parsed = urlparse(link)
                shell = REPO / parsed.path.lstrip("/")
                if not shell.exists():
                    errors.append(f"{rel(index_path)} {date}: class-log shell missing for link {link}")
                    continue
                qs = parse_qs(parsed.query)
                qdate = (qs.get("date") or [None])[0]
                subject_dir = shell.parent
                if qdate:
                    dated = subject_dir / "kb" / "class-log" / qdate / "entry.json"
                    if not dated.exists():
                        errors.append(f"{rel(index_path)} {date}: dated entry missing for link {link}")


def discover_subjects(args: list[str]) -> list[Path]:
    if args:
        result = []
        for raw in args:
            p = Path(raw)
            if not p.is_absolute():
                p = REPO / p
            if p.is_file() and p.name == "subject.json":
                p = p.parent
            result.append(p.resolve())
        return result
    return sorted(p.parent for p in REPO.glob("college/*/*/subject.json"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify PankusDesk college architecture")
    parser.add_argument("subjects", nargs="*", help="Optional subject directories or subject.json paths")
    ns = parser.parse_args()

    subjects = discover_subjects(ns.subjects)
    if not subjects:
        print("COLLEGE VERIFY: FAIL")
        print(" - no college subject.json files found")
        return 1

    for subject_dir in subjects:
        verify_subject(subject_dir)
    verify_calendar_indexes(subjects)

    if warnings:
        for w in warnings:
            print("WARNING:", w)

    if errors:
        print("COLLEGE VERIFY: FAIL")
        for e in errors:
            print(" -", e)
        return 1

    print("COLLEGE VERIFY: PASS")
    print(f" - {len(subjects)} subject configuration(s) checked")
    print(" - ready units have topic data and shells")
    print(" - topic/section provenance present")
    print(" - figure assets/alt text/anchors checked")
    print(" - textbook practice anchors checked where configured")
    print(" - class-log mappings/assets checked")
    print(" - raw notebook binaries absent from class asset raw folders")
    print(" - student-facing topic prose passed meta-commentary audit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
