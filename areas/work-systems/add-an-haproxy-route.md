---
type: protocol
---

# Add an HAProxy Route

Source: [[resources/software-engineering/infrastructure/2026-06-22 - Reverse Proxy for Third-Party Callbacks|Reverse Proxy for Third-Party Callbacks]]

Use when a new service needs a path on the shared HAProxy frontend.

## Checklist

- [ ] Settle the two facts first: the path prefix callers will use (`/econtract/`), and the upstream's real hostname plus server IPs.
- [ ] In the frontend, add the acl: `acl is_econtract path_beg /econtract/`.
- [ ] Negate the new acl on the `http-request redirect scheme https` line, alongside the existing services.
- [ ] Add `use_backend econtract_k8s if is_econtract`.
- [ ] Write the backend: `mode http`, `http-request set-header Host <upstream hostname>`, `option forwardfor except 127.0.0.1/8`, and one `server ... check` line per upstream IP.
- [ ] Validate before touching the running process: `haproxy -c -f /etc/haproxy/haproxy.cfg`.
- [ ] `systemctl reload haproxy`, then `systemctl status haproxy`.
- [ ] Curl the path end to end — a clean reload only proves the config parsed.

## Notes

- `set-header Host` is the whole point of the backend. The caller arrives at a raw IP with the wrong Host; the upstream matches its own routes on the hostname it expects.
- The redirect line is the step that gets forgotten. Miss the negation and plain-HTTP callers get bounced to HTTPS — which breaks exactly the third parties who cannot follow a redirect.
- `reload` re-reads the config without dropping established connections; `restart` drops them. Never reach for `restart` to fix a config mistake.
- `check` on each server is what makes the pair a failover rather than two names in a file.
