---
type: distilled-note
---

# Microsoft Graph Auth Architecture for MCP Excel and OneDrive

## Decision

Use **delegated per-user Graph tokens**, carried to the MCP server as `x-credential-token`. The workflow service owns the OAuth connection and the refresh; the MCP server only consumes the header it is handed.

The ask for the Entra admin is one tenant-wide consent on a new app registration:

| Scope | Why it is needed |
| --- | --- |
| `Files.ReadWrite.All` | Read and write any file the signed-in user can access, including files shared with them and files in SharePoint libraries |
| `Sites.Read.All` | Resolve a site by name or URL and list its document libraries; read-only, no write power on sites |
| `offline_access` | Issue a refresh token, so a connection survives past the \~1 hour access-token lifetime |

Rejected: an app-only service principal with `Sites.ReadWrite.All`. It reaches every site and every OneDrive in the tenant with no sharing check and no user to bound it. The three shapes are compared in [[resources/software-engineering/auth/2026-09-17 - Delegated vs Shared Bot vs App-Only Access|Delegated vs Shared Bot vs App-Only Access]].

## Why Files.ReadWrite.All Is the Scope That Matters

Delegated, it means "read, create, update and delete **all files the signed-in user can access**" — which covers files shared with them and files sitting in SharePoint libraries, not just their own OneDrive. Those libraries are reachable at all because [[resources/software-engineering/auth/2026-09-17 - Sites, Drives and driveItems in Microsoft Graph|every drive sits on some site]].

The scope never grants access. It only lets the app use access the user already has. If a file is not shared to them with edit rights, `Files.ReadWrite.All` gets nothing.

`.All` is widely misread. Delegated, it does not mean "all files in the tenant" — it means the app is not restricted to one specific resource, and SharePoint still enforces the user's own ACL on top. Effective access is [[resources/software-engineering/auth/2026-09-15 - Delegated Access Is Your Rights Intersected With App Scopes|the intersection: app scope ∩ what that user can already open]]. The same string granted app-only has no such intersection, which is the entire difference in blast radius.

Getting the grant is two separate things: [[resources/software-engineering/auth/2026-09-17 - Admin Consent Is Tenant-Wide, Not Per User|who the admin's one consent covers]], and [[resources/software-engineering/auth/2026-09-17 - client_id Selects the App on the Consent Screen|which registration the sign-in actually points at]].

## Where This Codebase Stands

The Google Sheets tools still use a shared account: `get_google_access_token()` prefers `x-credential-token` when present and otherwise falls back to a single shared account held in `GOOGLE_OAUTH_REFRESH_TOKEN`. The Excel and OneDrive tools already follow the delegated model instead: `GRAPH_ACCESS_TOKEN` stays unset in production, so a request with no credential is anonymous rather than running as somebody.

## The MCP Server Does Not Manage Tokens

The MCP server is a pure consumer of whatever token arrives in the header. `get_onedrive_access_token()` returns the contextvar, `graph_request()` attaches `Bearer`, and that is the whole of it. Conditional Access is evaluated by Entra at token issuance, long before a request reaches the server; token lifetime is the credential store's problem.

The workflow service owns the OAuth connection per user, the encrypted refresh token, the minting, and the injection of `x-credential-token` on each call — including [[resources/software-engineering/auth/2026-09-17 - Proactive and Reactive OAuth Token Refresh|both halves of the refresh]].

What the MCP side still owes:

- Never cache the token. It is per-request state and must stay out of `TokenCache`.
- Never log it.
- Keep `GRAPH_ACCESS_TOKEN` unset in production.
- Make an auth failure legible: the Vietnamese message should tell the user to reconnect their Microsoft account, not "request failed". That is the difference between a support ticket and a self-fix.
