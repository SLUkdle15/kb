# Reaching an Internal Service in the Browser

> [!summary]
> Notes on what has to line up for a browser to reach an internal service: the domain has to resolve to an IP (hosts file per machine, or internal DNS for everyone), the certificate has to prove the server is that domain (trusted CA plus a SAN match, which only exists over HTTPS), and the API has to allow our origin to read the response (CORS).

## Distilled notes

- [[resources/software-engineering/infrastructure/2026-08-22 - Internal DNS vs Local Hosts File|Internal DNS vs Local Hosts File]]
- [[resources/software-engineering/infrastructure/2026-08-22 - What the Browser Validates in a TLS Certificate|What the Browser Validates in a TLS Certificate]]
- [[resources/software-engineering/infrastructure/2026-08-22 - CORS Is a Browser Rule About Origins|CORS Is a Browser Rule About Origins]]
