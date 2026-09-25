# Gotchas

## Will bite your data

**Dates are a lie on this tenant.** `10/01/2026` is stored as 1 October, not 10 January — Excel reads d/m/y as US m/d/y whenever the day is ≤ 12. It displays as `10/1/2026`, so a reader sees one thing and arithmetic gets another. `20/01/2026` survives as text only because 20 can't be a month, which is why one column ends up half dates, half text. Right-aligned = real date, left-aligned = text. Prefix with `'` to keep it text.

**A read right after a write can show the old data.** Graph has no read-your-writes guarantee here, and the lag is variable — 4s wasn't enough once, 2s was enough the next time. I nearly reported a lost write over this; the row was there all along. If a workflow writes then immediately reads, it can conclude the write failed.

**OneDrive search lags deletes by minutes.** A deleted file still shows in `onedrive_search_items`. Verify with `onedrive_get_item`, not the search result — I chased a phantom leftover file doing exactly this.

## Will waste your time debugging

**Every OneDrive failure says the same sentence.** `"Microsoft Graph request failed."`, cause buried in `details`. You can't tell a transient lock (retry works) from a permission denial (retry never works) — a delete failed then succeeded unchanged, and the message was identical to a fatal error. Google Drive's tools name the operation instead. This is the one unfixed item on the list.

**Swagger's server/tool fields don't reset when you change the body.** That's the `file_name` `Field required` error you hit — right b[…]

**The test suite only passes on a** […] **errors under `venv/bin/python`,** pre-existing — the goldens were recorded with the stub harness active. So they're green everywhere except the environment that resembles production.

**A stubbed dependency makes tests pass while producing nothing.** `stubs.py` swaps in a `MagicMock`, so `wb.save(buf)` would write zero bytes and the "is it a valid xlsx" assertion would still go green. That's why the blank workbook is hand-rolled `zipfile`.

## Architectural dead ends

**Graph has no worksheet copy** — not in v1.0, not in beta. The `Worksheet.copy()` you're thinking of is Office.js, which only runs inside Excel. Don't build `clone_sheet`.

**`onedrive_copy_item` is async and nothing polls it.** It returns a `monitor_url` only, so you can't get the new file's id and can't […]hat blocks `clone_spreadsheet`, not the copy itself.

**Graph has no domain-scope sharing.** `createLink` takes `anonymous | organization | users`. Drive's `{type: "domain", domain: "fpt.co`[…]

**Excel writes can never go app-only.** `range/insert` is delegated-only — Graph lists Application as "Not supported". Fine today (the repo uses `refresh_token`), but it pins that choice.

## Process

**Check contracts by running both tools, not by reading them.** `excel_create_workbook` and `create_spreadsheet` shared zero top-level keys and I'd written it myself believing it matched. Twice more a bad test fixture produced a plausible wrong answer that looked like a real bug.

**Pin `.gitlab-ci.yml` by hand on ev**[…]ves it cleanly to the wrong version — no conflict, no warnin[…]ts prod pipeline. It happened to need no intervention this time o[…]e reset the base; don't rely on that.
