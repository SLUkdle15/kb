# Agent Rules

## Folder Naming

Use lowercase folder names for vault structure and links.

Current top-level content folders:

```text
inbox
next
projects
areas
resources
archives
raw
```

Use `raw` for attachments, screenshots, PDFs, exports, and other files that are referenced by notes but are not standalone notes.

Use `next` for GTD-style commitments that are more actionable than inbox captures but not necessarily full projects:

- `next/next-actions` for concrete standalone actions to do soon.
- `next/calendar` for date-specific or time-specific commitments.
- `next/maybe` for someday/maybe ideas and possible future projects.
- `next/waiting` for things blocked by someone or something else.

## Tags

Do not use tags for topics, folders, PARA categories, sources, or note types.

Prefer folders for actionability and wiki links for meaning.

Only use tags when they represent temporary workflow status that cuts across folders, such as:

```text
#status/waiting
#status/review
#status/draft
```

If a tag would duplicate a folder name or a linked concept, do not add it.

## Note Naming

When creating a new note from a user capture, prefix the filename with the current date in `YYYY-MM-DD` format.

Use this pattern:

```text
YYYY-MM-DD - Note Title.md
```

Example:

```text
2026-05-24 - Essentialism Core Models.md
```

This keeps notes parseable with simple Unix tools such as:

```sh
find inbox -type f -name '*.md' | sort
```
