# Sending Output Between Claude Code Sessions

A session's context is its own. Two sessions open on two project folders share nothing — not conversation history, not memory, not the files outside their own directory. So a result produced in one and needed in the other has to be carried across deliberately, and the choice of method is really a choice about how long the result needs to survive.

## Message the Session Directly

`ListAgents` returns the roster of local sessions, across project directories, and the name in each row is the address:

```text
SendMessage({to: "kb-d7", message: "..."})
```

The text lands in that session's context while its own project state stays intact — no file, no copy-paste, and nothing left behind afterwards. That makes it the right tool for a finding, a summary, or a decision, and the wrong one for anything that has to outlive the session.

Four things shape how it behaves:

The receiving session reads the message literally. An `@path` in it attaches nothing on the other side, because the path is resolved against a working directory the sender does not have. Send the content, not a reference to it. This is the one that actually bites.

Messages queue and drain at the receiver's next tool round, so a session sitting idle at its user's prompt has not read it yet.

A session running under a stricter permission mode may hold the message for its own user's approval rather than acting on it.

The roster is live rather than historical. A session that has exited stops appearing, so the name has to be read at send time instead of remembered from earlier — a session can message this one and already be gone from `ListAgents` by the time the reply would go back.

## A Shared File Outside Both Projects

```text
~/handoff/<topic>.md
```

Project one writes it, project two reads it by absolute path. Only `@`-completion is confined to the working directory; an absolute path reads fine from anywhere. This is the durable option, and the one to reach for when the result should still be there tomorrow or when more than two sessions need it.

## Add the Other Directory

```bash
claude --add-dir ~/Projects/proj1
```

Run from inside project two, when the "result" is actual code or config that lives in project one rather than prose about it. Better than copying, because a copy starts going stale the moment it is made.

## Headless Piping

```bash
(cd proj1 && claude -p "...") > ~/handoff/out.md
```

Then feed that file's contents into a `claude -p` run in project two. The scripted version of the shared file, for when neither end is a session someone is sitting in front of.

## What Does Not Cross

Two things are worth knowing are impossible rather than discovering by trying.

`--resume` and `--continue` are keyed by directory, so neither reaches a session started elsewhere.

Memory is per project, at `~/.claude/projects/<slug>/memory/`, where the slug is the working directory with its slashes turned into dashes. A subfolder gets its own slug and therefore its own memory — a session opened in `w/aichatbot/aichatbot-cms-service` does not see what was written from `w/aichatbot`. For a fact that should hold in every project, the global file is `~/.claude/CLAUDE.md`.
