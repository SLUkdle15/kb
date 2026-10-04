---
type: protocol
---

# Check Server-to-Server Connectivity

Use when a WebClient call from server A to server B fails.

## Checklist

- [ ] Find A's source IP range: pod → node → the node's IP range. Have it before asking anyone to open anything.
- [ ] `traceroute -nI` from A to B — is B reachable at all?
- [ ] `traceroute -nT -p 443` from A to B — the same route over TCP to the port itself. Needs root.
- [ ] Check ports 80 and 443 are open on B, even if the traceroute was clean.
- [ ] If CSOC guards B, request the whitelist for A's IP range.
- [ ] If CSOC does not guard A, connect the two directly.

## Notes

- A clean `-I` traceroute says nothing about the port. Skipping the port check is what wastes the most time.
- `-I` probes with ICMP, which firewalls often treat differently from real traffic. `-T -p 443` sends TCP SYNs to 443, so it follows the path the WebClient call takes. Without `-T`, `-p` only sets the starting UDP port and climbs per probe — it does not test 443.
- A whitelisted range is normally allowed to traceroute, so a failed traceroute from a whitelisted range is itself a signal.
- The direct-connection case is unfinished — the original capture said it "needs some form of public" something. Fill it in the next time it comes up.
