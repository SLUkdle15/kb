# Examine the Excel Clone Sheet Tool

Project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]
Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Action

The clone tool today clones the whole OneDrive file, not a sheet. Work out whether that is the intended ceiling or a gap worth closing.

Start from what is already settled in [[projects/give-the-ai-chatbot-excel-tools/gotchas|Gotchas]] rather than rediscovering it: Graph has no worksheet copy in v1.0 or beta, and `Worksheet.copy()` is Office.js, which only runs inside Excel. So a native per-sheet clone is not on the table — the open question is whether a read-the-range-and-write-it-into-a-new-sheet path is worth building, or whether file-level clone is what callers actually need.

Also check the other half recorded there: `onedrive_copy_item` is async and returns only a `monitor_url`, so nothing polls it and the new file's id is unavailable. If the current file clone works anyway, find out what it does instead.

## Done When

The gap is named — per-sheet clone is either scoped as work or explicitly cut, with the reason written into the gotchas note so it stays settled.

## Status

Obsolete 2026-09-25 — the question was already settled. The tool clones at file level through `onedrive_copy_item`, and that is the ceiling rather than a gap: a native per-sheet clone does not exist in Graph. Nothing left to examine.
