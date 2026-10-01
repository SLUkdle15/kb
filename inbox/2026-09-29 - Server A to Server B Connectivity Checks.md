# Server A to Server B Connectivity Checks

What to check, in order, when a WebClient call from server A to server B fails. Written
down from a debugging session and tidied up, not re-verified against a live case.

## First, Find the IP Range A Calls From

Work down from the application: which pod it runs in, which node that pod sits on, and
which IP range that node belongs to. That range is what A looks like from B's side, and
it is the thing any whitelist has to name — so it is worth having before asking anyone
to open anything.

## Then Work Through the Checks

1. `traceroute -nI` from A to B. This answers one question only: is B reachable at all.
2. Check the port is open on B — both 80 and 443.
3. A traceroute that succeeds does not mean the port is open. Check the port separately
   even when the route looks clean; this is the case that wastes the most time.
4. Where CSOC whitelisting is what guards B, the whitelist is granted to A's IP range,
   and a whitelisted range is normally allowed to traceroute.
5. If CSOC is not guarding A, the two can be made to talk to each other directly.

## Unfinished

The capture breaks off mid-sentence on step 5: in that case "they need some form of
public" — public IP, public route, something else. Fill this in from whoever walked
through it, or drop the clause.
