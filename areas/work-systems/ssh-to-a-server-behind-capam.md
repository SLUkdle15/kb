---
type: protocol
---

# SSH to a Server Behind CAPAM

Use when a server is only reachable through the CAPAM jump host.

## Checklist

- [ ] Open the server's entry in CAPAM and read the address it shows — the port is the part that matters.
- [ ] `ssh -p <PORT> jump90` with that port.
- [ ] At the `password:` prompt, `C-b j` to get the password in rather than typing it.
- [ ] Enter the protocol; that lands on the server behind CAPAM.
- [ ] To move text from CAPAM into the terminal, copy it in CAPAM and paste with `Ctrl+V`.

## Notes

- The port changes per session, so it is read from CAPAM each time rather than remembered.
- `Ctrl+V` only pastes once mouse drag selection is disabled in kitty. While it was on, the drag took the selection and the only way across was a round trip through the browser: highlight, paste into the browser, copy there, paste back into the terminal.
