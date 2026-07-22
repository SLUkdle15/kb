# Reverse Proxy Host Header Rewriting for Third-Party Callbacks

Related area: [[areas/software-architect-growth/software-architect-growth|Software Architect Growth]]

## Core Idea

Expose a single raw IP to the external caller, then rewrite the Host header at
the edge so Kong's hostname-based routing still works.

## How

Client hits HAProxy via raw IP → `path_beg /api` → `set-header Host` → Kong
(matches the route by Host **and** Path together) → upstream service.

## Why It Matters

The single exposed IP is a deliberate simplification for the external caller.
The Host rewrite is how you reconcile that flat IP-based entrypoint with Kong's
hostname-based routing inside.
