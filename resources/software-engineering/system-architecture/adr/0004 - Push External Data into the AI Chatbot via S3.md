# Push external data into the AI Chatbot via S3

System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Status

Accepted, captured 2026-10-02.

## Context

- An external system has to push data into the AI Chatbot.
- Three ways to do it were on the table.
- The data volume is large.

## Options Considered

- **Stage through S3 and load from there** (chosen).
- **Via the AI Chatbot's API** (rejected). Too much data to push through API calls.
- **Insert directly into the AI Chatbot's database** (rejected). Would mean giving the external system a connection to our database, which we don't want.

## Decision

The external system drops data in S3, and the AI Chatbot loads it from there. S3 carries the volume the API can't, without opening a DB connection to an outside system.

## Consequences

*Open — not recorded.*

## Compliance

*Open — not recorded.*

## Notes

- Captured 2026-10-02 as a three-line inbox note: "via system api / via db: insert directly or via s3".
