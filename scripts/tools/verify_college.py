#!/usr/bin/env python3
"""Generic PankusDesk college architecture verifier — Design Lock v2.

Run from repository root:
    python3 scripts/tools/verify_college.py

Optional subject root(s):
    python3 scripts/tools/verify_college.py college/1-1/basic-electrical-engineering

This verifier checks cross-subject architectural invariants. Subject-specific
source counts, known corpus anomalies and exact syllabus-coverage counts remain
the responsibility of each subject's own kb/tools/verify_kb.py (or equivalent).
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
ALLOWED_FIGURE_ANCHORS = {"before-paragraph", "paragraph", "bullet", "end"}
ALLOWED_GRID_SIDE = {"left", "right"}
ALLOWED_FIGURE_SIZE = {"symbol", "small", "medium", "large"}
DESIGN_LOCK_FILES = [
    REPO / "college" / "COLLEGE_BUILD_STANDARD.md",
    REPO / "college" / "REFERENCE_IMPLEMENTATION.md",
    REPO / "college" / "NOTEBOOK_REDRAW_STYLE.md",
    REPO / "college" / "UNIT_BUILD_CHECKLIST.md",
    REPO / "college" / "schemas" / "subject.schema.json",
    REPO / "college" / "schemas" / "topics.schema.json",
    REPO / "college" / "schemas" / "textbook-questions.schema.json",
    REPO / "college" / "schemas" / "class-log.schema.json",
    REPO / "scripts" / "new" / "study-ui.js",
    REPO / "styles" / "new" / "study-ui.css",
]

META_PATTERNS = [
    r"\bthe class notes?\b",
    r"\bPriyanka(?:'s|’s) notes?\b",
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
BAD_ALT_RE = re.compile(r"^(?:image|figure|fig\.?\s*\d+(?:\.\d+)?|[a-z]?f\d+(?:[-_][a-z0-9]+)?)$", re.I)

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
    if isinstance(topic.get("intro"), str):
        yield "intro", topic["intro"]

    for key in ("learn", "formulas", "method", "cautions"):
        for i, value in enumerate(topic.get(key, []) or []):
            if isinstance(value, str):
                yield f"{key}[{i}]", value

    for si, section in enumerate(topic.get("sections", []) or []):
        if not isinstance(section, dict):
            continue
        if isinstance(section.get("heading"), str):
            yield f"sections[{si}].heading", section["heading"]
        for key in ("paragraphs", "bullets", "accordion_recap"):
            for i, value in enumerate(section.get(key, []) or []):
                if isinstance(value, str):
                    yield f"sections[{si}].{key}[{i}]", value
        for ti, table in enumerate(section.get("tables", []) or []):
            if not isinstance(table, dict):
                continue
            if isinstance(table.get("caption"), str):
                yield f"sections[{si}].tables[{ti}].caption", table["caption"]
            for hi, value in enumerate(table.get("headers", []) or []):
                if isinstance(value, str):
                    yield f"sections[{si}].tables[{ti}].headers[{hi}]", value
            for ri, row in enumerate(table.get("rows", []) or []):
                if not isinstance(row, list):
                    continue
                for ci, value in enumerate(row):
                    if isinstance(value, str):
                        yield f"sections[{si}].tables[{ti}].rows[{ri}][{ci}]", value

        for ai, item in enumerate(section.get("accordions", []) or []):
            if not isinstance(item, dict):
                continue
            if isinstance(item.get("title"), str):
                yield f"sections[{si}].accordions[{ai}].title", item["title"]
            for key in ("paragraphs", "bullets"):
                for i, value in enumerate(item.get(key, []) or []):
                    if isinstance(value, str):
                        yield f"sections[{si}].accordions[{ai}].{key}[{i}]", value

    for qi, item in enumerate(topic.get("self_checks", []) or []):
        if isinstance(item, dict):
            for key in ("question", "answer"):
                if isinstance(item.get(key), str):
                    yield f"self_checks[{qi}].{key}", item[key]


def check_study_table(item, context: str):
    if not isinstance(item, dict):
        errors.append(f"{context}: table is not an object")
        return
    headers = item.get("headers")
    rows = item.get("rows")
    if not isinstance(headers, list) or not headers or any(not isinstance(v, str) or not v.strip() for v in headers):
        errors.append(f"{context}: table needs non-empty string headers")
        return
    if not isinstance(rows, list) or not rows:
        errors.append(f"{context}: table needs at least one row")
        return
    width = len(headers)
    for ri, row in enumerate(rows):
        if not isinstance(row, list):
            errors.append(f"{context}: row {ri} is not an array")
            continue
        if len(row) != width:
            errors.append(f"{context}: row {ri} has {len(row)} cells; expected {width}")
        for ci, value in enumerate(row):
            if isinstance(value, str):
                continue
            if isinstance(value, dict) and value.get("type") == "image":
                src = value.get("src")
                alt = value.get("alt")
                if not isinstance(src, str) or not src.strip():
                    errors.append(f"{context}: row {ri} cell {ci} image missing src")
                else:
                    path = resolve_repo_asset(src)
                    if path is not None and not path.exists():
                        errors.append(f"{context}: row {ri} cell {ci} missing image asset {src}")
                if not isinstance(alt, str) or len(alt.strip()) < 8:
                    errors.append(f"{context}: row {ri} cell {ci} image needs descriptive alt text")
                elif BAD_ALT_RE.fullmatch(alt.strip()):
                    errors.append(f"{context}: row {ri} cell {ci} image alt text is generic/non-descriptive: {alt!r}")
                continue
            errors.append(f"{context}: row {ri} cell {ci} must be a string or image cell")


def collect_topic_figures(topic: dict):
    for si, section in enumerate(topic.get("sections", []) or []):
        if not isinstance(section, dict):
            continue
        paragraphs = section.get("paragraphs", []) or []
        bullets = section.get("bullets", []) or []
        for fi, fig in enumerate(section.get("figures", []) or []):
            yield si, fi, fig, len(paragraphs), len(bullets), section


def configured_source_ids(subject_dir: Path, subject: dict) -> set[str]:
    result: set[str] = set()
    for i, cfg in enumerate(((subject.get("unitRenderer") or {}).get("sources") or [])):
        if not isinstance(cfg, dict):
            errors.append(f"{rel(subject_dir / 'subject.json')}: unitRenderer.sources[{i}] is not an object")
            continue
        source_path = cfg.get("path")
        id_field = cfg.get("idField")
        if not source_path or not id_field:
            errors.append(f"{rel(subject_dir / 'subject.json')}: source config {i} missing path/idField")
            continue
        data = load_json(subject_dir / str(source_path))
        if data is None:
            continue
        collection = cfg.get("collection")
        if collection:
            if not isinstance(data, dict) or collection not in data:
                errors.append(f"{rel(subject_dir / str(source_path))}: configured collection {collection!r} missing")
                continue
            data = data.get(collection)
        if not isinstance(data, list):
            errors.append(f"{rel(subject_dir / str(source_path))}: configured source data is not a list")
            continue
        for item in data:
            if not isinstance(item, dict):
                continue
            source_id = item.get(id_field)
            if isinstance(source_id, str) and source_id:
                result.add(source_id)
    return result


def check_source_refs(refs, known_ids: set[str], context: str):
    if not isinstance(refs, list) or not refs:
        errors.append(f"{context}: no provenance source_refs")
        return
    if known_ids:
        for source_id in refs:
            if source_id not in known_ids:
                errors.append(f"{context}: unresolved source_ref {source_id!r}")


def check_accordion(item, context: str):
    if not isinstance(item, dict):
        errors.append(f"{context}: accordion is not an object")
        return
    title = item.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append(f"{context}: accordion missing title")
    paragraphs = item.get("paragraphs") or []
    bullets = item.get("bullets") or []
    if not paragraphs and not bullets:
        errors.append(f"{context}: accordion has no paragraphs or bullets")
    for key, values in (("paragraphs", paragraphs), ("bullets", bullets)):
        if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
            errors.append(f"{context}: accordion {key} must be an array of strings")


def check_figure(
    fig,
    context: str,
    paragraph_count: int | None,
    bullet_count: int | None,
    *,
    require_placement: bool = False,
):
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
    elif BAD_ALT_RE.fullmatch(alt.strip()):
        errors.append(f"{context}: figure alt text is generic/non-descriptive: {alt!r}")

    size = fig.get("size")
    if size is not None and size not in ALLOWED_FIGURE_SIZE:
        errors.append(f"{context}: invalid figure size {size!r}")

    after = fig.get("after")
    grid = fig.get("grid")
    if after is not None and grid is not None:
        errors.append(f"{context}: figure cannot use both after and grid placement")

    if require_placement and after is None and grid is None:
        errors.append(f"{context}: ready-unit figure has no explicit after/grid placement")

    if after is not None:
        if not isinstance(after, dict) or after.get("type") not in ALLOWED_FIGURE_ANCHORS:
            errors.append(f"{context}: invalid figure insertion anchor")
        else:
            typ = after.get("type")
            idx = after.get("index")
            if typ != "end" and (not isinstance(idx, int) or idx < 0):
                errors.append(f"{context}: invalid figure insertion index")
            if typ in {"before-paragraph", "paragraph"} and paragraph_count is not None and isinstance(idx, int) and idx >= paragraph_count:
                errors.append(f"{context}: paragraph anchor index {idx} out of range ({paragraph_count})")
            if typ == "bullet" and bullet_count is not None and isinstance(idx, int) and idx >= bullet_count:
                errors.append(f"{context}: bullet anchor index {idx} out of range ({bullet_count})")

    if grid is not None:
        if not isinstance(grid, dict):
            errors.append(f"{context}: invalid figure grid placement")
        else:
            start = grid.get("start")
            end = grid.get("end", start)
            side = grid.get("side", "right")
            grid_size = grid.get("size", size or "medium")
            if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end < start:
                errors.append(f"{context}: invalid figure grid paragraph range")
            elif paragraph_count is not None and end >= paragraph_count:
                errors.append(f"{context}: grid paragraph range {start}-{end} out of range ({paragraph_count})")
            if side not in ALLOWED_GRID_SIDE:
                errors.append(f"{context}: invalid figure grid side")
            if grid_size not in ALLOWED_FIGURE_SIZE:
                errors.append(f"{context}: invalid figure grid size")


def load_question_ids(subject_dir: Path, subject: dict, topic_ids: set[str], source_ids: set[str]) -> tuple[set[str], dict | None]:
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
            if not isinstance(group, dict):
                continue
            for q in group.get("questions", []) or []:
                if not isinstance(q, dict):
                    errors.append(f"question record is not an object in {rel(subject_dir / data_path)}")
                    continue
                qid = q.get("id")
                if not qid:
                    errors.append(f"question without id in {rel(subject_dir / data_path)}")
                elif qid in ids:
                    errors.append(f"duplicate question id {qid} in {rel(subject_dir / data_path)}")
                else:
                    ids.add(qid)

                topic_id = q.get("topic_id")
                if topic_id and topic_ids and topic_id not in topic_ids:
                    errors.append(f"question {qid or '?'} points to unknown topic_id {topic_id}")

                for source_id in q.get("answer_source_refs", []) or []:
                    if source_ids and source_id not in source_ids:
                        errors.append(f"question {qid or '?'} unresolved answer_source_ref {source_id!r}")

                ans = q.get("answer") or {}
                if isinstance(ans, dict):
                    for fi, fig in enumerate(ans.get("figures", []) or []):
                        check_figure(fig, f"question {qid or '?'} figure {fi}", None, None)
    return ids, data


def iter_class_text(entry: dict):
    for pi, page in enumerate(entry.get("pages", []) or []):
        if not isinstance(page, dict):
            continue
        for bi, block in enumerate(page.get("blocks", []) or []):
            if not isinstance(block, dict):
                continue
            if isinstance(block.get("text"), str):
                yield f"pages[{pi}].blocks[{bi}]", block["text"]
            if block.get("type") == "pankusdesk-tip":
                if isinstance(block.get("title"), str):
                    yield f"pages[{pi}].blocks[{bi}].title", block["title"]
                for key in ("paragraphs", "bullets"):
                    for ti, text in enumerate(block.get(key, []) or []):
                        if isinstance(text, str):
                            yield f"pages[{pi}].blocks[{bi}].{key}[{ti}]", text
                if isinstance(block.get("example"), str):
                    yield f"pages[{pi}].blocks[{bi}].example", block["example"]
            if block.get("type") == "accordions":
                for ai, item in enumerate(block.get("items", []) or []):
                    if not isinstance(item, dict):
                        continue
                    if isinstance(item.get("title"), str):
                        yield f"pages[{pi}].blocks[{bi}].items[{ai}].title", item["title"]
                    for key in ("question_paragraphs", "paragraphs", "bullets"):
                        for ti, text in enumerate(item.get(key, []) or []):
                            if isinstance(text, str):
                                yield f"pages[{pi}].blocks[{bi}].items[{ai}].{key}[{ti}]", text
                    if isinstance(item.get("final_answer"), str):
                        yield f"pages[{pi}].blocks[{bi}].items[{ai}].final_answer", item["final_answer"]


def check_class_logs(subject_dir: Path, topic_ids: set[str], source_ids: set[str]):
    class_root = subject_dir / "kb" / "class-log"
    if class_root.exists():
        for entry_path in sorted(class_root.glob("*/entry.json")):
            entry = load_json(entry_path)
            if not isinstance(entry, dict):
                continue

            date = entry.get("date")
            if date and entry_path.parent.name != date:
                errors.append(f"{rel(entry_path)}: date does not match directory name")

            source_id = entry.get("source_id")
            if source_ids and source_id not in source_ids:
                errors.append(f"{rel(entry_path)}: source_id does not resolve through subject source collections: {source_id!r}")

            for mapped in entry.get("mapped_topics", []) or []:
                tid = mapped.get("topic_id") if isinstance(mapped, dict) else None
                if tid not in topic_ids:
                    errors.append(f"{rel(entry_path)}: mapped topic does not exist: {tid}")

            for page in entry.get("pages", []) or []:
                for block in page.get("blocks", []) if isinstance(page, dict) else []:
                    if isinstance(block, dict) and block.get("type") == "figure":
                        check_figure(block, f"{rel(entry_path)} class figure", None, None)

            for location, text in iter_class_text(entry):
                if "\\frac" in text:
                    errors.append(f"{rel(entry_path)} {location}: use \\dfrac instead of \\frac")

    raw_dirs = list((subject_dir / "assets" / "class").glob("**/raw")) if (subject_dir / "assets" / "class").exists() else []
    for raw_dir in raw_dirs:
        binaries = [
            p for p in raw_dir.rglob("*")
            if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".heic", ".tif", ".tiff"}
        ]
        if binaries:
            errors.append(f"raw notebook binaries must stay outside website assets: {rel(raw_dir)} ({len(binaries)} file(s))")


def check_class_history(subject_dir: Path, topic: dict, context: str):
    for i, item in enumerate(topic.get("class_history", []) or []):
        if not isinstance(item, dict):
            errors.append(f"{context}: class_history[{i}] is not an object")
            continue
        date = item.get("date")
        href = item.get("href")
        if not date or not href:
            errors.append(f"{context}: class_history[{i}] missing date/href")
            continue
        parsed = urlparse(href)
        qdate = (parse_qs(parsed.query).get("date") or [None])[0]
        if qdate and qdate != date:
            errors.append(f"{context}: class_history[{i}] date {date} does not match href query {qdate}")
        entry_path = subject_dir / "kb" / "class-log" / str(date) / "entry.json"
        if not entry_path.exists():
            errors.append(f"{context}: class_history[{i}] dated entry missing: {rel(entry_path)}")


def verify_subject(subject_dir: Path):
    subject_path = subject_dir / "subject.json"
    subject = load_json(subject_path)
    if not isinstance(subject, dict):
        return

    label = f"{subject.get('semester','?')} / {subject.get('shortName') or subject.get('name') or subject_dir.name}"
    required = ("code", "name", "shortName", "regulation", "semester", "kb", "syllabus", "coverage", "units")
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

    source_ids = configured_source_ids(subject_dir, subject)
    if not source_ids:
        warnings.append(f"{label}: no source IDs resolved from unitRenderer.sources; provenance resolution skipped")

    topic_ids: set[str] = set()
    topics_by_unit: dict[int, int] = {}
    for t in topics:
        if isinstance(t, dict) and isinstance(t.get("id"), str):
            topic_ids.add(t["id"])

    question_ids, _ = load_question_ids(subject_dir, subject, topic_ids, source_ids)

    seen_topic_ids: set[str] = set()
    for t in topics:
        if not isinstance(t, dict):
            errors.append(f"{label}: topic record is not an object")
            continue
        tid = t.get("id")
        unit = t.get("unit")
        if not isinstance(tid, str) or not tid:
            errors.append(f"{label}: topic without id")
            continue
        if tid in seen_topic_ids:
            errors.append(f"{label}: duplicate topic id {tid}")
        seen_topic_ids.add(tid)

        if not isinstance(unit, int) or unit not in unit_numbers:
            errors.append(f"{label}: {tid} points to undefined Unit {unit}")
        else:
            topics_by_unit[unit] = topics_by_unit.get(unit, 0) + 1

        if t.get("status") not in ALLOWED_TOPIC_STATUS:
            errors.append(f"{label}: {tid} invalid topic status {t.get('status')!r}")

        check_source_refs(t.get("source_refs"), source_ids, f"{label}: {tid}")

        for si, section in enumerate(t.get("sections", []) or []):
            if not isinstance(section, dict):
                errors.append(f"{label}: {tid} section {si} is not an object")
                continue

            scontext = f"{label}: {tid} section {si}"
            check_source_refs(section.get("source_refs"), source_ids, scontext)

            if section.get("kind") == "class-note":
                source_label = section.get("source_label")
                if not isinstance(source_label, str) or not source_label.strip():
                    errors.append(f"{scontext}: class-note section missing source_label")
                refs = section.get("source_refs") or []
                if not any(isinstance(ref, str) and ref.startswith("CLASS-") for ref in refs):
                    errors.append(f"{scontext}: class-note section needs a CLASS- source_ref")
                for fi, fig in enumerate(section.get("figures", []) or []):
                    if isinstance(fig, dict) and fig.get("kind") != "class-note":
                        errors.append(f"{scontext} figure {fi}: class-note cumulative figure needs kind='class-note'")

            for ti, table in enumerate(section.get("tables", []) or []):
                check_study_table(table, f"{scontext} table {ti}")

            for ai, accordion in enumerate(section.get("accordions", []) or []):
                check_accordion(accordion, f"{scontext} accordion {ai}")

        if unit in ready_units:
            if not (t.get("sections") or []):
                errors.append(f"{label}: ready-unit topic {tid} has no detailed sections")

            for location, text in visible_topic_strings(t):
                if META_RE.search(text):
                    errors.append(f"{label}: student-facing meta commentary in {tid}.{location}: {text[:100]!r}")
                if "\\frac" in text:
                    errors.append(f"{label}: {tid}.{location} uses \\frac; Design Lock v2 requires \\dfrac")

            for si, fi, fig, pc, bc, _section in collect_topic_figures(t):
                check_figure(fig, f"{label}: {tid} section {si} figure {fi}", pc, bc, require_placement=True)

        for pi, practice in enumerate(t.get("practice", []) or []):
            if not isinstance(practice, dict):
                continue
            anchor = practice.get("anchor")
            if anchor and question_ids and anchor not in question_ids:
                errors.append(f"{label}: {tid} practice[{pi}] anchor {anchor} does not resolve to a textbook question")

        check_class_history(subject_dir, t, f"{label}: {tid}")

    for n in sorted(ready_units):
        if topics_by_unit.get(n, 0) == 0:
            errors.append(f"{label}: Unit {n} is ready but has no topics")
        unit_shell = subject_dir / f"unit-{n}.html"
        if not unit_shell.exists():
            errors.append(f"{label}: ready Unit {n} missing shell {rel(unit_shell)}")

    qcfg = (subject.get("practice") or {}).get("unitQuestions") or {}
    for n in qcfg.get("availableUnits", []) or []:
        shell = subject_dir / str(qcfg.get("hrefPattern", "unit-{unit}-questions.html")).replace("{unit}", str(n))
        if not shell.exists():
            errors.append(f"{label}: Unit {n} marked as having textbook questions but shell is missing: {rel(shell)}")

    ccfg = subject.get("classNotes") or {}
    for n in ccfg.get("availableUnits", []) or []:
        shell = subject_dir / str(ccfg.get("hrefPattern", "unit-{unit}-class-notes.html")).replace("{unit}", str(n))
        if not shell.exists():
            errors.append(f"{label}: Unit {n} marked as having class notes but shell is missing: {rel(shell)}")

    check_class_logs(subject_dir, topic_ids, source_ids)


def verify_calendar_indexes():
    # Validate only links explicitly present; older calendar entries may intentionally have link=null.
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
                hdate = parsed.fragment if re.fullmatch(r"\d{4}-\d{2}-\d{2}", parsed.fragment or "") else None
                linked_date = qdate or hdate
                if linked_date and linked_date != date:
                    errors.append(f"{rel(index_path)} {date}: linked class-note date {linked_date} does not match calendar key")
                subject_dir = shell.parent
                if linked_date:
                    dated = subject_dir / "kb" / "class-log" / linked_date / "entry.json"
                    if not dated.exists():
                        errors.append(f"{rel(index_path)} {date}: dated entry missing for link {link}")


def verify_shared_study_ui_shells():
    renderer_names = {"subject-unit.js", "unit-class-notes.js", "unit-questions.js", "class-log.js"}
    for shell in REPO.glob("college/**/*.html"):
        try:
            text = shell.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if not any(f"scripts/new/{name}" in text for name in renderer_names):
            continue
        if "styles/new/study-ui.css" not in text:
            errors.append(f"{rel(shell)}: shared study UI stylesheet is not loaded")
        if "scripts/new/study-ui.js" not in text:
            errors.append(f"{rel(shell)}: shared study UI renderer is not loaded")


def verify_design_lock_files():
    for path in DESIGN_LOCK_FILES:
        if not path.exists():
            errors.append(f"missing Design Lock v2 file: {rel(path)}")
        elif path.suffix == ".json":
            load_json(path)


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
    parser = argparse.ArgumentParser(description="Verify PankusDesk college architecture (Design Lock v2)")
    parser.add_argument("subjects", nargs="*", help="Optional subject directories or subject.json paths")
    ns = parser.parse_args()

    verify_design_lock_files()
    verify_shared_study_ui_shells()

    subjects = discover_subjects(ns.subjects)
    if not subjects:
        print("COLLEGE VERIFY: FAIL")
        print(" - no college subject.json files found")
        return 1

    for subject_dir in subjects:
        verify_subject(subject_dir)
    verify_calendar_indexes()

    if warnings:
        for warning in warnings:
            print("WARNING:", warning)

    if errors:
        print("COLLEGE VERIFY: FAIL")
        for error in errors:
            print(" -", error)
        return 1

    print("COLLEGE VERIFY: PASS")
    print(f" - {len(subjects)} subject configuration(s) checked")
    print(" - Design Lock v2 contract files present/parseable")
    print(" - shared study UI loaded by all study-content shells")
    print(" - ready units have detailed topic data and shells")
    print(" - topic/section provenance present and configured refs resolved")
    print(" - class-note labels/source refs checked")
    print(" - semantic study tables and explanation accordions checked")
    print(" - figure assets/alt text/explicit anchors/Grid placement checked")
    print(" - textbook practice anchors checked where configured")
    print(" - class-log mappings/assets/calendar links checked")
    print(" - raw notebook binaries absent from class asset raw folders")
    print(" - ready-unit topic/class-log fractions use \\dfrac")
    print(" - student-facing topic/accordion prose passed meta-commentary audit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
