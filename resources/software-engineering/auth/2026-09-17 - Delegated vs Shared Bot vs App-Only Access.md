---
type: distilled-note
---

# Delegated vs Shared Bot vs App-Only Access

When an agent acts on someone's files, delegated wins because the agent should never reach further than the person it acts for.

|  | Delegated (per-user) | Shared human account (bot) | App-only service principal |
| --- | --- | --- | --- |
| Reaches | that user's own drive, plus what is shared with them | the bot's own drive, plus what is shared **to the bot** | everything in the tenant |
| Bounded by | sharing | sharing | nothing |
| Audit trail | the real person | one identity for every workflow | the app |
| Setup | admin consent once, then each user connects | someone must share each site to the bot | admin consent once |
| Token upkeep | one refresh token per user | one refresh token, one place | client secret, no user |

The shared bot account is **not** the dangerous option — it is still gated by sharing, exactly like a normal user. Its real problem is drift: after a year it is a member of two hundred sites, its access is the union of everything ever shared to it, and nobody prunes that list.

If unattended access is ever needed — a scheduled job with no user present — the right shape is `Sites.Selected` app-only, where each site owner grants the app access to their own site. Not `Sites.ReadWrite.All`.
