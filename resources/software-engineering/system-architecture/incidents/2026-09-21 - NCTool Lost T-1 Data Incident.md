# NCTool Lost T-1 Data Incident

Date: 2026-09-21
Area: [[areas/work-systems/work-systems|Work Systems]]

## Background

The NCTool job pulls its data from CSOC. CSOC does not stream that data; it is fetched from upstream, and T-1 data is not available from CSOC on the current day.

## What Happened

A quick change to the job went to production untested and without checking the data availability with CSOC first. The change assumed data CSOC does not provide on the current day, so the production run failed.

## Impact

- The job lost the T-1 day's data.

## Fix

- The change was reverted.
- A manual way to trigger the job over HTTP was opened on production, so a missed run can be re-run by hand.

## Lessons Learned

- Confirm with the data owner (CSOC) when their data is actually available before changing what a job assumes about it.
- Do not ship an untested change to production, even a quick one — see [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]].
