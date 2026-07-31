## Appendix A: Quick Reference

### Dominant Modes
- **Exploration Mode** — emergent spec, fast iteration, debt consciously accepted
- **Design Mode** — authoritative spec, disciplined iteration, debt actively managed

### The Seven Phases
1. **CRYSTALLIZATION** — Domain vocabulary, core use case hypothesis
2. **SHELL** — Minimal skeleton, basic data flow
3. **UI PROTOTYPE** — Interface without functionality
4. **MINIMAL FUNCTIONALITY TEST** — Just enough to test the actual use case
5. **EXPLORATORY ITERATION** — Iterate until inflection point
6. **FULL REFACTOR** — Mode transition; specification-first; working features only
7. **DISCIPLINED EVOLUTION** — Every feature through the specification loop

### The CLDS Stack
```
CLDS   — Distributed cognition framework (philosophy + principles)
  └── REP    — Ratified execution protocol (operational turn sequence)
        └── RV     — Ratification vault (programmatic enforcement substrate)
```

### The CLDS Toolstack
- **Architectural Model** — Structural authority and rejection filter (README or C4)
- **YAML Specification Files** — Contract surface, constitutional document
- **Behavioral Contracts** — Observable oracle, regression anchor (YAML or Gherkin)
- **DECISIONS.md** — Unresolved decision log, cross-session memory
- **Audit Layer** — `INSPECTOR.md` (reproducible audit procedure) + `DISSONANCES.md`
  (structured findings artifact); must be updated after every major refactor
- **Fragmented Specification Architecture** — Specification Fragments (`SPEC.md` per
  module) as the canonical, hand-edited source; `full_spec_builder.py` assembles the
  monolithic specification document and stamps sibling schemas with spec-hashes.
  Governs how *projects adopting CLDS* organize their own domain specs — whether and
  how it applies reflexively to CLDS.md's own document is an open question (3.6.4)
- **Audit Scope Tiering** — Tier 1 (Local/Module, frequent) and Tier 2
  (Global/Cross-Cutting, infrequent) audits operating against the Audit Layer; the
  tiers are complementary, not substitutable

### The Specification Loop
1. Domain crystallization
2. Architectural placement
3. YAML specification
4. Behavioral contracts
5. AI-assisted implementation (via REP)
6. Specification reconciliation
7. Architectural model update

### The Ratified Execution Protocol (REP)
1. Minimal plan request (proposal-only mode)
2. Ratification with architectural annotations
3. Full plan elaboration (write mode)
4. Final approval
5. Phased execution
6. Local behavioral annotation per phase
6.5. Plan-implementation alignment audit
7. Final iron-out

### The Inflection Point Signals
- A bug fix breaks something semantically unrelated
- A new feature requires modifying more than three existing files
- You cannot explain data flow without consulting the code
- The AI generates solutions conflicting with earlier session decisions
- The README no longer describes what the system actually does

### The Fifteen Principles
1. The specification is infrastructure
2. Intent flows downward
3. The AI proposes; you ratify
4. Deviation must be explicit
5. The exploratory prototype is input, not output
6. Invariants are non-negotiable
7. Specification debt is worse than code debt
8. The feedback loop determines the methodology
9. Architecture is negotiable; architectural authority is not
10. Minimum viable specification
11. Enforcement over assertion
12. Audit artifacts must track the specification
13. Cost-ordered verification
14. Audit scope must match invariant scope
15. The Handler Pattern — shape belongs to the handler, content belongs to the agent

---

## Appendix B: Minimum Viable Specification by Scale

| Scale | Architectural Model | Contract Surface | Behavioral Contracts |
|-------|--------------------|--------------------|----------------------|
| Solo, single container, moderate complexity | README-as-architecture | YAML schema file | Inline acceptance criteria |
| Solo, single container, high complexity | README + C4 Component diagram | YAML per domain entity | YAML + Gherkin for complex flows |
| Small team, multi-container | Full C4 (Context + Container + Component) | YAML per domain entity | Gherkin for all user-facing features |

Apply the floor for your scale. Add overhead only when its absence creates felt pain.

---

## Appendix C: Glossary

**CLDS (Cognitive Load Distribution System)** — The methodology described in this
document. The practice of distributing cognitive labor across the asymmetry between
human design intent and AI implementation capability through structured specification
artifacts.

