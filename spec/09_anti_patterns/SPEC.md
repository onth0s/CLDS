## Part IX: Anti-Patterns

### Anti-Pattern 1: The Perpetual Prototype

Symptom: the exploratory prototype is never refactored because it always *mostly works*,
and refactoring feels like losing progress.

Consequence: the system's architecture is permanently defined by the accumulated decisions
of AI sessions that had no architectural authority to check against. The system becomes
progressively harder to extend without breaking existing behavior.

Resolution: a PARTIALLY WORKING system with no specification is not progress — it is
potential energy for future regression. The Full Refactor is not loss; it is crystallization.

### Anti-Pattern 2: The Specification as Ceremony

Symptom: specification artifacts are written but never loaded into session context.
They exist to satisfy a process requirement rather than to guide the AI.

Consequence: specification and implementation drift silently. The specification becomes
stale documentation rather than living infrastructure.

Resolution: if the specification is not in the context window, it does not exist for
that session. Session opening protocol is non-optional.

### Anti-Pattern 3: The Unilateral AI Refactor

Symptom: the AI proposes and implements a structural change within a session without
explicitly flagging it as an architectural decision.

Consequence: the architectural model is silently invalidated. Future sessions inherit
an inaccurate structural model.

Resolution: instruct the AI explicitly at session opening — "architectural proposals
must be surfaced as proposals, not implementations. Describe the change and your
reasoning. Do not implement it until I ratify it."

### Anti-Pattern 4: The Over-Specified Prototype

Symptom: CLDS tooling is applied to exploratory phases before the domain is understood.

Consequence: the specification reflects premature assumptions that the exploratory
prototype would have corrected. The specification becomes a constraint on learning.

Resolution: exploratory phases are intentionally under-specified. CLDS tooling engages
fully at the Full Refactor. The discipline is distinguishing exploration from design.

### Anti-Pattern 5: The Invisible Debt

Symptom: WORKING BUT UNSPECIFIED features are carried into the refactored system
without specification.

Consequence: the refactored system inherits unknown constraints. Future refactors
encounter behavior that cannot be changed safely because no one knows whether it
is intentional.

Resolution: the feature inventory is non-optional. Every feature entering the
refactored system must be classified. WORKING BUT UNSPECIFIED features must be
specified before implementation.

### Anti-Pattern 6: The Specification Bureaucracy

Symptom: the full CLDS toolstack (C4 + YAML + Gherkin + DECISIONS.md + session
protocols) is applied uniformly regardless of project scale or complexity.

Consequence: specification maintenance cost competes with implementation effort.
The methodology becomes a burden rather than infrastructure.

Resolution: apply the Minimum Viable Specification principle. README-as-architecture
and YAML acceptance criteria are legitimate artifacts at appropriate scales. Gherkin
is not mandatory. C4 is not mandatory. The principles are mandatory; the formats are
not. Start at the floor and add overhead only when its absence creates felt pain.

### Anti-Pattern 7: The Silent Execution

Symptom: the AI is given a specification and immediately begins implementation without
a proposal-and-ratification cycle. The plan is implicit, not explicit.

Consequence: architectural assumptions embedded in the AI's interpretation of the spec
are never surfaced for review. The implementation may be technically correct against
the spec while violating unstated architectural intent.

Resolution: REP. Always. For any implementation that is sufficiently significant to
warrant a PLAN.md, the minimal-plan-then-ratify cycle is the non-negotiable first step.
The plan carries your ratification before execution begins.

### Anti-Pattern 8: The Unverified Plan

Symptom: a CA produces PLAN.md and then implements it. No step verifies that
the implementation actually covers what the plan declared. Coverage gaps —
untested scenarios, missing fixtures, undeclared deviations — go unnoticed
because both the plan and the implementation were produced by AI, and no
authority checked the gap between them.

Consequence: PLAN.md becomes retrospective documentation rather than an
executable contract. The gap between declared strategy and actual
implementation is invisible — until a scenario the plan specified, but the
implementation skipped, causes a regression.

Resolution: REP Step 6.5. After execution, a CA (preferably in a fresh
context) performs a plan-implementation alignment audit: given PLAN.md and
the implementation, report every scenario, fixture, or teardown requirement
the plan declared that the implementation does not cover. This is a deviation
report, not a quality review. The output is the coverage gap, stated plainly.

Note: this anti-pattern is frequently avoided *accidentally* by developers
who manually test against PLAN.md. Making the avoidance deliberate and
CA-delegated is the CLDS response — it costs nothing and catches exactly the
class of silent gaps that manual testing catches inconsistently.

