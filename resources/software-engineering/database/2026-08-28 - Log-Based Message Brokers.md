---
type: distilled-note
---

# Log-Based Message Brokers

A widely used way to deliver a stream is to send messages via a **message broker** (also known as a message queue), which is essentially a kind of database optimized for handling message streams.

Two delivery patterns sit on top of it, and they answer different needs:

- **Load balancing** — each message goes to one of the consumers, so the work is shared out and throughput scales with consumers.
- **Fan-out** — each message goes to all of the consumers, so independent systems each see the whole stream.

**Using logs for message storage.** Producers send messages by appending them to a topic-partition file, and consumers read these files sequentially. The append-only log is what lets a message be read more than once and read from a chosen position, rather than being consumed and destroyed.
