---
type: distilled-note
---

# Delegated Access Is Your Rights Intersected With App Scopes

In a delegated OAuth 2 flow, rights arrive through a chain, and each link can only narrow what the one above it granted.

```text
FPT Software (tenant admin)
   │  grants you a licensed account → you get a OneDrive + ACLs on sites
   ▼
You (KhangLD5@fpt.com)          ← has real rights on content, log in via oauth 2
   │  consents to delegate SOME of those rights
   ▼
The app: graph explorer                          ← has ZERO rights of its own
   │  gets a token carrying `scp`
   ▼
effective access = your ACL  ∩  the app's consented scopes
```

The tenant admin is the only source of rights on content: a licensed account comes with a OneDrive and ACLs on sites. You hold those rights for real. The app holds none of its own — Graph Explorer is not a principal with a share of the tenant, it is a piece of software you sign into.

What the app gets is a token carrying `scp`, the scopes you consented to delegate. That consent is a subset of your rights, never an extension of them.

So effective access is the intersection: your ACL ∩ the app's consented scopes. Broad scopes on a token do not reach files you cannot open, and a wide ACL does not help an app you only consented to read with. Both have to allow the call — which is the model any Microsoft Graph client sits on, including an [[next/next-actions/2026-09-11 - Add an Excel Online MCP Server to the AI Chatbot|Excel Online MCP server]].