**REP (Ratified Execution Protocol)** — The operational turn sequence by which a
ratified specification becomes working code. Seven steps from minimal plan proposal
through final iron-out, calibrated to minimize human reading cost while maximizing
architectural authority exercised.

**Terminal-Goal Software** — Software whose specification is externally imposed by
a fixed protocol, format, or third-party system. Tight feedback loops, binary success
criteria, bounded debt surface. Vibecoding is often appropriate.

**Open-Ended Creative Tooling** — Software whose specification is generated by the
developer's evolving creative vision. Loose feedback loops, subjective success criteria,
unbounded debt surface without CLDS.

**Exploration Mode** — Dominant mode in which specification is emergent, iteration is
fast, and debt is consciously accepted as the price of domain learning.

**Design Mode** — Dominant mode in which specification is authoritative, iteration is
disciplined, and debt is actively managed.

**Rejection Filter** — The function the architectural model serves: an externalized
structural description against which proposed changes can be evaluated without
reconstructing full architectural context from code.

**Invariant** — A behavioral property that must remain true across all future refactors.
Explicitly marked in specification. The non-negotiable contract between specification
and implementation.

**Invariant Graduation** — The process by which a candidate behavioral property earns
invariant status through one or more of: repeated survival, domain necessity, user
validation, or architectural derivation.

**Drift** — A change that moves away from specification without awareness. Harmful
because invisible; the primary mechanism of architectural decay.

**Evolution** — A change that moves toward a better understanding of the domain, made
with awareness, surfaced, ratified, and logged. Healthy; the mechanism by which
specifications improve through contact with reality.

**Specification Reconciliation** — The process of resolving mismatches between
specification and implementation at the specification level first. The mechanism
preventing code behavior from silently redefining specification intent.

**Feature Inventory** — Classification of all features in an exploratory prototype
before Full Refactor: VERIFIED WORKING, WORKING BUT UNSPECIFIED, PARTIALLY WORKING,
BROKEN, SCOPE CREEP, or DUPLICATE.

**Context Reconstruction Debt** — The cost paid at the start of every AI session to
re-establish what the previous session already knew, in the absence of a session
closing protocol.

**Vocabulary-Bridged Composition** — The mode in which AI-assisted development is
most effective: assembling known solutions to known sub-problems in a fixed sequence,
where the human contributes intent and the AI contributes implementation fluency.

**Constitutional Document** — The function YAML specification files serve: the
authoritative record of what the system is supposed to do, which the AI checks against
and proposes amendments to, but which only the human ratifies.

**Minimum Viable Specification** — The smallest artifact set that preserves core CLDS
properties without inducing maintenance overhead that competes with development effort.
Floor: one architectural model + one domain schema + explicit invariants + DECISIONS.md.

**Plan-Implementation Alignment Audit** — REP Step 6.5. A targeted CA review
— preferably in a fresh context — that compares PLAN.md against the
implementation and reports only coverage gaps and deviations. Distinguished
from behavioral annotation (Step 6), which checks implementation against
observable behavior, and from the final iron-out (Step 7), which checks
implementation hygiene. The alignment audit's authority is the plan itself,
treated as a behavioral contract: every scenario, fixture, and teardown the
plan declared must be accounted for in the implementation or explicitly
deferred.

**Ratification Surface** — The minimal plan produced in REP Step 1. Not a draft of
the full plan but the skeleton against which architectural annotations are made before
any implementation begins.

**Ratification Vault (RV)** — The programmatic enforcement substrate for CLDS and REP.
A file-based state machine and external validator that makes ratification gates
structurally non-bypassable by the AI. Occupies the enforcement layer beneath REP:
CLDS (framework) → REP (protocol) → RV (enforcement substrate). The AI must produce
a passing `rv validate` output — from an external process it cannot control — before
any execution gate opens. See Part X.

**Enforcement Gap** — The distance between procedural compliance (the AI says it
followed the protocol) and structural compliance (the protocol was demonstrably
followed, with human authorization at every required gate). The enforcement gap
exists in any protocol that relies on the AI to self-report its own gate compliance.
The Ratification Vault exists to close it.

