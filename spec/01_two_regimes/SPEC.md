## Part I: The Two Regimes of AI-Assisted Development

### 1.1 Terminal-Goal Software

Some software problems are **externally constrained**. The specification is imposed by
the world rather than invented by the developer. A CLI tool that reverse-engineers an
encrypted API, a data pipeline that must conform to a third-party schema, a scraper that
must match what a CDN actually serves — these are *terminal-goal* problems. They have:

- A single correct order of operations
- A binary success criterion (it works or it doesn't)
- Immediate, tight feedback loops (the output is either valid or visibly broken)
- No meaningful architectural decisions beyond pipeline ordering

In this regime, AI-assisted development is extraordinarily effective because the AI is
performing *vocabulary-bridged composition*: assembling known solutions to known sub-problems
in a fixed sequence. The human's primary contribution is *intent* — knowing what the
pipeline needs to accomplish. The implementation detail is genuinely delegatable.

**In terminal-goal software, vibecoding is often appropriate.** The specification is
the world itself; the feedback loop is tight; the debt surface is bounded.

### 1.2 Open-Ended Creative Tooling

Other software problems are **internally generated**. Every feature, every data model,
every aesthetic decision emerges from the developer's evolving creative vision. A webtoon
editor, a game engine, a content creation workstation — these are *open-ended* problems.
They have:

- Features that generate architecture (each new use case adds structural commitments)
- Success criteria that are subjective, evolving, and only partially knowable in advance
- Feedback loops that are loose (a wrong architectural decision may not reveal itself for weeks)
- Meaningful architectural decisions at every layer

In this regime, AI-assisted development without a CLDS degrades rapidly. The AI implements
locally correct solutions to locally presented problems, without a global invariant to
check against. Each session's output is individually coherent; the aggregate accumulates
structural debt.

**In open-ended creative tooling, vibecoding without CLDS produces a system that works
until it doesn't, and then is very difficult to fix.**

### 1.3 The Asymmetry That Defines CLDS

The AI has:
- Unlimited working memory for syntax and API surface
- Comprehensive knowledge of implementation patterns
- Zero persistent memory for design intent
- No awareness of the *why* behind structural decisions

You have:
- Clear creative vision and domain understanding
- Finite working memory for implementation detail across large systems
- The ability to recognize correct vs. incorrect architectural reasoning
- The judgment to reject outputs that violate unstated invariants

**CLDS is the methodology for distributing cognitive labor across this asymmetry.**

You hold the intent. The AI holds the syntax. The specification artifacts hold the
bridge between them — encoded in forms that both parties can read, reason about,
and check against.

**The bottleneck has inverted.** In traditional software development, the constraint
was typing speed — human thinks fast, types slowly. In CLDS, the constraint is reading
speed — the AI writes hundreds of lines of code faster than you can read the documentation
it produces. Every workflow decision in CLDS is ultimately a decision about minimizing
your reading cost while maximizing the architectural authority you exercise. This inversion
is not incidental. It shapes every layer of the methodology.

---

