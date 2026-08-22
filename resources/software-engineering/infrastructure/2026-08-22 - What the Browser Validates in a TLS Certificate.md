---
type: distilled-note
---

# What the Browser Validates in a TLS Certificate

The browser checks two things about the certificate the server sends:

- Is it signed by a CA my machine already trusts?
- Is the domain I typed listed in the cert's SAN (**Subject Alternative Name**) field?

If either check fails, the server hasn't proved it's the domain I asked for, so the browser warns.

## Why HTTP Never Warns

HTTP has no certificate, so there's nothing to validate and no warning. HTTPS wraps the same protocol in TLS, and that's where the CA and SAN checks happen. The absence of a warning on HTTP is not the absence of a problem — it means identity was never checked at all.
