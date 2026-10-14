# Work Out SSH to a Server Behind CAPAM

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/ssh-to-a-server-behind-capam|SSH to a Server Behind CAPAM]]
Status: completed 2026-10-14

## Action

Get a working SSH session to a server reached through CAPAM, and settle the three things that get in the way:

- The error the terminal throws.
- Copying between the CAPAM website and the terminal.
- Filling in the SSH password.

## Done When

I can open an SSH session through CAPAM start to finish, and know the fix for each of the three so the next time is not a rediscovery.

## Found So Far

The connection itself works:

```sh
ssh -p <PORT> jump90          # PORT from the address CAPAM shows
# at the password: prompt -> C-b j -> Enter protocol
```

The port comes from the address CAPAM shows, so it changes per session. At the `password:` prompt, `C-b j` is what gets the password in rather than typing it; entering the protocol after that lands on the server behind CAPAM.

Copying from CAPAM into the terminal needed a round trip through the browser until mouse drag selection was disabled in kitty; after that `Ctrl+V` pastes straight into the terminal. The protocol above carries the working version.

The terminal error was never written down, and it stopped getting in the way before this was closed.
