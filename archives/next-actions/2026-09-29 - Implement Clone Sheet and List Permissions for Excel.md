# Implement Clone Sheet for Excel

Project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]
Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Build a per-sheet clone for the Excel tools. Someone actually needs it, which reverses the 2026-09-25 cut — see [[archives/next-actions/2026-09-25 - Examine the Excel Clone Sheet Tool|Examine the Excel Clone Sheet Tool]], where per-sheet clone was closed as a dead end on the grounds that no caller wanted it.

The dead end was only the native path. Graph has no worksheet copy in v1.0 or beta and `Worksheet.copy()` is Office.js ([[projects/give-the-ai-chatbot-excel-tools/gotchas|Gotchas]]), so this is the other path that note named: read the source range and write it into a new sheet.

Settle what a copy carries before building it. A read-and-write path moves values; formulas, number formats, column widths, merged cells, conditional formatting, and charts do not come along for free. Ask the person who needs it which of those matter, because "clone" will be read as "identical" otherwise.

Watch the write-then-read lag from the gotchas note — verifying the new sheet immediately after writing it can show nothing there.

Also:

- Add the list permission.
- Contact thienbm.

## Done When

A caller can clone a worksheet inside a workbook through the tool, and the gotchas note records what the clone carries and what it drops.
