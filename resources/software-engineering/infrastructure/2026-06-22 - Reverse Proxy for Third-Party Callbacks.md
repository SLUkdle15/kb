# Reverse Proxy for Third-Party Callbacks

## Core Idea
Put a reverse proxy between the client and Kong. Expose one simple entrypoint (raw IP) to the caller; let the proxy adapt the request so Kong's routing still works.

## How 
Use a reverse proxy (e.g. HAProxy) to sit in front of Kong and reshape the incoming request into whatever Kong needs to match its route.

## Diagram 

``` Client (raw IP) → Reverse Proxy (HAProxy) → Kong → upstream service ```
