---
type: distilled-note
---

# Reverse Proxy for Third-Party Callbacks

A third-party caller gets one simple entrypoint, a raw IP, and a reverse proxy in front of Kong adapts the request so Kong's routing still works.

The chain is `Client (raw IP) → Reverse Proxy (HAProxy) → Kong → upstream service`. HAProxy takes each incoming request and reshapes it into whatever Kong needs to match its route before passing it on.

The caller never has to know how Kong matches routes. The entrypoint stays simple for the outside party, and Kong's routing stays as it is.
