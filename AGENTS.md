# Agent Rules

## Folder Naming

Use lowercase folder names for vault structure and links.

Current top-level content folders:

```text
inbox
projects
areas
resources
archives
raw
```

Use `raw` for attachments, screenshots, PDFs, exports, and other files that are referenced by notes but are not standalone notes.

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
