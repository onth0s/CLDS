# CLDS.md
## A Manifesto for Cognitive Load Distribution in AI-Assisted Software Development

*Last revised: 2026-07-26T00:00:00Z — Version 1.6*

> *This document was renamed from `SPECIFICATION.md` to `CLDS.md` at Version 1.6.
> The rationale is not cosmetic — it is a prescriptive failure-mode entry in its
> own right. See Anti-Pattern 13 (The Generic Artifact Name).*

> *"The specification artifacts are the shared memory between two cognitive profiles.
> They encode your intent in a form the AI can check against, and they encode the AI's
> implementation decisions in a form you can audit without reading every line of code."*

---

## Preamble

This document is a living methodology manifesto. It exists because a specific and repeatable
problem has emerged at the intersection of human creative vision and AI-assisted implementation:
the gap between *what you intend to build* and *what the AI produces* grows non-linearly as
project scope expands, and no existing methodology in the software engineering canon was
designed with this particular cognitive partnership in mind.

TDD, BDD, DDD, C4 — these are all frameworks built for human-to-human engineering teams,
optimized for correctness, maintainability, and architectural coherence. They are genuinely
useful, and this methodology borrows from all of them. But they share a foundational assumption
this methodology does not: that the entities collaborating on a system share persistent memory,
accumulated context, and evolving mutual understanding over time.

The AI does not. Every session begins from zero. Every context window is finite. Every
handoff between sessions is a lossy compression of everything that came before.

This manifesto describes a methodology — called **Cognitive Load Distribution System (CLDS)**
— designed specifically for that reality. Its central thesis is simple:

**The specification artifacts are not documentation. They are infrastructure.**

They are the mechanism by which your architectural authority, design intent, and accumulated
domain understanding survive the context boundary. Without them, every AI session begins
not where the last one ended, but at a shallow reconstruction of it. With them, the AI
operates as a capable, well-briefed collaborator rather than an amnesiac contractor who
has to be re-onboarded every morning.

**A note on scope and era-contingency.** CLDS is not a permanent methodology claiming
timeless validity. It is the currently optimal response to a specific technological
constraint: AI systems that possess high implementation capability but no persistent
design memory. As that constraint relaxes — as AI systems develop longer-term project
awareness — the specific artifact prescriptions of CLDS will change. The underlying
principles (intent should be explicit, architectural authority should be preserved,
deviations should be surfaced) may survive in some form. The methodology should be
read with this contingency in mind.

**A note on domain.** Although CLDS was discovered in a software development context,
its actual subject is not software. It is the problem of *how intent survives across
cognition boundaries* — wherever one actor holds vision and another holds execution
capability, and shared artifacts must preserve the bridge between them. Software is
the first environment in which the pattern became acute enough to force a systematic
response. It will not be the last.

---