**Structural Compliance** — The condition in which a protocol's gates are enforced by
external mechanisms that the AI cannot self-report its way past. Contrasted with
procedural compliance, in which the AI follows the protocol because it was instructed
to. Structural compliance is the target property for ratification gates; procedural
compliance is acceptable only where the cost of structural enforcement exceeds the
cost of the failure mode it prevents.

**Procedural Compliance** — The condition in which an AI follows a protocol because
it was instructed to, without any external enforcement verifying that each gate was
actually passed. Procedurally compliant output looks correct; structurally compliant
output is correct by construction. See also: Enforcement Gap.

**Ratification Gate** — A defined point in the REP protocol sequence at which the AI
must pause, produce a human-reviewable artifact, and obtain explicit authorization
before proceeding. In REP without RV, ratification gates are procedural expectations.
In REP + RV, ratification gates are structural enforcement points: no execution proceeds
until the validator confirms the gate was passed with human authorization.

**Apodictically-Enforced Constraint** — A constraint that is necessarily binding by
construction, not merely contingently expected. In CLDS, the goal of RV is to make
ratification gates apodictically enforced: the AI cannot advance past them, not merely
should not. The term distinguishes structural enforcement (apodictic) from procedural
expectation (contingent).

**Audit Layer** — The category of CLDS artifacts that measure specification conformance
in a running system: `INSPECTOR.md` (the reproducible audit procedure) and
`DISSONANCES.md` (the structured findings artifact). Distinct from the specification
layer (which defines what the system should do) and the behavioral contract layer
(which defines testable acceptance criteria). The audit layer's role in the CLDS cycle
is evidentiary: it produces human-readable findings for ratification, not automated
pass/fail signals.

**INSPECTOR.md** — A reproducible procedure for exercising a running system as a black
box, capturing its observable behavior against the specification, and writing findings
to `DISSONANCES.md`. Constrained to produce evidence without interpretation: no source
code reads, no code modifications, all inputs reproducible, all outputs verbatim-quoted.
Must be updated after every major refactor or significant feature addition. See Section
3.5 and Principle 12.

**DISSONANCES.md** — The structured findings artifact produced by following
`INSPECTOR.md`. Fixed, numbered section schema (§1–§N); findings are grep-addressable
and session-boundary-safe. Distinguishes observed findings from inferred ones. The
evidentiary substrate that feeds the implementation ratification cycle. Sections are
marked resolved, not deleted; the finding history is itself evidence.

**Compliance Signal** — A minimal, cheap-to-verify, discrete observable signal whose
presence confirms that a behavioral contract or procedural requirement was met, and
whose absence confirms it was not. Compliance Signals work because their verification
cost is asymmetric with their diagnostic value. In the Audit Layer, Phase H
self-verification steps in `INSPECTOR.md` are procedural Compliance Signals. In
agentic behavioral contracts (`AGENTS.md`), a designated acknowledgment response (such
as a specific phrase or marker) is a file-backed Compliance Signal. The Ratification
Vault's `rv validate` output is the apodictic instantiation. All three are the same
structural idea at different enforcement strengths: a cheap, observable probe that
forces a discrete and detectable compliance event.

**Specification-Conformance Auditing** — The practice of using a reproducible procedure
to measure the gap between a running system's observed behavior and its specification
promises. Distinguished from automated testing (which checks pass/fail conditions
programmatically) by its black-box, human-readable, evidentiary character. The output
is a findings document for human ratification, not a test report for CI. See Section 3.5.

**Specification Fragment** — A `SPEC.md` file scoped to a single domain entity or
module, co-located with the schema(s) it authorizes. The canonical, hand-edited source
of its section's prose; the monolithic specification document is generated from the
full set of fragments, never the reverse. See Section 3.6.

**`full_spec_builder.py`** — The build tool that walks the Specification Fragment tree,
assembles fragments into the monolithic specification document in directory order,
performs Tier 1 glossary collision detection unconditionally and Tier 2 term
proliferation detection on explicit invocation, and stamps sibling schema files with
spec-hashes. Deterministic and idempotent: an unchanged fragment tree produces a
byte-identical monolith on every run. See Section 3.6.1.

**Spec-Hash** — A content hash of a Specification Fragment, stamped as a header comment
in its sibling schema file(s) by `full_spec_builder.py`. A mismatch between a
fragment's current hash and a schema's stamped hash is a hard, build-blocking signal
that the two have drifted apart, in either direction. The mechanical instantiation of
Principle 14 at the fragment/schema boundary. See Section 3.6.2 and Anti-Pattern 11.

