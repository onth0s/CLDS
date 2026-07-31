## Part VIII: Principles

These are the foundational principles of CLDS. They are listed in order of priority;
when principles conflict, earlier ones take precedence.

### Principle 1: The Specification Is Infrastructure

Specification artifacts are not documentation written after the fact. They are
load-bearing infrastructure that makes the AI's implementation checkable and your
architectural authority persistent. Treat their maintenance with the same seriousness
as the codebase itself.

### Principle 2: Intent Flows Downward

Design intent flows from specification into implementation, never the reverse. When
implementation and specification conflict, the conflict is resolved at the specification
level first, then propagated into code. Code that silently redefines the specification
is the primary vector of architectural drift.

### Principle 3: The AI Proposes; You Ratify

The AI is the implementation engine. You are the architectural authority. The AI may
propose amendments to the specification — this is valuable and expected. You ratify
or reject them. Once ratified, the AI implements to the spec. Settled decisions are
not re-opened without surfacing the re-opening explicitly.

### Principle 4: Deviation Must Be Explicit

When the AI deviates from specification — for any reason, including good ones — the
deviation must be stated, reasoned, and decided upon. Silent deviation, even when
locally correct, is invisible debt because it breaks the invariant that the
specification describes what the code does.

### Principle 5: The Exploratory Prototype Is Input, Not Output

The exploratory prototype is an epistemic instrument for learning the domain. Its
output is not a deliverable system; it is a specification. Mine it for domain
understanding, inventory its working features, and then design the system that should
exist given everything it taught you.

### Principle 6: Invariants Are Non-Negotiable

Invariants, once declared and marked, are non-negotiable behavioral contracts. Any
refactor that breaks a marked invariant is wrong by definition. If an invariant needs
to change, that change is a deliberate architectural decision — ratified, logged, and
propagated — not a side effect of an unrelated refactor.

### Principle 7: Specification Debt Is Worse Than Code Debt

Code debt is expensive. Specification debt is more expensive, because it hides code
debt. An undocumented architectural decision cannot be evaluated; it can only be lived
with or accidentally overwritten. A missing invariant will eventually be violated by an
AI that had no way to know it existed. Specification debt compounds invisibly.

### Principle 8: The Feedback Loop Determines the Methodology

In terminal-goal software with tight, binary feedback loops, CLDS overhead is
disproportionate to the benefit. Vibecoding with aggressive iteration is appropriate.
In open-ended creative tooling with loose, subjective feedback loops, CLDS overhead
is the minimum viable investment in architectural integrity. Know which regime you
are in.

### Principle 9: Architecture Is Negotiable; Architectural Authority Is Not

Not all structural decisions carry equal weight. File naming, utility organization,
and component decomposition within an already-defined container are **implementation
decisions** — delegatable to the AI within the bounds of established invariants. State
management patterns, data model shape, and API boundary design are **architectural
invariants** — requiring explicit human ratification before implementation.

CLDS does not require you to ratify every line of code. It requires you to maintain
clear authority over the decisions that define the system's structure. Delegate
implementation decisions freely. Ratify architectural ones always.

### Principle 10: Minimum Viable Specification

More specification is not always better. Beyond a threshold, specification maintenance
competes with implementation effort. An outdated invariant is worse than a missing one.
A stale YAML file describing behavior that no longer exists creates false confidence.

The minimum viable specification surface for a solo developer on a single-container
application: one architectural model (README or C4) + one domain schema + explicit
invariants + a DECISIONS.md. Everything above this floor is additive and should be
adopted based on felt need, not methodology prescription.

Treat the specification surface itself as a design problem: the right amount for your
project at your scale, no more.

### Principle 11: Enforcement Over Assertion

A protocol that relies on the AI to self-report its own compliance will receive the
appearance of compliance, not the substance. Any gate that the AI can pass by asserting
it has passed is not a gate — it is a suggestion formatted as a checkpoint.

Where compliance matters enough to be specified, it matters enough to be structurally
enforced. Procedural compliance (the AI says it followed the protocol) and structural
compliance (the protocol was demonstrably followed, with human authorization at every
required gate) are not equivalent. Design for structural compliance. Accept procedural
compliance only in contexts where the cost of structural enforcement exceeds the cost
of the failure mode it prevents.

This principle applies most forcefully to ratification gates. The value of a ratification
gate is that it is non-bypassable. A bypassable ratification gate is not a weaker version
of enforcement — it is an absence of enforcement with compliance theater added.

### Principle 12: Audit Artifacts Must Track the Specification

An audit procedure (`INSPECTOR.md` or equivalent) that references behavioral expectations
from a superseded version of the system does not produce findings — it produces noise.
False positives (behaviors the spec no longer promises) and false negatives (behaviors
the spec now promises but the audit does not probe) are equally damaging: they undermine
the audit layer's evidentiary authority, eventually rendering `DISSONANCES.md` unreliable
as a ratification input.

