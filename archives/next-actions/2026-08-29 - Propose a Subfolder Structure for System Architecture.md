# Propose a Subfolder Structure for System Architecture

Project: [[archives/reorganize-resources-folder/reorganize-resources-folder|Reorganize the Resources Folder]]
Due: 2026-09-01

## Action

`resources/software-engineering/system-architecture` holds ~20 flat notes (mostly DDIA reading notes) plus its `adr/` and `incidents/` subfolders. Read through the flat notes and propose a grouping — likely by DDIA part or topic (storage engines, replication and partitioning, transactions and consistency, distributed systems) — then move notes into the new subfolders and update `system-architecture.md`'s index.

Also file the loose top-level note `resources/software-engineering/2026-05-28 - JavaScript Dev to Main Merge Review.md` into whichever existing subfolder (`infrastructure/`, `testing/`, or a new one) actually fits it.

While going through the notes, rewrite the ones that need it, not just relocate them — some of the ~20 flat notes are likely rough or thin and worth cleaning up as part of this pass rather than moving as-is.

## Done When

`system-architecture/` has topic subfolders, the loose top-level note is filed, and `system-architecture.md` and `software-engineering.md` reflect the new structure.

## Status

Descoped and completed 2026-09-01 without the subfolder split. Discussed live: moving ~20 files just to fix a "looks messy" complaint would touch 20+ inbound links for a cosmetic win, so `system-architecture.md`'s index was regrouped into sections (DDIA book / system overviews / reference) instead — no files moved. The loose JS note was left in place; not addressed this pass. See the parent project's completion note.