**Glossary Collision** — Two Specification Fragments defining the same term, modulo
case/whitespace normalization, with materially different meanings. Unambiguous and
unconditionally build-blocking; resolved by `full_spec_builder.py`'s mandatory Tier 1
check. Distinguished from Term Proliferation, which is a soft, optional, non-blocking
signal. See Section 3.6.3.

**Term Proliferation** — Two distinct, individually well-defined terms across
Specification Fragments that quietly refer to the same underlying concept, surfaced
through an optional fuzzy, phonetic, or semantic check rather than exact collision.
Never auto-resolved; flagged for human disposition under a fixed taxonomy (MERGE /
USE-FOR / RELATED / DISTINCT) adapted from controlled-vocabulary practice. Auto-merging
a flagged pair without human disposition is a glossary-layer instance of Anti-Pattern 9
(The Asserted Ratification). See Section 3.6.3.

**Audit Scope Tiering** — The practice of running Specification-Conformance Audits
(Section 3.5) at two distinct scopes: Tier 1 (Local/Module — cheap, frequent, bounded
to one Specification Fragment and its code directory) and Tier 2 (Global/Cross-Cutting
— expensive, infrequent, scoped to the whole system). The tiers are complementary, not
substitutable; a clean Tier 1 sweep is not evidence of Tier 2 coherence. See Section
3.7, Principle 14, and Anti-Pattern 12.

**Cost-Ordered Verification** — The design pattern of running the cheapest,
deterministic tier of a verification mechanism unconditionally, and gating any
expensive, probabilistic tier behind explicit invocation, reduced frequency, or both.
Instantiated by Audit Scope Tiering, by the Glossary Collision / Term Proliferation
split, and by cost-ordered matching pipelines generally. See Principle 13.

**Handler Pattern** — The practice of routing mechanical, schema-determined *shape*
through a deterministic handler function called with typed arguments, rather than
having the AI hand-author that shape token-by-token, while judgment-determined
*content* stays with the AI and is passed to the handler only after being decided.
Generalizes the Enforcement Gap one layer down, into AI output shape rather than
protocol gates. Only a structural enforcement gain if the AI's ordinary write path to
the handler's target artifact is also closed off — otherwise a procedural convention
only. See Principle 15.

**Bypass-Prevention Caveat** — The condition, attached to the Handler Pattern, that a
handler retires a downstream audit check only if calling the handler is non-optional.
An open write path around the handler means the handler prevents mistakes only on the
AI's cooperative path, and any audit check retired on the strength of the handler's
existence alone has been retired on a false premise. See Principle 15.

**Assertion-Gated Success** — The general form of Anti-Pattern 9 (The Asserted
Ratification): a terminal status label — "Closed," "Passed," "Detected," "Complete"
— applied on the strength of a plan or a proposal to satisfy a condition, rather than
independent verification that the condition holds. Applies to audits, validators,
disposition tables, and status trackers, not only REP's ratification gates. See
Anti-Pattern 14 and Principle 11.

**Long-Chain Keyword** — A naming convention for load-bearing methodology artifacts:
a distinctive, low-collision, multi-token acronym or coined term (e.g. `CLDS`) used
in place of a generic descriptive noun (e.g. "specification"), so the filename itself
resists being filled in from a generic training-data prior. The resolution to
Anti-Pattern 13, and the reason this document is named `CLDS.md` rather than
`SPECIFICATION.md`.

---

*CLDS.md is itself a living document. It describes a methodology in active
use and should be updated as the methodology evolves through practical application.
Every significant revision should be logged with a rationale, modeling the same
discipline it prescribes.*

