---
type: distilled-note
---

# Consent Can Be Tenant-Wide or Per User

Both paths exist, and tenant policy picks which one you get.

**Admin consent** is granted once per application, for the whole tenant — not once per user. **User consent** is granted by each user at first sign-in, for themselves only. Microsoft's own default does not require admin consent for delegated `Files.ReadWrite.All` or `Sites.ReadWrite.All` (only `Sites.FullControl.All` does), so where self-consent is allowed, the per-user path is the one that runs.

The AI chatbot ended up on the per-user path: each user consents and connects their own Microsoft account. See [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]].

Where the tenant disables self-consent, the shape collapses to: **either the admin opens it for everyone, or nobody can use it** — not an approval queue per person.

To limit who can use the app without limiting what each user reaches, set **Assignment required = Yes** on the enterprise application and assign a group. Unassigned users then fail at sign-in with `AADSTS50105`. This controls *who*, never *what* — there is no per-file restriction for delegated scopes.

One failure mode to plan for: a missing Sites scope usually surfaces as **empty results or a 404, not a clear 403**. Test against a file genuinely shared between two accounts before concluding the setup works.
