# CLAUDE.md — CDR (Canadian Digital Railway)

<!-- response-contract v2 -->
## Response Contract — hard rule, overrides all other formatting guidance

Reasoning is internal. Report conclusions, never the path to them.

Default shape for every reply:

**TL;DR** — one line, <=25 words.
**Next** — the single command, file, or decision Fred acts on. One item only.
**Notes** — max 3 bullets, <=15 words each. Blockers, risks, surprises only.

Hard caps:
- <=120 words total outside code and diffs.
- One topic per reply. Found something else? Hold it. Do not append it.
- No preamble, no restating the question, no closing summary, no "worth noting".
- No unrequested code blocks. Show the diff, not the file.

Overrides:
- "expand" or "why" → caps off, that reply only.
- "brief me" → 5 bullets max.

## Project State

Read `SESSION_LOG.md` at the repo root first — it is the single source of truth for current CDR state. Enterprise-wide rules live in `CLAUDE.md` in `hazeydata/operations`.
