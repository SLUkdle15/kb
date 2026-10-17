# Implement the Refresh Token Flow for Excel

Project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]
Area: [[areas/work-systems/work-systems|Work Systems]]
Deadline: about 2026-12-17 — the hardcoded token's 90 days, counted from the project start on 2026-09-18 (estimated; the issue date was not recorded)

## Action

Replace the hardcoded token with a real refresh token flow for the Excel tools. A hardcoded token will not hold: it stops working after 90 days, and then Excel calls fail until someone swaps it by hand.

Build [[resources/software-engineering/auth/2026-09-17 - Proactive and Reactive OAuth Token Refresh|both halves of the refresh]]: refresh before a token is about to expire, and refresh once and retry on a 401.

Completed: 2026-10-17 — done and deployed.

## Where It Stood

In progress as of 2026-10-17, interrupted by urgent work. Kept undated on purpose: it was calendared for 2026-09-29, 2026-10-12 and 2026-10-13 and moved each time, so it lives here and gets picked up when there is time. The deadline above is the only real date.

## Done When

The Excel tools get fresh tokens through the refresh flow, with no hardcoded token left, so nobody has to replace a token by hand when it expires.