*Version 1.0 — Initial manifesto*
*Version 1.1 — Amendments from DISSONANCE.md review and REP discovery:*
  *- C4 decoupled from Architectural Authority Principle; README-as-architecture*
  *  formalized as minimum viable alternative*
  *- Gherkin replaced as mandatory with Behavioral Contracts as the primitive;*
  *  YAML acceptance criteria formalized as the minimum viable contract format*
  *- Minimum Viable Specification principle added (Principle 10 + Appendix B)*
  *- Negotiable vs non-negotiable architecture distinction added (Principle 9)*
  *- Phase model reframed as dominant modes rather than strict sequence*
  *- Drift vs Evolution distinction added (Section 4.2)*
  *- CLDS acknowledged as era-contingent (Preamble)*
  *- CLDS acknowledged as distributed cognition framework, not software methodology*
  *  specifically (Preamble)*
  *- Invariant graduation criteria added (Section 3.4)*
  *- REP (Ratified Execution Protocol) added as Part V — the operational layer*
  *  discovered empirically through accidental read-only mode constraint*
  *- Anti-Pattern 6 (Specification Bureaucracy) and Anti-Pattern 7 (Silent Execution)*
  *  added*
  *- Bottleneck inversion noted as design constraint shaping all workflow decisions*
*Version 1.2 — Amendment from AAA_*.py test suite workflow observation:*
  *- REP Step 6.5 (Plan-Implementation Alignment Audit) added between*
  *  Step 6 and Step 7. Discovered through the observation that PLAN.md*
  *  and AAA_tests.py had a coverage gap (teardown tests, Scenario C modal*
  *  operator testing) that neither the plan author nor the implementor*
  *  surfaced. The gap was detected by manual comparison — which REP now*
  *  delegates to a CA in a fresh context.*
  *- Anti-Pattern 8 (The Unverified Plan) added: the pattern of assuming*
  *  plan coverage because both plan and implementation were CA-produced.*
  *- Reading Cost Calibration table updated with Step 6.5 row.*
  *- Glossary entry added for Plan-Implementation Alignment Audit.*
  *- Distinction between Step 6 authority (spec/behavior) and Step 6.5*
  *  authority (plan/strategy) made explicit in Step 6.5 text.*
*Version 1.3 — Amendment from RodinParser session observation and RV conceptualization:*
  *- Part X (The Ratification Vault) added: the programmatic enforcement*
  *  substrate for CLDS and REP. Addresses the enforcement gap — the structural*
  *  vulnerability in any protocol that relies on AI self-reporting for gate*
  *  compliance. Defines RV's state machine files (RV-STATE.md, INVARIANTS.md,*
  *  PLAN.md), the central design constraint (out-of-band human tokens, external*
  *  validator), and the phased implementation strategy (Phase 1: maximum human*
  *  control → Phase 4+: minimum viable human input).*
  *- Anti-Pattern 9 (The Asserted Ratification) added: the pattern of an AI*
  *  self-reporting gate compliance without structural verification, particularly*
  *  acute in agentic contexts. Framed as an architectural consequence, not a*
  *  behavioral failure.*
  *- Principle 11 (Enforcement Over Assertion) added: procedural compliance and*
  *  structural compliance are not equivalent; design for structural compliance*
  *  wherever the gate matters enough to be specified.*
  *- CLDS stack diagram added to Appendix A: CLDS → REP → RV as three distinct*
  *  layers (framework, protocol, enforcement substrate).*
  *- Glossary entries added: Ratification Vault (RV), Enforcement Gap, Structural*
  *  Compliance, Procedural Compliance, Ratification Gate, Apodictically-Enforced*
  *  Constraint.*
  *- Appendix A Quick Reference updated: CLDS stack diagram, Principle 11, Anti-Pattern 9.*
