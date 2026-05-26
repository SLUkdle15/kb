#!/usr/bin/env python3
"""Build a lightweight Obsidian vault index and lint report."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WIKI_LINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_RE = re.compile(r"https?://[^\s)>]+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
TAG_RE = re.compile(r"(?<![\w/])#([A-Za-z][\w/-]*)")
DATE_RE = re.compile(
    r"\b(?:20\d{2}-\d{2}-\d{2}|20\d{2}|Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|"
    r"May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\b",
    re.IGNORECASE,
)
TIME_SENSITIVE_RE = re.compile(
    r"\b(current|currently|latest|recent|newest|best|today|now|pricing|price|version|"
    r"deprecated|roadmap|deadline|schedule|law|policy|regulation|market|forecast)\b",
    re.IGNORECASE,
)
UNRESOLVED_RE = re.compile(r"\b(TODO|FIXME|TBD|question|unclear|verify|check|research)\b|\?", re.IGNORECASE)
CONCEPT_RE = re.compile(r"\b[A-Z][A-Za-z0-9]+(?:\s+[A-Z][A-Za-z0-9]+){1,4}\b")
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

EXCLUDED_DIRS = {
    ".git",
    ".obsidian",
    ".trash",
    ".agents",
    "node_modules",
    ".venv",
    "__pycache__",
}


@dataclass
class Note:
    path: str
    folder: str
    filename: str
    stem: str
    title: str
    h1: str | None
    headings: list[str]
    wiki_links: list[str]
    resolved_wiki_links: list[str]
    broken_wiki_links: list[str]
    backlinks: list[str]
    external_links: list[str]
    tags: list[str]
    word_count: int
    modified_time: str
    dates_mentioned: list[str]
    time_sensitive_terms: list[str]
    unresolved_markers: list[str]
    has_next_actions_section: bool
    links_to_next_actions: list[str]
    links_back_to_projects: list[str]
    links_to_context: list[str]


def rel(path: Path, vault: Path) -> str:
    return path.relative_to(vault).as_posix()


def iter_markdown(vault: Path) -> list[Path]:
    files: list[Path] = []
    for path in vault.rglob("*.md"):
        if set(path.relative_to(vault).parts) & EXCLUDED_DIRS:
            continue
        files.append(path)
    return sorted(files, key=lambda p: rel(p, vault).lower())


def normalize_title(value: str) -> str:
    value = value.strip().split("|", 1)[0].split("#", 1)[0]
    if value.lower().endswith(".md"):
        value = value[:-3]
    return re.sub(r"\s+", " ", value).strip().lower()


def display_link_target(value: str) -> str:
    return value.strip().split("|", 1)[0].split("#", 1)[0].strip()


def strip_code(text: str) -> str:
    text = FENCED_BLOCK_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def first_h1(text: str) -> str | None:
    for match in HEADING_RE.finditer(text):
        if len(match.group(1)) == 1:
            return match.group(2).strip()
    return None


def unique_sorted(values: list[str] | set[str]) -> list[str]:
    return sorted(set(v for v in values if v), key=str.lower)


def build_aliases(paths: list[Path], vault: Path, texts: dict[Path, str]) -> dict[str, set[str]]:
    aliases: dict[str, set[str]] = defaultdict(set)
    for path in paths:
        path_rel = rel(path, vault)
        candidates = {path.stem, path_rel, path_rel[:-3], path.name}
        h1 = first_h1(texts[path])
        if h1:
            candidates.add(h1)
        for candidate in candidates:
            key = normalize_title(candidate)
            if key:
                aliases[key].add(path_rel)
    return aliases


def resolve_wiki(raw: str, aliases: dict[str, set[str]]) -> str | None:
    matches = aliases.get(normalize_title(raw), set())
    if len(matches) == 1:
        return next(iter(matches))
    return None


def extract_note(path: Path, vault: Path, text: str, aliases: dict[str, set[str]]) -> Note:
    path_rel = rel(path, vault)
    prose = strip_code(text)
    headings = [m.group(2).strip() for m in HEADING_RE.finditer(prose)]
    h1 = first_h1(prose)
    wiki_raw = [display_link_target(m.group(1)) for m in WIKI_LINK_RE.finditer(prose)]

    resolved = []
    broken = []
    for target in wiki_raw:
        resolved_target = resolve_wiki(target, aliases)
        if resolved_target:
            resolved.append(resolved_target)
        else:
            broken.append(target)

    external_links = set(URL_RE.findall(prose))
    for target in MD_LINK_RE.findall(prose):
        if target.startswith(("http://", "https://")):
            external_links.add(target)

    folder = path.parent.relative_to(vault).as_posix()
    if folder == ".":
        folder = ""

    words = re.findall(r"\b[\w'-]+\b", prose)
    return Note(
        path=path_rel,
        folder=folder,
        filename=path.name,
        stem=path.stem,
        title=h1 or path.stem,
        h1=h1,
        headings=headings,
        wiki_links=unique_sorted(wiki_raw),
        resolved_wiki_links=unique_sorted(resolved),
        broken_wiki_links=unique_sorted(broken),
        backlinks=[],
        external_links=unique_sorted(external_links),
        tags=unique_sorted(["#" + m.group(1) for m in TAG_RE.finditer(prose)]),
        word_count=len(words),
        modified_time=datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat(),
        dates_mentioned=unique_sorted([m.group(0) for m in DATE_RE.finditer(prose)]),
        time_sensitive_terms=unique_sorted([m.group(1).lower() for m in TIME_SENSITIVE_RE.finditer(prose)]),
        unresolved_markers=unique_sorted([m.group(0) for m in UNRESOLVED_RE.finditer(prose)]),
        has_next_actions_section=any(h.lower() == "next actions" for h in headings),
        links_to_next_actions=unique_sorted([p for p in resolved if p.startswith("next/next-actions/")]),
        links_back_to_projects=unique_sorted([p for p in resolved if p.startswith("projects/")]),
        links_to_context=unique_sorted([
            p for p in resolved
            if p.startswith(("projects/", "areas/", "resources/"))
        ]),
    )


def concept_candidates(texts: dict[Path, str], aliases: dict[str, set[str]], vault: Path) -> list[dict[str, Any]]:
    stop = {
        "Current Projects",
        "Modified Date",
        "Next Actions",
        "Purpose Maintain",
        "Related Resources",
        "Review Frequency Review",
        "Review Rhythm Review",
        "Table Of Contents",
        "What Belongs Here",
        "What Does Not Belong Here",
    }
    counts: Counter[str] = Counter()
    paths_by_concept: dict[str, set[str]] = defaultdict(set)
    for path, text in texts.items():
        prose = strip_code(text)
        prose = HEADING_RE.sub("", prose)
        for match in CONCEPT_RE.finditer(prose):
            concept = re.sub(r"\s+", " ", match.group(0).strip())
            if concept in stop or len(concept) < 5 or normalize_title(concept) in aliases:
                continue
            if concept.lower().startswith(("the ", "this ", "that ")):
                continue
            counts[concept] += 1
            paths_by_concept[concept].add(rel(path, vault))

    return [
        {"concept": concept, "mentions": count, "sample_paths": sorted(paths_by_concept[concept])[:5]}
        for concept, count in counts.most_common(40)
        if count >= 3
    ]


def markdown_list(items: list[str], empty: str = "None found.") -> str:
    if not items:
        return empty
    return "\n".join(f"- {item}" for item in items)


def write_report(index: dict[str, Any], out_dir: Path) -> None:
    notes = index["notes"]
    issues = index["issues"]
    lines = [
        f"# Lint Index - {datetime.now().date().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Notes indexed: {len(notes)}",
        f"- Broken wiki links: {len(issues['broken_wiki_links'])}",
        f"- Orphan notes: {len(issues['orphan_notes'])}",
        f"- Projects missing next actions: {len(issues['projects_missing_next_actions'])}",
        f"- Next actions missing context links: {len(issues['next_actions_missing_context_links'])}",
        f"- Notes with time-sensitive terms: {len(issues['stale_candidates'])}",
        f"- Repeated missing wiki links: {len(issues['repeated_missing_wiki_links'])}",
        "",
        "## Projects Missing Next Actions",
        "",
        markdown_list(issues["projects_missing_next_actions"]),
        "",
        "## Broken Wiki Links",
        "",
        markdown_list([f"{i['source']} -> [[{i['target']}]]" for i in issues["broken_wiki_links"][:80]]),
        "",
        "## Repeated Missing Wiki Links",
        "",
        markdown_list([
            f"[[{i['target']}]] mentioned {i['count']} times in {', '.join(i['sources'][:5])}"
            for i in issues["repeated_missing_wiki_links"][:40]
        ]),
        "",
        "## Orphan Notes",
        "",
        markdown_list(issues["orphan_notes"][:120]),
        "",
        "## Stale Claim Candidates",
        "",
        markdown_list([f"{i['path']} ({', '.join(i['terms'][:8])})" for i in issues["stale_candidates"][:80]]),
        "",
        "## Possible Missing Concept Pages",
        "",
        markdown_list([f"{i['concept']} ({i['mentions']} mentions)" for i in issues["concept_candidates"][:40]]),
        "",
        "## Inbox Candidates",
        "",
        markdown_list(issues["inbox_candidates"][:80]),
        "",
        "## Next Actions Missing Context Links",
        "",
        markdown_list(issues["next_actions_missing_context_links"]),
        "",
    ]
    (out_dir / "report.md").write_text("\n".join(lines), encoding="utf-8")


def write_log(index: dict[str, Any], vault: Path, out_dir: Path, log_path: Path) -> None:
    issues = index["issues"]
    notes_count = len(index["notes"])
    report_path = (out_dir / "report.md").as_posix()
    entry = [
        f"## [{datetime.now().date().isoformat()}] lint | Vault health check",
        "",
        f"- Indexed {notes_count} notes",
        f"- Broken wiki links: {len(issues['broken_wiki_links'])}",
        f"- Orphan notes: {len(issues['orphan_notes'])}",
        f"- Projects missing next actions: {len(issues['projects_missing_next_actions'])}",
        f"- Stale-claim candidates: {len(issues['stale_candidates'])}",
        f"- Report: {report_path}",
        "",
    ]

    if not log_path.is_absolute():
        log_path = vault / log_path

    if log_path.exists() and log_path.read_text(encoding="utf-8", errors="replace").strip():
        prefix = "\n"
    else:
        prefix = ""
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(prefix + "\n".join(entry))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", default=".", help="Vault root directory")
    parser.add_argument("--out", default="/tmp/vault-lint", help="Output directory")
    parser.add_argument("--log", default="log.md", help="Append a compact lint entry to this log path")
    parser.add_argument("--no-log", action="store_true", help="Do not append to log.md")
    args = parser.parse_args()

    vault = Path(args.vault).resolve()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    paths = iter_markdown(vault)
    texts = {path: path.read_text(encoding="utf-8", errors="replace") for path in paths}
    aliases = build_aliases(paths, vault, texts)
    notes = [extract_note(path, vault, texts[path], aliases) for path in paths]

    backlinks: dict[str, set[str]] = defaultdict(set)
    for note in notes:
        for target in note.resolved_wiki_links:
            backlinks[target].add(note.path)
    for note in notes:
        note.backlinks = unique_sorted(backlinks.get(note.path, set()))

    broken = []
    missing_counter: Counter[str] = Counter()
    missing_sources: dict[str, set[str]] = defaultdict(set)
    for note in notes:
        for target in note.broken_wiki_links:
            broken.append({"source": note.path, "target": target})
            missing_counter[target] += 1
            missing_sources[target].add(note.path)

    repeated_missing = [
        {"target": target, "count": count, "sources": sorted(missing_sources[target])}
        for target, count in missing_counter.most_common()
        if count >= 2
    ]

    project_notes = [
        note for note in notes
        if note.path.startswith("projects/") and note.path.lower() != "projects/projects.md"
    ]
    projects_missing = [
        note.path for note in project_notes
        if not note.has_next_actions_section or not note.links_to_next_actions
    ]

    next_action_notes = [
        note for note in notes
        if note.path.startswith("next/next-actions/") and note.path != "next/next-actions/next-actions.md"
    ]
    next_missing_context = [
        note.path for note in next_action_notes
        if not note.links_to_context
        and not any(src.startswith(("projects/", "areas/", "resources/")) for src in note.backlinks)
    ]

    root_allowlist = {"index.md", "AGENTS.md", "log.md"}
    orphan_notes = [
        note.path for note in notes
        if not note.backlinks
        and note.path not in root_allowlist
        and not note.path.startswith("archives/")
    ]

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "vault": str(vault),
        "notes": [asdict(note) for note in notes],
        "issues": {
            "broken_wiki_links": broken,
            "repeated_missing_wiki_links": repeated_missing,
            "orphan_notes": orphan_notes,
            "projects_missing_next_actions": projects_missing,
            "next_actions_missing_context_links": next_missing_context,
            "stale_candidates": [
                {
                    "path": note.path,
                    "terms": note.time_sensitive_terms,
                    "dates": note.dates_mentioned[:10],
                    "external_links": note.external_links[:5],
                }
                for note in notes
                if note.time_sensitive_terms
            ],
            "concept_candidates": concept_candidates(texts, aliases, vault),
            "inbox_candidates": [note.path for note in notes if note.path.startswith("inbox/")],
        },
    }

    (out_dir / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    write_report(index, out_dir)
    if not args.no_log:
        write_log(index, vault, out_dir, Path(args.log))
    print(f"Wrote {out_dir / 'index.json'}")
    print(f"Wrote {out_dir / 'report.md'}")
    if not args.no_log:
        print(f"Appended {Path(args.log).as_posix()}")
    print(f"Indexed {len(notes)} notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
