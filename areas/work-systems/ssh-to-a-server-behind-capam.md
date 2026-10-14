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
- [ ] To move text between the CAPAM page and the terminal, copy with `Ctrl+Shift+C` and paste with `Ctrl+Shift+V`.

## Notes

- The port changes per session, so it is read from CAPAM each time rather than remembered.
- `Ctrl+Shift+C` / `Ctrl+Shift+V` only work with `set -g mouse off` in the tmux config. With mouse mode on, tmux takes the selection and the only way across was a round trip through the browser: highlight, paste into the browser, copy there, paste back into the terminal.
