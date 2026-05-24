# Agent Rules

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
find Inbox -type f -name '*.md' | sort
```
