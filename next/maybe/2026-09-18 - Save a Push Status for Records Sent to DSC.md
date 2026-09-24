# Save a Push Status for Records Sent to DSC

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

NCTool pulls one way today, so nothing on our side records that a given record went to DSC. When a record is missing, there is no way to tell the two causes apart: the data was never there, or the job missed it. Those need opposite fixes, and right now both look identical.

Store a status per record at push time, enough to answer "did this one go, and when". That is what makes a check against the CSOC side possible — compare what we say we pushed against what they received, instead of guessing from absence.

Related: [[2026-09-11 - Reschedule the NCTool Job Past the Two-Hour Assumption|Reschedule the NCTool Job Past the Two-Hour Assumption]] — the same blind spot, that what the job actually did is not recorded anywhere.

## Done When

A pushed record carries a status that can be looked up, and one real record has been traced end to end against CSOC.