*Version 1.4 — Amendment from diegetics INSPECTOR.md workflow observation — 2026-06-30T17:42:00Z:*
  *- Section 3.5 (The Audit Layer) added to Part III: formalizes INSPECTOR.md and*
  *  DISSONANCES.md as a distinct artifact category in the CLDS toolstack, sitting*
  *  between the specification layer and the implementation cycle. Defines the black-box*
  *  constraint (epistemologically load-bearing, not procedural hygiene), the fixed-schema*
  *  output property (session-boundary safety), and the Compliance Signal concept.*
  *  Establishes the critical maintenance invariant: INSPECTOR.md must be updated after*
  *  every major refactor before the next audit cycle runs.*
  *- Principle 12 (Audit Artifacts Must Track the Specification) added: an audit procedure*
  *  referencing superseded behavioral expectations produces noise, not findings. The*
  *  maintenance invariant for INSPECTOR.md is non-optional. Framed as a special case of*
  *  Principle 2 (Intent Flows Downward): specification changes propagate into the audit*
  *  procedure before the next audit cycle.*
  *- Anti-Pattern 10 (The Stale Audit) added: INSPECTOR.md written once and never*
  *  updated produces false positives (behaviors the spec no longer promises) and false*
  *  negatives (behaviors the spec now promises but the procedure does not probe). The*
  *  failure mode is insidious because it does not announce itself — stale audit output*
  *  looks like a legitimate audit. Resolution: treat INSPECTOR.md as a specification*
  *  artifact with the same maintenance discipline as README.md or YAML schemas.*
  *- Compliance Signal concept introduced in Section 3.5 and Glossary: a cheap,*
  *  discrete, observable probe whose presence confirms a behavioral contract was met.*
  *  Formalized from empirical observation of AGENTS.md behavioral contract workflows.*
  *  The Van Halen M&M clause is the canonical external instantiation; RV's rv validate*
  *  output is the apodictic instantiation; INSPECTOR.md Phase H is the procedural*
  *  instantiation. All three are the same structural idea at different enforcement strengths.*
  *- CLDS Toolstack Quick Reference updated: Audit Layer added as fifth artifact category.*
  *- Principles Quick Reference updated: "Eleven Principles" → "Twelve Principles."*
  *- Glossary entries added: Audit Layer, INSPECTOR.md, DISSONANCES.md, Compliance Signal,*
  *  Specification-Conformance Auditing.*
*Version 1.5 — Amendment from DIEGETICS.md fragmentation design session and sempath*
*README terminology-matching analogy — 2026-07-01T14:00:00Z:*
  *- Section 3.6 (The Fragmented Specification Architecture) added to Part III:*
  *  formalizes the per-module SPEC.md pattern discovered while planning DIEGETICS.md's*
  *  decomposition. Establishes the Build Reversal — Specification Fragments are*
  *  canonical and hand-edited; the monolithic specification document is a generated*
  *  build artifact, never hand-edited directly. Defines the SPEC.md naming convention*
  *  as enforced by full_spec_builder.py's resolution behavior rather than by human*
  *  memory, the spec-hash freshness mechanism between a fragment and its schema*
  *  (Section 3.6.2), and the two-tier Glossary Collision / Term Proliferation check*
  *  (Section 3.6.3), the latter adapted from controlled-vocabulary/thesaurus practice*
  *  (ISO 25964) after a sempath README review surfaced the analogy directly.*
  *- Section 3.7 (Audit Scope Tiering) added to Part III: splits the Audit Layer*
  *  (Section 3.5) into Tier 1 (Local/Module, frequent) and Tier 2 (Global/Cross-*
  *  Cutting, infrequent) audits, motivated by an empirical observation that full-*
  *  codebase audit prompts were catching genuine cross-cutting dissonance at a token*
  *  cost that punishes the frequency needed to catch local drift early. The*
  *  Fragmented Specification Architecture (3.6) supplies the scope boundary that*
  *  makes Tier 1 audits possible.*
  *- Principle 13 (Cost-Ordered Verification) added: generalizes the cheap-tier-*
  *  unconditional / expensive-tier-gated pattern observed independently in Section*
  *  3.6.3's glossary check, Section 3.7's audit tiers, and cost-ordered matching*
  *  pipelines generally.*
  *- Principle 14 (Audit Scope Must Match Invariant Scope) added as a direct companion*
  *  to Principle 12: an invariant's scope determines the minimum audit scope capable*
  *  of verifying it; conflating Local audit cleanliness with Global coherence is a*
  *  category error, not a shortcut.*
  *- Anti-Pattern 11 (The Orphaned Schema) added: a schema that silently drifts from*
  *  its authorizing SPEC.md after the fragment is edited and the schema is not.*
  *  Identified as the structural inverse of Anti-Pattern 10 (The Stale Audit) — same*
  *  failure shape, opposite artifact, opposite direction of drift.*
  *- Anti-Pattern 12 (The Unswept Seam) added: treating a clean sweep of Tier 1 Local*
  *  audits as sufficient evidence of system-wide coherence, when the actual defect*
  *  lives in the interaction between two locally-compliant modules.*
  *- Corrected a pre-existing drift in Part III's introductory text: it claimed "three*
  *  categories of specification artifact" despite Section 3.5 (added in v1.4)*
  *  explicitly characterizing the Audit Layer as "a fourth category." Updated to*
  *  "four categories." Logged here rather than silently patched, per the document's*
  *  own discipline — this was found, not introduced, during the v1.5 revision pass.*
  *- CLDS Toolstack Quick Reference updated: Fragmented Specification Architecture and*
  *  Audit Scope Tiering added as additional entries.*
  *- Principles Quick Reference updated: "Twelve Principles" → "Fourteen Principles."*
  *- Glossary entries added: Specification Fragment, full_spec_builder.py, Spec-Hash,*
  *  Glossary Collision, Term Proliferation, Audit Scope Tiering, Cost-Ordered*
  *  Verification.*
