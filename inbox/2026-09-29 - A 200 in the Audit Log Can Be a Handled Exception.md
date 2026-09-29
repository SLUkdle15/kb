# A 200 in the Audit Log Can Be a Handled Exception

Related area: [[areas/work-systems/work-systems|Work Systems]]

Raw capture from debugging `fcm-template-service`. Not filed yet — the logging collection in `resources/software-engineering` is the likely home once it is worth keeping.

One audit line in `fcm-template-service` read `-> 200` and `19902ms`. It looks like a filter bug — a request that plainly failed, logged as success, and twenty seconds of it. Neither number was wrong. Both had causes worth keeping, because both are the kind that survive the specific incident.

## The 200 Is by Design

`GlobalExceptionHandler.handleCallApiException` is annotated `@ResponseStatus(value = HttpStatus.OK)` (`fcm-template-service/.../GlobalExceptionHandler.java:139`). A `CallApiException` thrown by `DscaiApiClient.getOauthAccessToken` is mapped to HTTP 200 with an error body carrying `errorCode 500`. `AuditLoggerFilter` records the status of the response it actually sees, so it faithfully logs `-> 200`.

The filter is not lying. The handler decided the status before the filter looked at it, and a handled exception is, by that point, a successful response with a disappointing body.

What this costs is searchability: **filtering these logs by HTTP status will not find the failures.** The failure signal lives in the body's `errorCode`, not the status line — see [[areas/work-systems/read-the-json-logs|Read the JSON Logs]] for getting at it.

## The 19902ms Is OkHttp's Default

`ApiClient` never calls `setConnectTimeout` or `setReadTimeout`, so it rides OkHttp's defaults. The ~20 seconds is the socket timeout burning down before the client gives up.

An unset timeout is not the absence of a timeout — it is the library's timeout instead of yours. Twenty seconds is far too long to hold a request for a token fetch that is not coming back, and it is only ever visible as an odd duration in a log line, because nothing throws until it expires.

Setting connect and read timeouts explicitly on `ApiClient` is the open item here.
