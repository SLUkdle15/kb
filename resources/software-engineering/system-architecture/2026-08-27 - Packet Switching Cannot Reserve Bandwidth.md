---
type: distilled-note
---

# Packet Switching Cannot Reserve Bandwidth

A TCP connection opportunistically uses whatever network bandwidth is available. You can give TCP a variable-sized block of data (e.g., an email or a web page), and it will try to transfer it in the shortest time possible. While a TCP connection is idle, it doesn't use any bandwidth.

Unlike a circuit, then, the bandwidth available over a packet-switched network cannot be reserved ahead of time — and so it cannot be guessed.
