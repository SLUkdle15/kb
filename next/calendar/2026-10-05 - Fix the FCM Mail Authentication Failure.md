# Fix the FCM Mail Authentication Failure

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/read-the-json-logs|Read the JSON Logs]]
Due: 2026-10-05

## Action

`MailService.sendEmail` in FCM `common-service` is failing SMTP authentication, so outgoing mail is silently dropped — the call is `@Async`, so nothing upstream sees the failure. Caught on 2026-10-02:

```text
2026-10-02 09:29:33.081 [common-service-task-2] ERROR o.s.a.i.SimpleAsyncUncaughtExceptionHandler:
Unexpected exception occurred invoking async method:
public void vn.com.fpt.fcm.services.app.service.MailService.sendEmail(...MailRequest)
org.springframework.mail.MailAuthenticationException: Authentication failed;
nested exception is javax.mail.AuthenticationFailedException: 535 5.7.3 Authentication unsuccessful
```

535 5.7.3 is the mail server rejecting the credentials, not the app failing to reach it — so the question is which of four things changed:

- The mailbox password expired or was rotated, and the config still carries the old one.
- SMTP AUTH is disabled on the mailbox, or basic auth was turned off tenant-wide and the account now needs an app password or OAuth.
- The account is locked, or the sender address no longer matches the authenticated account.
- The config points at the wrong host, port, or starttls setting after an environment change.

Find the first failure before changing anything: how long mail has been down decides whether this is a quiet rotation or something that broke today, and which messages need resending.

## Done When

A test send from `common-service` authenticates and delivers, the cause is named rather than guessed, and whatever mail was dropped since the first failure is either resent or recorded as lost.