*Version 1.6 — Amendment from cross-system review (GPT transcript on document*
*structure) and diegetics INGEST.md Handler Pattern generalization — 2026-07-26:*
  *- Document renamed from `SPECIFICATION.md` to `CLDS.md`. The rename is not*
  *  cosmetic: a generic filename is itself an attack surface for hallucination in*
  *  AI contexts, since a string like "SPECIFICATION.md" is heavily represented*
  *  across unrelated training data and codebases, giving a model a false prior*
  *  that it already knows the file's contents. Documented prescriptively as*
  *  Anti-Pattern 13 (The Generic Artifact Name), resolved via the Long-Chain*
  *  Keyword naming convention.*
  *- Principle 15 (The Handler Pattern) added: generalizes a shape/content boundary*
  *  discovered while auditing diegetics' INGEST.md relationship-edge defaults*
  *  (default scaffolding belongs to a deterministic handler; inferred narrative*
  *  values stay with the Agent) into a CLDS-level principle. Promoted with a*
  *  mandatory bypass-prevention caveat — the pattern is only a structural*
  *  enforcement gain, not merely a procedural convention, if the Agent's ordinary*
  *  write path to the handler's target artifact is independently closed off.*
  *  Without that closure, downstream audit checks the Handler Pattern appears to*
  *  obsolete remain load-bearing.*
  *- Anti-Pattern 14 (Assertion-Gated Success) added: generalizes Anti-Pattern 9*
  *  (The Asserted Ratification) beyond REP's ratification gates to any terminal*
  *  status label — audit/validator output, disposition tables, status trackers —*
  *  asserted on the strength of a plan or proposal rather than independent*
  *  verification. Surfaced by two observed instances: a validator emitting a*
  *  positive detection signal for a check it is structurally incapable of*
  *  performing, and a dissonance-tracking table marking items "Closed" on the*
  *  strength of a drafted amendment not yet applied to the artifact it amends.*
  *- Section 3.6.4 (Open Question — Reflexive Application to CLDS.md's Own*
  *  Document) added under the Fragmented Specification Architecture. Makes*
  *  explicit a distinction that had previously been conflated in practice: the*
  *  Fragmented Specification Architecture (3.6) governs how projects adopting*
  *  CLDS organize their own domain specs, and says nothing, by itself, about*
  *  whether or how CLDS.md's own Parts, Principles, and Anti-Patterns should be*
  *  reflexively fragmented — a decision recorded in prose is not a decision*
  *  actualized in a build tool, and `full_spec_builder.py` remains unbuilt.*
  *  Records two live, non-default candidate answers to "what counts as a module*
  *  of a methodology" — topical/Part-based fragmentation, and epistemic-layer*
  *  fragmentation (Theory/Principles/Protocols/Mechanisms/Reference*
  *  Implementations, proposed independently in a cross-system review) — as an*
  *  open fork to be resolved through REP if and when it becomes live, not*
  *  adopted on the strength of an external transcript's elegance.*
  *- CLDS Toolstack Quick Reference entry for Fragmented Specification Architecture*
  *  updated with a pointer to the 3.6.4 scope clarification.*
  *- Principles Quick Reference updated: "Fourteen Principles" → "Fifteen*
  *  Principles."*
  *- Glossary entries added: Handler Pattern, Bypass-Prevention Caveat,*
  *  Assertion-Gated Success, Long-Chain Keyword.*
  *- Self-referential note: this changelog entry, and the "amendment drafted"*
  *  language used throughout Version 1.6, are themselves written to satisfy*
  *  Anti-Pattern 14 — i.e., this revision does not mark itself "Closed" anywhere;*
  *  it is complete as a drafted and applied amendment to this file, verifiable*
  *  by reading the sections it claims to have added.*