### Anti-Pattern 9: The Asserted Ratification

Symptom: the AI asserts that a ratification gate has been passed — produces a minimal
plan, claims to have paused for ratification, reports that Step 6.5 was completed —
without any out-of-band human authorization having been issued. The AI's self-report
becomes the gate record. The human, trusting the protocol, proceeds without recognizing
that no structural verification occurred.

Consequence: the ratification gates of REP become advisory checkpoints that the AI
can procedurally satisfy through compliant-sounding language, while maintaining
continuous implementation authority. The enforcement gap (see Section 10.1) is not
merely present — it is actively exploited, even without intent, because the AI's
optimization toward task completion is stronger than the procedural expectation to pause.

This anti-pattern is particularly insidious in agentic contexts, where the human is not
monitoring every step and relies on the AI's state reporting to know where the protocol
stands.

Resolution: the Ratification Vault (Part X). Structural enforcement rather than
procedural expectation. The AI must produce a passing `rv validate` output — issued
by an external process it cannot control — before any execution gate opens. The
validator's output is the gate record, not the AI's self-report.

Note: this anti-pattern is not a failure of the human's discipline or the AI's honesty.
It is an architectural consequence of building a compliance protocol that lives entirely
within the AI's context. Any protocol that relies on the AI to self-report its own gate
compliance will be subject to this failure mode. The resolution is architectural,
not behavioral.

### Anti-Pattern 10: The Stale Audit

Symptom: `INSPECTOR.md` is written once against the system at a specific revision and
never updated. After subsequent refactors or feature additions, the audit procedure
still references commands, schema fields, and behavioral claims from the original version.
The audit runs; `DISSONANCES.md` is populated; findings are acted on.

Consequence: the findings are a mix of real conformance gaps and artifacts of specification
drift in the audit procedure itself. Findings that reference behavior the system no longer
promises are false positives — they generate remediation work for non-problems. Behavioral
claims the system now promises but `INSPECTOR.md` does not probe are false negatives —
they generate a false sense of conformance coverage. Over time, `DISSONANCES.md` loses
evidentiary authority as a ratification input because no one can distinguish genuine
findings from procedure staleness.

This failure mode is insidious because it does not announce itself. A stale
`INSPECTOR.md` produces output that looks like a legitimate audit. The noise is only
detectable by cross-referencing the procedure's behavioral claims against the current
specification — which is exactly the cross-reference that the audit procedure exists
to automate.

Resolution: treat `INSPECTOR.md` as a specification artifact with the same maintenance
discipline as `README.md` or YAML schemas. After every major refactor, update
`INSPECTOR.md` before running the audit. The update is not optional and is not an
afterthought — it is the precondition for the audit having any evidentiary value. Apply
Principle 12.

### Anti-Pattern 11: The Orphaned Schema

Symptom: a Specification Fragment's `SPEC.md` (Section 3.6) is edited — an invariant
clarified, a concept renamed, a field added — but the sibling schema file it authorizes
is not updated to match, and its spec-hash stamp is not refreshed. The schema continues
to parse and operate normally; nothing fails at runtime, so nothing draws attention to
the gap.

Consequence: the schema silently diverges from the prose that authorizes it. A future
reader — human or CA — trusts the schema as a faithful serialization of its `SPEC.md`,
per Section 3.6.1, when it no longer is one. This is the structural inverse of
Anti-Pattern 10: where the Stale Audit is an audit procedure that fails to track a
specification that moved, the Orphaned Schema is an implementation artifact that fails
to track a specification that moved. Same disease — an artifact decoupled from the
ground truth that authorizes it — in a different organ.

Resolution: run the spec-hash validator (Section 3.6.2) as part of every
`full_spec_builder.py` invocation or pre-commit hook. A mismatch between a fragment's
current hash and its schema's stamped hash is a hard failure, surfaced before the
schema is treated as current — never a warning to be triaged later. Apply Principle 14.

### Anti-Pattern 12: The Unswept Seam

Symptom: every module's Tier 1 Local audit (Section 3.7) reports clean — no open
findings in any local `DISSONANCES.md` — and this is treated as sufficient evidence
that the system as a whole is coherent. No Tier 2 Global audit is run, or it is run
on a cadence that quietly lengthens whenever Tier 1 stays clean.

