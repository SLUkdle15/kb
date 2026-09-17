---
type: distilled-note
---

# Admin Consent Is Tenant-Wide, Not Per User

Admin consent is granted once per application, for the whole tenant — not once per user. Microsoft's own default does not even require admin consent for delegated `Files.ReadWrite.All` or `Sites.ReadWrite.All` (only `Sites.FullControl.All` does). What forces it is tenant policy: FPT disables user self-consent, so nobody can approve these for themselves.

So the shape is: **either the admin opens it for everyone, or nobody can use it.** Not an approval queue per person.

To limit who can use the app without limiting what each user reaches, set **Assignment required = Yes** on the enterprise application and assign a group. Unassigned users then fail at sign-in with `AADSTS50105`. This controls *who*, never *what* — there is no per-file restriction for delegated scopes.

One failure mode to plan for: a missing Sites scope usually surfaces as **empty results or a 404, not a clear 403**. Test against a file genuinely shared between two accounts before concluding the setup works.
