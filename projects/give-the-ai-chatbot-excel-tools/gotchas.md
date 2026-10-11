# Gotchas

## Will bite your data

**Dates are a lie on this tenant.** `10/01/2026` is stored as 1 October, not 10 January — Excel reads d/m/y as US m/d/y whenever the day is ≤ 12. It displays as `10/1/2026`, so a reader sees one thing and arithmetic gets another. `20/01/2026` survives as text only because 20 can't be a month, which is why one column ends up half dates, half text. Right-aligned = real date, left-aligned = text. Prefix with `'` to keep it text.

## Will waste your time debugging

**Serial Graph calls add up past the request timeout — and parallel costs you throttling.** The clone is one request that fans out into many Graph calls; made one after another, their times add up and the original request times out. Implementing them in parallel fixes the wait but costs throttling: fired all at once, the calls hit Graph's rate limits. So parallel, but throttled. 
Background: [How to avoid getting throttled or blocked in SharePoint Online](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

**A fixed range like `A1:A100000` loads every row you named.** The clone timed out on exactly this: one request fanning out into serial Graph calls, each returning 100,000 rows whether or not anything was in them. The sheet wasn't big — the address was. Excel accepts an open-ended column reference, `A:A`, which resolves against the used range instead, so the read stops at the last row that holds data. Same tool, a fraction of the payload. Fixed 2026-10-05.

## Architectural dead ends

**Graph has no worksheet copy**

**`onedrive_copy_item` is async and nothing polls it.** It returns a `monitor_url` only