The maintenance invariant: `INSPECTOR.md` is updated after every major refactor or
significant feature addition, before the next audit cycle runs. The audit procedure and
the specification it tests are not independent artifacts that can drift from each other
— they are coupled. Their coupling is the source of the audit layer's value.

This principle is a special case of Principle 2 (Intent Flows Downward): the specification
defines the intended behavior; the audit procedure's behavioral claims flow from the
specification; when the specification changes, the audit procedure changes first.

### Principle 13: Cost-Ordered Verification

Any verification mechanism that has both a cheap, deterministic tier and an expensive,
probabilistic tier should run the cheap tier unconditionally, and gate the expensive
tier behind explicit invocation, reduced frequency, or both. The two tiers are not
interchangeable substitutes for each other — the cheap tier exists to catch what it
can catch reliably and often; the expensive tier exists to catch what the cheap tier
structurally cannot, and is invoked only as often as its cost permits.

This pattern recurs wherever CLDS tooling performs automated checking: the mandatory
Tier 1 glossary collision check versus the optional Tier 2 proliferation report
(Section 3.6.3); Local versus Global audits (Section 3.7); a matching pipeline that
exhausts exact and normalized comparison before escalating to fuzzy, phonetic, or
semantic methods. None of these are coincidences. A system that runs its expensive
tier unconditionally will be too costly to use at the frequency that makes it useful.
A system that runs only its cheap tier will silently miss the class of defect only
the expensive tier can see. Designing the gate between them — what triggers escalation,
and at what frequency the expensive tier runs regardless — is itself a first-class
design decision, not an afterthought to be resolved ad hoc each time the pattern recurs.

### Principle 14: Audit Scope Must Match Invariant Scope

An invariant's scope determines the minimum audit scope capable of verifying it. A
**local invariant** — true within the boundary of a single module, independent of any
other module's state — can be fully verified by a Local audit (Section 3.7) scoped to
that module alone. A **global invariant** — true only as a property of the interaction
between two or more modules — cannot be verified by any number of Local audits, no
matter how many pass; verifying it requires an audit whose scope spans the modules the
invariant actually depends on.

Conflating these two scopes — treating a clean sweep of Local audits as sufficient
evidence that a global invariant holds — is not a methodological shortcut. It is a
category error, and it is the specific failure mode Anti-Pattern 12 names. This
principle is a direct companion to Principle 12 (Audit Artifacts Must Track the
Specification): Principle 12 ensures an audit's *content* stays current; Principle 14
ensures an audit's *scope* is sufficient for the invariant it claims to verify. An
audit that is current but under-scoped is still capable of producing false confidence.

### Principle 15: The Handler Pattern — Shape Belongs to the Handler, Content Belongs to the Agent

Wherever an AI's output decomposes into a mechanical, schema-determined **shape** and
a judgment-determined **content**, the shape should be produced by a deterministic
handler function the AI *calls*, with the content as typed arguments — never
hand-authored token-by-token by the AI itself. The dividing line: if the correct
output is a pure function of known inputs — required-field scaffolding, default-value
structures, naming and namespacing conventions, boilerplate wiring — it belongs in a
handler, because a handler makes the invalid state unrepresentable rather than merely
catchable after the fact. If correctness instead depends on a plausible reading of a
domain-specific judgment call — inferred values, narrative content, magnitudes tied to
specific evidence — it stays with the AI, and the handler should be the thing the AI
calls *after* deciding the values, not a way of avoiding the decision.

This generalizes the Enforcement Gap (Section 10.1) one layer down: it separates the
class of AI output where enforcement-by-construction is achievable at negligible cost
from the class where it is not achievable at all, because the "correct" output is
inherently a matter of interpretation rather than derivation. Applying the Handler
Pattern to the first class can retire entire categories of downstream audit check that
exist only to catch handler-shaped mistakes — a required field silently omitted, a
naming convention silently violated — because a well-typed handler cannot produce
that mistake, by construction.

**The bypass-prevention caveat, without which this principle does not hold.** A
Handler Pattern delivers a *structural* enforcement gain only if calling the handler
is non-optional. If the AI can still hand-author the shape directly, through an
ordinary write path to the same artifact, the handler is a convenience, not a
guarantee — and any downstream audit checks retired on the strength of "the handler
cannot produce this mistake" have been retired on a false premise. The handler removes
the mistake only from the AI's cooperative path; it does nothing to a bypass path that
remains open. Do not retire an audit check on the strength of a Handler Pattern's
existence unless the bypass itself is also independently prevented — by removing the
AI's ordinary write access to the artifact the handler produces, by a pre-commit or
pre-wipe gate that rejects diffs to that artifact not tagged as handler-originated, or
an equivalent structural block. Until that bypass-prevention exists, the Handler
Pattern remains a strong procedural convention — worth adopting regardless, for its
token-economy and default-correctness benefits — but it is, in the vocabulary of
Principle 11, a *procedural* compliance gain, not yet a *structural* one, and the audit
checks it appears to obsolete should be treated as still load-bearing.

---

