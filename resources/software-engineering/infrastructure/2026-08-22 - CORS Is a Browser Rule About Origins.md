---
type: distilled-note
---

# CORS Is a Browser Rule About Origins

CORS is a browser rule about origins — an origin being the `scheme://host:port` a page is loaded from, like `https://a.fpt.net`.

Frontend code running on that origin can't read a response from `a-api.fpt.net` unless that API allows it. Spring returns `Access-Control-Allow-Origin: https://a.fpt.net`, and the browser then permits the read while any other site stays blocked.

The permission is granted by the API and enforced by the browser. The header names which origin is allowed, so it opens the read for our frontend only, not for the web generally.