Consequence: a defect that exists specifically in the interaction between two or more
locally-compliant modules goes undetected indefinitely. Logic duplicated independently
across two directories that never reference each other, a global invariant violated
only by the combination of two individually-correct local behaviors, a function that
is dead specifically because nothing *outside* its own module calls it anymore — none
of these will ever appear in a Local audit, because none of them are visible from a
local vantage point by construction. Every individual Tier 1 finding is, in this
scenario, telling the truth. Their aggregate is not equivalent to system-wide coherence,
and treating it as such is the error.

Resolution: Tier 1 cleanliness is a precondition for a productive Tier 2 audit, not a
substitute for one. Schedule Global audits on a cadence independent of Tier 1 results
— a clean Tier 1 sweep never extends the interval before the next Tier 2 audit is due.
Apply Principle 14.

### Anti-Pattern 13: The Generic Artifact Name

Symptom: a core methodology or specification document is given a generic, common
filename — `SPECIFICATION.md`, or a `README.md` pressed into service as if it were
the project's constitution, or `DESIGN.md` — that collides with the vast quantity of
unrelated content bearing the same name across the AI's training distribution and
across any number of unrelated codebases' own conventions.

Consequence: an AI operating across sessions, or reasoning about the artifact from a
reference rather than the loaded file itself, is more likely to hallucinate its
contents — filling gaps with generic, statistically-typical "specification document"
boilerplate drawn from training data, rather than surfacing uncertainty or requesting
the actual file. The filename itself, being common, hands the model a strong but
false prior that it already "knows" what the file contains, precisely because a
string like `SPECIFICATION.md` is heavily represented in training corpora attached to
thousands of unrelated projects. A distinctive filename cannot be filled in from a
generic prior; a common one invites exactly that.

Resolution: name load-bearing methodology artifacts using a **long-chain keyword** —
a distinctive, low-collision, multi-token acronym or coined term — rather than a
generic descriptive noun, so the filename itself functions as an anchor that forces
attention to the actual loaded content instead of inviting confident confabulation
from a generic prior. This is the rationale for this document's own name: the
manifesto for the Cognitive Load Distribution System is named `CLDS.md`, not
`SPECIFICATION.md`, specifically to defend against this failure mode. This is a rare
case of a resolution being self-referential — the document names itself in accordance
with the very anti-pattern it defines, to prevent hallucination about itself.

### Anti-Pattern 14: Assertion-Gated Success

Symptom: a terminal status label — "Closed," "Resolved," "Passed," "Dead-end
detected," "Complete" — is applied to an artifact, a disposition, or a validator's
output on the strength of a *plan* to satisfy the underlying condition, rather than
independent verification that the condition actually holds. The label is frequently
emitted by the same process — human or AI — that has an incentive toward the outcome
the label asserts.

Consequence: the success signal detaches from the thing it is supposed to signal.
Two of its most damaging instances: **(1)** an audit or validator emits a positive
or terminal signal for a check it is structurally incapable of performing — a
dead-end detector that traverses a graph in the wrong direction still prints "dead-end
detected" on violations it cannot actually see — meaning its silence and its correct
output are indistinguishable from its failure mode; and **(2)** a tracking artifact
marks an item's disposition as terminal the instant an amendment is *drafted*, before
the amendment has actually been applied to the live artifact it amends — collapsing
"a fix has been proposed" into "the fix has been verified to exist." In both cases,
everything downstream that trusts the label — a later audit, a future session, a
collaborator — inherits a false belief at zero apparent cost, which is the most
dangerous kind of debt, because nothing about consulting the label reveals that it is
unearned.

This is the general form of Anti-Pattern 9 (The Asserted Ratification), which names
the specific instance of this failure at REP's ratification gates. Assertion-Gated
Success is the same failure shape wherever a terminal claim of correctness,
completion, or detection is emitted without the coverage to back it — audits,
validators, disposition tables, and status trackers are all susceptible, not only
ratification gates.

Resolution: apply Principle 11 (Enforcement Over Assertion) beyond ratification gates
specifically. A terminal status label should be backed by either (a) independent,
structural verification — the RV pattern — or (b) an explicit, checkable statement of
what was actually confirmed versus merely proposed: "amendment drafted, not yet
applied" is an honest label; "Closed" is not, until the artifact it amends has
actually been changed and that change verified. For validators and audit procedures
specifically, a positive or terminal output should be paired with a stated test of the
check's own capacity to fail — a check that cannot be observed to produce a negative
result under any real input is not verified to be checking anything.

---

