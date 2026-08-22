---
type: distilled-note
---

# Internal DNS vs Local Hosts File

Name resolution can be solved per-machine or once for everyone.

We used to each add the domain-to-IP mapping manually in our local hosts file. DevOps has now put that same mapping on the internal DNS server, so every machine resolves it automatically.

The mapping is the same either way; what changes is who has to maintain it. A hosts-file entry only exists on the machine that has it, so a new laptop or a colleague hitting the same domain fails until someone repeats the step. On the internal DNS server the mapping is maintained once and every machine on the network inherits it.
