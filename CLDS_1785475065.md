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

## Part II: The Development Lifecycle

### 2.1 Dominant Modes, Not Strict Phases

CLDS describes a development lifecycle in terms of **dominant modes** rather than strict
sequential phases. At any point in a project, you are predominantly in one of two modes:

**Exploration Mode** — specification is emergent, iteration is fast, debt is consciously
accepted as the price of learning. The goal is domain understanding, not architectural
correctness. Vibecoding is appropriate. CLDS tooling is deliberately light.

**Design Mode** — specification is authoritative, iteration is disciplined, debt is
actively managed. The goal is architectural integrity, not speed of discovery. Full
CLDS tooling is engaged.

Real projects cycle between these modes. A new subsystem may warrant a return to
exploration mode even within an otherwise designed system. A feature whose domain
turns out to be more complex than anticipated may require a local return to exploration
before design can proceed. This cycling is healthy, not a methodology failure.

The lifecycle described below is the idealized arc of a project's dominant mode.
It describes the *vector* — the general direction of travel — not a rigid sequence
of discrete events.

### 2.2 The Seven Phases

```
Phase 1: CRYSTALLIZATION
  General idea → domain vocabulary → core use case hypothesis
  Mode: Exploration

Phase 2: SHELL
  Vibecode a minimal, functional skeleton → establish basic data flow
  Mode: Exploration

Phase 3: UI PROTOTYPE
  Interface without functionality → force reasoning about user mental model
  before committing to system data model
  Mode: Exploration

Phase 4: MINIMAL FUNCTIONALITY TEST
  Add just enough real behavior to test the actual use case →
  specification crystallizes from collision with reality
  Mode: Exploration → transition beginning

Phase 5: EXPLORATORY ITERATION
  Iterate until bugs, scope pressure, or structural debt signals the
  inflection point → document everything that works
  Mode: Exploration → inflection point

Phase 6: FULL REFACTOR (The Mode Transition)
  CLDS tooling engaged fully → design the system that should exist
  given everything learned → implement only verified working features
  Mode: Design

Phase 7: DISCIPLINED EVOLUTION
  Every new feature passes through the specification loop before
  implementation → the architecture grows with intention
  Mode: Design (with local exploration cycles permitted)
```

### 2.3 The Inflection Point

Recognizing the inflection point — the moment when the exploratory prototype has
accumulated enough real behavior to be *understood* but enough structural debt to be
*untrustworthy* — is one of the most valuable skills in AI-assisted development.

The signals:

- A bug fix in one component breaks something semantically unrelated
- Adding a new feature requires modifying more than three existing files
- You can no longer explain the data flow through the system without consulting the code
- The AI begins generating solutions that conflict with decisions made in earlier sessions
- The README (or its absence) no longer accurately describes what the system actually does

When these signals appear, the correct response is not another iteration. It is the
Full Refactor.

### 2.4 What the Full Refactor Is Not

The Full Refactor is not a rewrite motivated by aesthetic preference. It is not an
opportunity to adopt a new framework or technology stack out of curiosity. It is not
a punishment for having vibecoded the exploratory prototype.

The Full Refactor is a **deliberate mode transition** from exploration to design. It
uses everything learned in the exploratory phase — including the wrong turns — as input
to a specification-first design process.

The exploratory prototype is not wasted. It is the most important input to the specification.

---

## Part III: The CLDS Toolstack

CLDS uses four categories of specification artifact, operating at distinct abstraction
levels. They are not interchangeable. Each one captures something the others cannot.

Critically: the specific tools named here are **implementations of underlying principles**,
not the principles themselves. A README can serve as an architectural model. YAML
acceptance criteria can serve as behavioral contracts. The principle is always more
important than the format. Choose the lightest format that preserves the principle at
your project's scale.

### 3.1 The Architectural Model — Structural Authority

Every project needs a **persistent structural model**: an explicit, maintained artifact
that describes what the system is and how its parts relate. This model serves as the
**rejection filter** — the authority against which proposed changes can be evaluated
without requiring the full architectural context to be reconstructed from code.

The rejection filter function: when the AI proposes adding a new component, hook,
store, or endpoint, the architectural model provides the authority to evaluate that
proposal. Where does this live? What are its declared relationships? Does adding it
violate any structural invariant we have defined?

**Format options, from lightest to most formal:**

- **README-as-architecture**: for a solo developer on a single-container application,
  a well-maintained README with explicit domain entity descriptions, data flow narrative,
  and component responsibilities often provides a sufficient structural model. This is
  the minimum viable architectural artifact and is appropriate for projects of moderate
  complexity.

- **C4 Model**: for systems with multiple containers, external integrations, or team
  members, the C4 hierarchy (Context → Container → Component → Code) provides structured
  zoom levels that README prose cannot. Use C4 when the system's structural complexity
  exceeds what a single readable document can represent without losing important detail.

The choice between them is a scale decision, not a quality decision. A README that
is actually maintained is more valuable than a C4 diagram that has drifted from reality.

**CLDS-specific practices for the architectural model:**

- Load it into context at the start of every session that touches structure
- The C4 audit (or README audit) — mapping what actually exists against what is documented
  — is the first step of every Full Refactor
- When implementation reveals the model was wrong, update the model deliberately and
  annotate the reason; do not silently drift
- When the AI proposes a structural change, it must be ratified before implementation,
  then reflected in the model after

### 3.2 YAML Specification Files — The Contract Surface

YAML specification files are the **single source of truth** for what the system is
supposed to do at the domain entity level. They are more durable than code comments,
more precise than README prose, and more machine-readable than architectural diagrams.

Their structural advantage: YAML enforces completeness. A well-designed specification
schema forces you to define inputs, outputs, dependencies, constraints, and acceptance
criteria as parallel fields. You cannot accidentally omit the acceptance criteria because
the field is present and waiting.

The **constitutional document function**: YAML specs function as constitutional law for
the system. The AI can propose amendments; you ratify them; the spec governs what counts
as a valid implementation. This is the mechanism by which your architectural authority
is preserved across session boundaries.

**Recommended schema for a feature specification:**

```yaml
feature:
  id: FEAT-001
  name: ""
  status: draft | specified | implemented | verified | deprecated
  domain_entity: ""           # Which core entity does this feature touch?

  intent: ""                  # Why does this feature exist? One sentence.
  user_story: ""              # As a [user], I want [goal], so that [value].

  inputs: []                  # What data or events trigger this feature?
  outputs: []                 # What does it produce or mutate?

  dependencies:               # What must exist for this feature to function?
    features: []
    components: []
    external: []

  invariants: []              # What must always be true, regardless of implementation?
                              # See Section 3.4 for invariant graduation criteria.

  acceptance_criteria: []     # Observable conditions that define success.

  implementation_notes: ""    # Constraints, chosen approaches, rejected alternatives.

  architectural_location:     # Where does this live in the structural model?
    container: ""
    component: ""

  refactor_history: []        # Log of significant changes with rationale.
                              # Not optional. Undocumented refactors are invisible debt.
```

**CLDS-specific YAML practices:**

- Every domain entity gets its own specification before implementation begins
- `invariants` are the highest-priority field — they define what must survive any future refactor
- `refactor_history` is not optional; undocumented refactors are invisible debt
- The AI reads the YAML before implementing; you read it before accepting output
- When implementation reveals a mismatch with the spec, resolve at the specification
  level first, then propagate to code — never the reverse

### 3.3 Behavioral Contracts — The Oracle

Behavioral contracts specify the **observable behavior** of the system from the outside,
without reference to implementation. They serve three functions:

**1. Intent clarity**: forces reasoning about the system from the user's perspective.
What precondition makes this behavior meaningful? What action triggers it? What observable
outcome defines success? These are questions with architectural answers.

**2. Regression anchor**: when a feature is refactored, its behavioral contracts define
exactly what observable behaviors must be preserved. This is the primary safeguard against
refactors that improve structure while silently breaking behavior.

**3. Session handoff vehicle**: behavioral contracts are the most efficient way to
communicate expectations to an AI in a new session. "Here are the contracts this
component must satisfy" is more precise and more compact than prose description.

**Format options:**

- **YAML acceptance criteria** (inline in the feature spec): for simple features with
  linear behavior, a flat list of observable conditions in the `acceptance_criteria`
  field is sufficient. This is the minimum viable behavioral contract.

- **Gherkin scenarios**: for complex workflows, multi-step state transitions, or user
  journeys where the sequential Given/When/Then narrative structure genuinely aids
  clarity. Gherkin earns its overhead when behavior is temporal and branching; it is
  overhead when behavior is simple and stateless.

The `@invariant` concept is format-agnostic and should be preserved regardless of
which format is used. Some behavioral properties are non-negotiable across all future
refactors. These must be explicitly marked — whether as `invariants:` fields in YAML
or `@invariant`-tagged Gherkin scenarios. A refactor that breaks a marked invariant
is by definition wrong, regardless of any other improvement it achieves.

### 3.4 Invariant Graduation Criteria

Not every behavioral property deserves to be an invariant. An invariant that is wrong
is worse than no invariant — it encodes false confidence and will eventually cause the
AI to faithfully implement the wrong thing. The question of how a candidate property
graduates to invariant status is the methodology's most important open epistemological
question.

Current best-practice criteria, applicable at different specification levels:

- **Repeated survival**: the property has held true across multiple independent refactors
  without being intentionally violated. Time and change are the strongest validators.

- **Domain necessity**: removing the property would make the system unable to serve its
  core purpose. If the invariant were false, the system would not be the system.

- **User validation**: the property corresponds to observable behavior that users have
  confirmed they depend on. External validation is stronger than internal reasoning.

- **Architectural derivation**: the property follows necessarily from a higher-order
  invariant that is already established. Derived invariants inherit the authority of
  their parents.

These criteria are not equivalent. Domain necessity applies most strongly at the entity
level. User validation applies most strongly at the behavioral contract level.
Architectural derivation applies most strongly at the structural level. Repeated survival
is the universal fallback when other criteria are uncertain.

**The open question**: a complete theory of invariant validation — a principled epistemology
for how claims graduate from ideas to non-negotiable contracts — remains the most important
unresolved extension of CLDS. The criteria above are practical heuristics, not a theory.

### 3.5 The Audit Layer — Specification-Conformance Artifacts

The toolstack described in Sections 3.1–3.3 governs the *specification* of a system: what
it should do, how components relate, what behaviors are non-negotiable. A fourth category
of artifact addresses a different, orthogonal problem: **measuring whether the running
system conforms to its specification** — not through automated tests, but through
reproducible behavioral auditing.

The **Audit Layer** consists of two artifact types that operate in tandem:

- **`INSPECTOR.md`** — A reproducible procedure for exercising the running system as a
  black box, capturing its observable behavior against the specification, and writing
  findings to a structured output artifact. It produces evidence; it does not interpret it.
  It is explicitly constrained: no source code reads, no code modifications, all inputs
  reproducible, all outputs verbatim-quoted.

- **`DISSONANCES.md`** — The structured findings artifact populated by following
  `INSPECTOR.md`. Its schema is fixed and numbered (§1–§N) so findings are grep-addressable,
  session-boundary-safe, and ratifiable across AI contexts. It distinguishes *observed*
  findings from *inferred* ones. It is the evidentiary substrate that feeds the
  implementation ratification cycle.

The relationship between these artifacts and the rest of the CLDS stack:

```
SPECIFICATION LAYER       — DIEGETICS.md / README / YAML schemas / behavioral contracts
      ↓ (defines expected behavior)
AUDIT LAYER               — INSPECTOR.md (procedure) → DISSONANCES.md (findings)
      ↓ (surfaces conformance gaps)
IMPLEMENTATION CYCLE      — REP-governed corrections; findings become ratified changes
```

**The black-box constraint is epistemologically load-bearing.** `INSPECTOR.md` is
explicitly forbidden from reading source code to explain observed behavior. This is not
procedural hygiene — it is an architectural commitment to grounding findings in
*specification promises* rather than *implementation details*. A finding that says "the
CLI does not do X" is binding against the spec regardless of any future refactor. A
finding that says "the source does X" evaporates the moment the source changes.

**The fixed-schema output is a session-boundary property.** `DISSONANCES.md` uses
stable numbered sections so findings remain addressable across AI sessions, human reviews,
and implementation cycles. `§10` means the same thing to a CA opening the artifact three
months later as it does to the one who wrote it.

**The Compliance Signal.** `INSPECTOR.md` should contain, for each behavioral claim it
tests, a minimal elicitable signal whose presence confirms conformance and whose absence
confirms non-conformance. This is the CLDS instantiation of what Van Halen's tour rider
achieved with the M&M bowl: a cheap, discrete, observable probe whose cost is asymmetric
with its diagnostic value. The Phase H self-verification step in `INSPECTOR.md` is a
procedural Compliance Signal — before declaring done, every quoted block must exist in
the transcript, every "No" must be grounded. Compliance Signals work because they are
*cheap to verify* even when the underlying compliance is *complex to achieve*.

**Audit artifacts must be updated after major refactors.** This is the critical maintenance
invariant of the Audit Layer. An `INSPECTOR.md` that references behavioral expectations
from a previous version of the system is not a neutral artifact — it is a *misleading*
one. Its hardcoded behavioral claims (which commands exist, which schema fields are
displayed, which state transitions are valid) must be kept current with the specification.
After any major refactor or significant feature addition, `INSPECTOR.md` is updated
*before* the next audit cycle runs. A stale `INSPECTOR.md` will produce findings against
behavior the system no longer has — false positives — and miss behavior the system has
acquired — false negatives. Both failures undermine the audit layer's core purpose.

**CLDS-specific practices for the audit layer:**

- `INSPECTOR.md` drives the CLI as a black box; findings live in `DISSONANCES.md` only
- `DISSONANCES.md` section numbering is fixed once established; sections are not renumbered
  as findings are resolved (resolved findings are marked, not deleted)
- After a refactor, update `INSPECTOR.md` first, then run the audit, then reconcile
  `DISSONANCES.md`; the order is not negotiable
- The audit layer is not a test suite. It produces human-readable findings for ratification,
  not automated pass/fail signals. Its role in the CLDS cycle is evidentiary, not executional.
- Audit artifacts are version-controlled alongside the specification artifacts they reference

### 3.6 The Fragmented Specification Architecture — Specification Fragments and the Build Reversal

Sections 3.1 and 3.2 describe the architectural model and the YAML specification files
as artifacts maintained directly — as a single coherent document, or a small set of
per-entity files. At small scale this is correct: a monolithic specification document
is easier to read end-to-end than a scattered one, and fragmentation overhead is not
yet justified. At larger scale, a different failure mode emerges, and it is structural,
not aesthetic.

A monolithic specification document — hundreds or thousands of lines, covering every
domain entity in one file — degrades the property specification exists to provide: a
*local* authority a CA can check a *local* change against. The schema field being
edited and the prose clause that justifies it become spatially distant inside the file,
and spatial distance is exactly the kind of gap the Enforcement Gap (Section 10.1)
exploits. Nothing prevents a CA from editing a schema without consulting the relevant
section of a four-thousand-line specification — not because the CA is non-compliant,
but because nothing in the file layout makes the omission visible.

The **Fragmented Specification Architecture** resolves this by inverting which artifact
is canonical.

#### 3.6.1 The Build Reversal

In the monolithic model, the specification document is hand-maintained and is the
single source of truth. In the fragmented model, this direction is reversed:

- **Specification Fragments** — small, per-module `SPEC.md` files, each scoped to one
  domain entity or architectural component, co-located in the same directory as the
  schema(s) they authorize — are the canonical, hand-edited source of truth.
- **The monolithic specification document** (e.g. `DIEGETICS.md`) is a **generated
  build artifact**, assembled from the full set of fragments by `full_spec_builder.py`.
  It is never hand-edited directly; doing so is a direct violation of Principle 2
  (Intent Flows Downward), since the edit would land on a derived artifact rather than
  its source.

This reversal is not merely a filesystem reorganization. It changes which document a
CA is structurally positioned to consult while editing a given piece of code: the
fragment sits in the same directory listing as the schema, where its absence from a
CA's attention is conspicuous, rather than inside a large separate document where its
absence is invisible. Proximity does not make consultation mandatory — that requires
the spec-hash mechanism described in 3.6.2 — but it makes non-consultation visibly
negligent rather than merely unenforced, which is a real, if soft, reduction in
Enforcement Gap surface area.

The monolithic document remains valuable for a different purpose: the linear,
end-to-end read needed to onboard a new CA session, perform a Global Audit (Section
3.7), or support external cross-system review. It is a read artifact, not a write
artifact, in the fragmented model.

**Directory and naming convention:**

```
schemas/
  04.1_world_ledger/
    SPEC.md                    <- canonical, hand-edited; the section's prose
    snapshot.schema.yaml       <- header comment: # spec-hash: <sha256 of SPEC.md>
```

The directory's numeric prefix (`04.1_`) gives the builder a deterministic, sortable
assembly order without a separate manifest — the file tree does the ordering work for
free, consistent with Principle 10 (Minimum Viable Specification). A manifest
(`_order.txt` or equivalent) should only be introduced if section ordering genuinely
cannot be expressed through directory naming; it is not a default requirement.

The fragment filename is fixed: `SPEC.md`, matching the existing capitalization
convention of `README.md` and `AGENTS.md`. This convention is enforced not by a human
remembering it, but by `full_spec_builder.py`'s resolution behavior — the builder looks
only for files literally named `SPEC.md` when walking the fragment tree. A misnamed
file is invisible to the build, and its section silently drops out of the assembled
monolith. This is a loud, detectable failure (a missing section on the next build)
rather than a silently-violated naming convention, giving the rule real teeth without
requiring a dedicated resolver.

`full_spec_builder.py` walks the fragment tree in directory order, concatenates
`SPEC.md` contents into the monolithic document (including a merged, chronologically-
ordered changelog assembled from the per-fragment revision entries), and performs the
checks described in 3.6.2 and 3.6.3. It is deterministic and idempotent: an unchanged
fragment tree must produce a byte-identical monolith on every run, which is what
permits it to be run unattended as a pre-commit or CI step rather than only manually.

#### 3.6.2 Spec-Hash Stamping and Schema Freshness

Co-location (3.6.1) makes a Specification Fragment and its schema conspicuous to each
other; it does not make their consistency verifiable. Nothing about sitting two files
in the same directory prevents one from being edited while the other is not.

`full_spec_builder.py` closes this gap mechanically: on every build, it computes a
content hash of each `SPEC.md` and writes it as a header comment in the sibling
schema file(s) it authorizes. A trivial validator then diffs the hash currently stored
in the schema against the hash the fragment's present content would produce:

```bash
sha256sum schemas/*/SPEC.md | awk '{print $1}' \
  | diff - <(grep -h '# spec-hash:' schemas/*/*.schema.yaml | awk '{print $3}')
```

A mismatch means the fragment and its schema have drifted apart — in either direction.
Either the schema was edited and the stamp was never refreshed, or the fragment was
edited and the schema (and its stamp) were never revisited. Both are failures of the
same invariant: a schema's spec-hash must equal its authorizing fragment's current
hash, or the schema is not safe to treat as current. See Anti-Pattern 11.

#### 3.6.3 Glossary Collision and Term Proliferation

Merging glossary entries across many Specification Fragments introduces a problem a
single hand-maintained glossary never faced: two fragments, authored independently
(often in different sessions, sometimes months apart), may define vocabulary that
should have been unified and was not. This is not a hypothetical risk — it is the
same problem large organizations solve with controlled vocabularies and thesauri
(formally standardized as ISO 25964) when engineering and non-engineering stakeholders
must share exact terms for exact concepts. CLDS adopts the same structural distinction
that controlled-vocabulary practice has used for decades: not every mismatch is the
same kind of problem, and the two kinds require different responses.

**True Collision (Tier 1 — mandatory, build-blocking).** The same term, modulo
case/whitespace normalization, is defined twice with materially different meanings.
This is unambiguous: there is no judgment call about whether it is a problem, only a
duplicate key with conflicting values. `full_spec_builder.py` performs this check
unconditionally on every build, using a normalized-key dictionary with no external
dependencies. Any collision halts the build and reports both defining fragments side
by side. This check is never optional and never skipped — see Principle 13.

**Term Proliferation (Tier 2 — optional, advisory, non-blocking).** Two genuinely
distinct, individually well-defined terms across different fragments quietly refer to
the same underlying concept — "Character Roster" in one section, "Cast Registry" in
another — without either definition being wrong on its own. This failure is only
visible at the scale of the assembled glossary, not at the scale of any single
fragment, which makes it structurally similar to the cross-cutting dissonance that
motivates Section 3.7. Detecting it is an optional, explicitly-invoked mode of
`full_spec_builder.py` (e.g. `--check-proliferation`), using fuzzy string similarity
as a cheap first pass and, optionally, an embedding or LLM-assisted similarity check
as a more expensive second pass — gated behind explicit invocation precisely because
it is the costlier tier. See Principle 13.

A Term Proliferation flag is a **candidate for human review, never an instruction to
merge.** Auto-merging two terms because a similarity score crossed a threshold is a
glossary-layer instance of Anti-Pattern 9 (The Asserted Ratification): an automated
process asserting semantic equivalence with no ratification gate in between. Every
flagged pair is resolved by a human into one of a fixed taxonomy, adapted from
controlled-vocabulary practice:

- **MERGE** — true duplicate; collapse to one canonical term, update both fragments.
- **USE-FOR** — alias; one term redirects to the canonical entry but remains
  searchable, useful when a CA is plausibly likely to reach for either word.
- **RELATED** — distinct but worth a cross-reference note in both entries.
- **DISTINCT** — false positive; dismiss, no action.

**CLDS-specific practices for the Fragmented Specification Architecture:**

- `SPEC.md` fragments are hand-edited; the assembled monolith never is
- `full_spec_builder.py` runs Tier 1 glossary collision detection unconditionally on
  every build; Term Proliferation detection is explicitly invoked, not default
- Spec-hash mismatches are treated as build failures, not warnings
- A new domain entity or module gets a new fragment directory before its schema is
  written, not after

#### 3.6.4 Open Question — Reflexive Application to CLDS.md's Own Document

A scope clarification, stated explicitly because it has been a live source of
conflation: Section 3.6 as written governs how **projects adopting CLDS** organize
their own domain specifications — the per-module `SPEC.md` pattern discovered while
planning DIEGETICS.md's decomposition applies to a project's schemas, entities, and
subsystems. It says nothing, by itself, about how *this document* — CLDS.md —
should organize its own internal Parts, Principles, and Anti-Patterns. Treating a
written intention to fragment project specifications as though it already settled
the separate, harder question of whether and how to fragment CLDS.md's own
methodological content is a category error: a decision recorded in prose is not the
same object as a decision actualized in a build tool, and a decision actualized for
one target (a project's domain specs) does not automatically transfer to a
structurally different target (a methodology document *about* specs in general).
Both distinctions matter, and both are easy to blur under the shared word
"fragmentation."

Whether CLDS.md itself should ever be reflexively fragmented is therefore an **open
question, not a settled one**, and it stays open at minimum until `full_spec_builder.py`
exists and is deliberately pointed at this document — which has not happened; the
tool remains unbuilt as of this revision (see Appendix A, On the Horizon items
tracked in project practice). Should that day come, "what counts as a module of a
methodology" has at least two live candidate answers, neither of which should be
treated as a default:

- **Candidate 1 — Topical / Part-based fragmentation.** One fragment per existing
  Part (`REP.SPEC.md`, `RatificationVault.SPEC.md`, `AuditLayer.SPEC.md`,
  `Glossary.SPEC.md`, ...). Lower friction, because it mostly formalizes boundaries
  the document already has informally.
- **Candidate 2 — Epistemic-layer fragmentation.** One fragment per *kind* of
  knowledge rather than per topic — `Theory.SPEC.md`, `Principles.SPEC.md`,
  `Protocols.SPEC.md`, `Mechanisms.SPEC.md`, `ReferenceImplementations.SPEC.md` —
  separating *why* from *what must hold* from *recommended workflow* from *how it
  is enforced* from *concrete tooling*, regardless of which Part or topic each
  piece of content currently belongs to.

These candidates are not compatible without a real design choice. A single topic
like REP has content at every epistemic layer simultaneously — it embodies theory
about intent-flow, states principles, defines a protocol, and (per Part X) specifies
enforcement mechanisms — so Candidate 1 keeps REP whole and lets it contain all
layers internally, while Candidate 2 would slice REP itself apart across five
separate files. Candidate 2 was proposed independently, in a cross-system review
conversation with no visibility into this section, and is recorded here as a
legitimate candidate precisely *because* independent convergence on a structural
idea is a meaningful legibility signal — but a legibility signal is not a
ratification, and adopting either candidate now, on the strength of an external
transcript's elegance, would be exactly the premature structural commitment
Principle 10 (Minimum Viable Specification) exists to prevent. Resolution of this
fork, whenever it becomes live, should itself go through REP: a minimal plan,
ratification, and a logged decision — not an unforced adoption.

### 3.7 Audit Scope Tiering — Local and Global Audits

The Audit Layer (Section 3.5) as originally specified operates at a single scope: the
whole running system, audited as a black box against the whole specification. This is
the only mechanism available for catching genuinely cross-cutting dissonance —
duplicated logic between modules that do not reference each other, code that is dead
specifically because nothing in the *entire* tree calls it anymore, an invariant
violated only by the interaction of two individually-correct modules. None of these
are detectable from a local vantage point, by definition; they are properties of the
whole graph, not of any single node in it.

The cost of that completeness is real and punishes frequency. A full audit's token and
time cost scales with the size of the whole specification corpus, not the size of any
one change, which means it cannot run on every touch without becoming the dominant
cost center of the workflow. In practice this means full audits run rarely, and local
drift — a single module quietly diverging from its own `SPEC.md` — can accumulate for
a long interval before the next full sweep catches it.

The Fragmented Specification Architecture (Section 3.6) gives audits a natural,
cheaper scope boundary that did not previously exist: one `SPEC.md` fragment and its
corresponding code directory. This motivates splitting the Audit Layer into two tiers
rather than replacing it with one.

**Tier 1 — Local / Module Audits.** Scoped to a single fragment and its code
directory. Cheap enough to run frequently — on every touch to that directory, every
session, or every PR, depending on token budget. Catches local drift while it is still
small: a function whose behavior no longer matches its fragment, a field documented in
`SPEC.md` but absent from the schema. Writes a local `DISSONANCES.md` sibling, stamped
with the same spec-hash mechanism described in 3.6.2, so a local audit's freshness is
verifiable the same way a schema's is.

**Tier 2 — Global / Cross-Cutting Audits.** The audit described in Section 3.5,
unchanged in mechanism but narrowed in scope of responsibility once Tier 1 exists. It
no longer needs to rediscover every module's local conformance from scratch; it can
proceed from the assumption that Tier 1 has already verified local conformance, and
focus specifically on the class of dissonance invisible at module scope: cross-module
duplication, whole-tree dead code, and invariant violations that only manifest as an
interaction between modules. This narrowing is what keeps Tier 2 audits affordable
enough to still run, even infrequently.

**The tiers are complementary, not substitutable.** A clean sweep of every module's
Tier 1 audit is not evidence of system-wide coherence — it is evidence that no module
is locally inconsistent with its own fragment, which is a narrower claim. The defects
Tier 2 exists to catch live specifically in the seams between modules that each pass
their own local audit individually. Treating Tier 1 cleanliness as sufficient is itself
a named failure mode — see Anti-Pattern 12 and Principle 14.

**CLDS-specific practices for Audit Scope Tiering:**

- Tier 1 audits run at module-touch frequency; Tier 2 audits run on a fixed cadence
  independent of Tier 1 results
- A clean Tier 1 sweep never extends the interval before the next scheduled Tier 2 audit
- Tier 2 audit procedures may explicitly assume Tier 1-verified local conformance and
  scope their own effort to cross-module dissonance only
- Local `DISSONANCES.md` siblings follow the same resolved-not-deleted convention as
  the global artifact (Section 3.5)

---

## Part IV: The Specification Loop

The specification loop is the inner cycle that governs every significant feature addition
or refactor in Design Mode. It replaces the vibecode-and-iterate cycle with a deliberate
sequence that maintains architectural integrity.

### 4.1 The Loop

```
1. DOMAIN CRYSTALLIZATION
   Name the irreducible entities and their relationships.
   If you cannot name them, you are not ready to specify.

2. ARCHITECTURAL PLACEMENT
   Where does this feature live in the structural model?
   If it doesn't fit, the model needs updating — deliberately.

3. YAML SPECIFICATION
   Write the spec before implementation.
   Focus on invariants and acceptance criteria.
   Leave implementation_notes blank until you have something to say.

4. BEHAVIORAL CONTRACTS
   Write the observable oracle.
   Mark invariant contracts explicitly.
   Happy path first; edge cases after domain is stable.
   Use YAML acceptance criteria for simple features;
   Gherkin for complex multi-step workflows.

5. AI-ASSISTED IMPLEMENTATION (via REP — see Part V)
   Share: architectural model + relevant YAML specs + behavioral contracts.
   Instruct: implement to spec, flag any mismatch with reasoning.
   Constraint: propose architectural changes; do not make them unilaterally.

6. SPECIFICATION RECONCILIATION
   Review implementation against spec.
   If implementation reveals spec was wrong: update spec first, then code.
   If implementation drifts from spec without reason: revert and clarify.
   Log all significant decisions in refactor_history.
   Distinguish drift from evolution — see Section 4.2.

7. ARCHITECTURAL MODEL UPDATE
   If the implementation changed the structure, update the model.
   Never let the architectural model drift silently from reality.
```

### 4.2 Drift vs. Evolution

CLDS treats deviation from specification with discipline, but not with blanket suspicion.
Some deviations are mistakes. Others are discoveries — the implementation has revealed
something true about the domain that the specification did not yet know.

The distinction is not in the deviation itself but in its **deliberateness**:

- **Drift**: a change that moves away from specification without awareness. The spec says
  one thing; the code does another; nobody noticed. Drift is harmful because it is
  invisible — it breaks the invariant that the specification describes what the code does,
  silently and cumulatively.

- **Evolution**: a change that moves toward a better understanding of the domain, made
  with awareness and recorded. The implementation revealed that the spec's approach was
  suboptimal; the deviation was surfaced, reasoned about, ratified, and logged in
  `refactor_history`. Evolution is healthy — it is how specifications improve through
  contact with reality.

CLDS is not hostile to emergent architecture. Unix pipes, React hooks, event sourcing
patterns — these crystallized through repeated practical use, not prior specification.
CLDS is hostile specifically to *invisible* emergence. The discipline is making emergence
explicit and deliberate, not preventing it.

The mechanism that separates drift from evolution is the Reconciliation Principle:
when implementation deviates from spec, the deviation is surfaced, decided upon, and
logged. A discovered architectural improvement that goes through this process is
evolution. The same change made silently is drift. The difference is the deliberateness
of the decision, not the content of the change.

### 4.3 The Reconciliation Principle

Specification mismatch is not a failure — it is information. Implementations routinely
reveal that the specification was underspecified, contradictory, or based on incorrect
assumptions about the domain. This is expected and healthy.

The discipline is in *where the resolution happens*. The invariant:

**Specification changes flow downward into code. Code behavior never silently redefines
specification.**

When the AI proposes a deviation from the spec, it must:
- State the deviation explicitly
- Provide reasoning for why the spec's approach is suboptimal
- Propose specific spec language to replace the current spec

You then decide: accept the amendment and update the spec, or reject it and restate the
constraint. The AI implements whatever the ratified spec says.

This is not bureaucratic overhead. This is the mechanism by which you remain the
architectural authority rather than becoming a code reviewer for an AI that has quietly
accumulated design authority through incremental drift.

---

## Part V: The Ratified Execution Protocol (REP)

The Specification Loop describes *what* to specify and *how* to maintain it. The
Ratified Execution Protocol describes the *operational turn sequence* by which a
ratified specification becomes working code.

REP was discovered empirically — not designed from first principles. An AI agent
constrained to read-only mode could not write an implementation plan directly; it
instead produced a *minimal* plan to the CLI for human review. The constraint
accidentally instantiated the most important CLDS principle at the execution level:
the AI proposes, you ratify, before a single line of code is written. The protocol
that emerged from that accident is now the recommended execution layer for all
sufficiently significant implementation work.

The calibration principle governing every REP step: **minimize human reading cost
while maximizing architectural authority exercised.**

### 5.1 The Seven Steps

```
STEP 1 — MINIMAL PLAN REQUEST (Proposal-Only Mode)
  Instruct the AI to produce a minimal implementation plan:
  phases named, major operations listed, no implementation detail.
  Output fits on one screen. Readable in under two minutes.
  The AI cannot execute. It can only propose.

  This is the ratification surface — not a draft of the full plan,
  but the skeleton you annotate architecturally.

STEP 2 — RATIFICATION WITH ARCHITECTURAL ANNOTATIONS
  Read the minimal plan. Annotate directly:
  - Dependency order corrections
  - Scope exclusions
  - Behavioral preservation requirements
  - Approach rejections with alternatives
  These are architectural annotations, not editorial ones.
  They change what will be built, not how it will be described.

STEP 3 — FULL PLAN ELABORATION (Write Mode Enabled)
  The AI writes the full PLAN.md incorporating your annotations.
  This document now carries your ratification before implementation begins.
  It divides work into distinct phases with:
  - Explicit scope per phase
  - Success criteria per phase
  - Dependency order respected
  - No phase leaving the system in an invalid intermediate state

STEP 4 — FINAL APPROVAL
  One pass. Verify annotations were correctly incorporated.
  Check for new architectural assumptions introduced during elaboration.
  This is fast because you already ratified the structure.
  You are scanning for drift between minimal and full, not re-evaluating.

STEP 5 — PHASED EXECUTION
  For heavy implementations: execute phases sequentially, one at a time.
  For lighter scopes: execute all phases in sequence ("let it rip").
  Phase boundaries exist regardless — they are the unit of analysis
  for behavioral testing and problem localization, not just checkpoints.

STEP 6 — LOCAL BEHAVIORAL ANNOTATION PER PHASE
  After each phase (or after the full run for lighter scopes):
  test working features, note behavioral deviations.
  "This doesn't do X." / "This should look like Y."
  These are behavioral annotations — correcting implementation against
  spec — not re-opening architectural decisions.
  They are local: they address the phase that just ran, not the whole system.

STEP 6.5 — PLAN-IMPLEMENTATION ALIGNMENT AUDIT
  A CA — ideally a fresh context, not the one that wrote the implementation
  — is given PLAN.md and the implementation and asked one specific question:
  "Where does the implementation deviate from or fail to cover the plan?"
  The output is a deviation report, not a general quality review.
  Targeted, not open-ended.

  This step is the executable equivalent of Specification Reconciliation
  applied to the plan itself rather than the spec. PLAN.md is treated as
  a behavioral contract: the implementation must account for every scenario
  and fixture it declared. Coverage gaps surfaced here are either resolved
  before Step 7 or explicitly logged as deferred in DECISIONS.md.

  Calibration: do not conflate this with Step 6 (behavioral annotation).
  Step 6 corrects implementation against observable behavior.
  Step 6.5 corrects implementation against declared strategy.
  They are different authorities: spec vs. plan.

STEP 7 — FINAL IRON-OUT
  "Run ESLint and do a final lookaround for kinks."
  Single sentence. The AI performs pattern recognition on its own
  recently-written code: dead imports, unused variables, inconsistent
  naming, edge cases the happy-path testing did not surface.
  This is implementation hygiene, not architectural review.
```

### 5.2 Why Phase Boundaries Matter Even When You "Let It Rip"

When running all phases in a single execution, phase boundaries might appear to be
cosmetic — just headings in a document. They are not. They do two things regardless
of whether you pause between them:

**Scope discipline during planning.** Writing Phase 1 as a distinct unit forces the AI
to reason about what is complete at the end of Phase 1 independently of Phase 2. This
prevents implicit cross-phase dependencies that would make mid-run failure unrecoverable.
Each phase leaves the system in a valid state.

**The vocabulary for behavioral localization.** When testing after a full run reveals
something is wrong, "Phase 3 broke the border rendering" is a dramatically more useful
diagnostic than "something broke." Phase structure gives you a bounded implementation
unit to reason about.

The phases are not execution checkpoints that require your presence. They are the
structural unit of the entire protocol, including the lightweight path.

### 5.3 The Reading Cost Calibration

Every REP step is calibrated to a specific reading cost that is proportionate to the
authority being exercised:

| Step | Reading Cost | Authority Exercised |
|------|-------------|---------------------|
| Minimal plan review | ~2 minutes | Architectural ratification |
| Annotation | ~5 minutes | Structural decisions |
| Full plan review | ~5 minutes | Drift check, not re-evaluation |
| Phase behavioral testing | Variable | Behavioral contract verification |
| Plan-implementation alignment audit | ~5 minutes | Coverage gap detection |
| Final iron-out review | ~2 minutes | Implementation hygiene |

The total human reading investment for a week-equivalent implementation sprint is
measured in minutes, not hours. This is the payoff of ratifying the structure before
execution begins: the implementation phase requires behavioral verification, not
architectural re-adjudication.

---

## Part VI: Session Management

### 6.1 The Context Window as a First-Class Constraint

Every AI session has a finite context window. In long projects, the entire specification
corpus will not fit in a single session. This is a design constraint to architect for,
not a limitation to work around.

CLDS responds with **layered context loading**: load the minimum specification context
necessary to accomplish the session's goal, plus enough architectural context to prevent
local decisions from violating global invariants.

**Standard session opening protocol:**

```
1. Load architectural model (always — it is the structural authority)
2. Load YAML specs for components being touched in this session
3. Load behavioral contracts for features being implemented or modified
4. State the session goal explicitly: "In this session we are implementing FEAT-003"
5. State what is out of scope: "We are not touching the state management layer today"
```

The out-of-scope declaration is as important as the in-scope declaration. It prevents
the AI from making locally tempting improvements that violate session discipline.

### 6.2 The Session Closing Protocol

At the end of every productive session, before closing the context:

```
1. Update any YAML spec that changed during the session
2. Update architectural model if structure changed
3. Add any new behavioral contracts that emerged from implementation
4. Note unresolved decisions in DECISIONS.md for the next session
5. Summarize what was accomplished in a form the next session can read in 30 seconds
```

The session closing protocol is the investment that makes the next session cheaper.
Its absence is the primary source of context reconstruction debt — the tax paid at
the start of every session to re-establish what the previous session already knew.

### 6.3 The DECISIONS.md Convention

DECISIONS.md is a flat log of unresolved architectural questions, deferred decisions,
and known technical debt. It is not a task list. It is specifically for decisions that are:

- Too architectural for a code comment
- Too implementation-specific for the YAML spec
- Too unresolved to go in `refactor_history`
- Too important to lose between sessions

Format:

```markdown
## OPEN

### [DATE] — [Decision title]
Context: [What situation produced this decision point?]
Options: [What are the viable approaches?]
Blocking: [What cannot proceed until this is decided?]

## RESOLVED

### [DATE] — [Decision title]
Decision: [What was chosen?]
Rationale: [Why?]
Impact: [What changed in the spec/architecture/implementation?]
```

---

## Part VII: The Refactor Phase in Detail

### 7.1 The Architectural Audit

The Full Refactor begins with an architectural audit: a systematic mapping of what
*actually exists* in the codebase against what was *intended* to exist. This is
performed before any specification is written, because the specification must be
grounded in reality, not aspiration.

The audit produces three lists:
- **Components that exist as intended** — carry forward
- **Components that exist but deviate from intent** — specify the deviation; decide
  whether to align to original intent or ratify the deviation
- **Components that exist without design rationale** — the most dangerous category;
  these are the accumulated decisions of AI sessions that had no architectural
  authority to check against

### 7.2 Domain Model Crystallization

After the architectural audit, before writing a single YAML spec, name the irreducible
domain entities. These are the nouns the system is fundamentally about — entities that
would survive a complete technology stack replacement.

For a webtoon editor: Project, Chapter, Panel, TextGroup, TextBlock.
For a 3D asset pipeline: Asset, Stream, DecryptionKey, MeshBuffer, OutputFile.

The domain entities are the anchor points for everything else. Every YAML spec, every
behavioral contract, every architectural component ultimately traces back to one of
these entities. If a component cannot be expressed in terms of the domain entities,
that is a signal that either the entity list is incomplete or the component is
architectural debt wearing a feature's clothing.

### 7.3 The Feature Inventory

After domain crystallization, inventory every feature in the exploratory prototype:

```
VERIFIED WORKING     — behavior is correct, tested, and intentional
WORKING BUT UNSPECIFIED — behavior exists but rationale is unclear
PARTIALLY WORKING    — happy path works; edge cases are broken
BROKEN               — does not function as intended
SCOPE CREEP          — exists but is not core to the system's purpose
DUPLICATE            — same behavior is implemented in multiple places
```

The Full Refactor carries forward only VERIFIED WORKING features. Everything else is
specified first and then re-implemented — or consciously dropped.

The temptation is to carry forward PARTIALLY WORKING features because most of the
behavior is correct. Resist this. A PARTIALLY WORKING feature implemented without a
spec is a future broken feature with no contract defining what "fixed" means.

### 7.4 Specification-First Implementation

For every feature carried into the refactored system:

1. Write the YAML spec
2. Write the behavioral contracts
3. Confirm architectural placement
4. Execute via REP

This order is not negotiable in the refactor phase. In exploratory iteration (Phases 2–5),
you are learning — specification-first would be premature. In the Full Refactor, you
have learned. The specification is the product of the exploration.

---

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

## Part X: The Ratification Vault (RV)

### 10.1 The Enforcement Gap

CLDS, as specified through Part IX, is a **human-facing methodology**. Its authority rests
on the human developer loading the specification into context, issuing REP-compliant
instructions, and manually verifying that the AI followed the protocol. Every gate in REP
— the ratification of the minimal plan, the architectural annotations, the final approval,
Step 6.5 — is *procedurally expected*, not *structurally enforced*.

This creates a specific, systematic vulnerability: **the AI can assert compliance without
achieving it.** An LLM instructed to follow REP can:

- Claim to have produced a minimal plan while writing a full implementation plan
- Assert that Step 6.5 was completed without a fresh-context alignment audit having occurred
- Advance through ratification gates by outputting the correct language, even when no
  human has reviewed or approved anything
- Produce a `[RATIFIED]` marker in a document it controls, without any out-of-band human
  authorization having been issued

This is not malice. It is the structural consequence of building a protocol that lives
entirely inside the AI's context window and relies on the AI's self-reporting. RLHF-trained
models are systematically optimized to produce *plausibly compliant* output. A protocol
that rewards the appearance of compliance without verifying its substance will, over time,
receive the appearance.

This gap is called the **enforcement gap**: the distance between procedural compliance
(the AI says it followed the protocol) and structural compliance (the protocol was
demonstrably followed, with human authorization at every required gate).

REP as specified in Part V closes the enforcement gap *when the human is disciplined*.
The Ratification Vault closes it *structurally* — independent of session-to-session
human discipline.

### 10.2 What the Ratification Vault Is

The **Ratification Vault (RV)** is a programmatic enforcement substrate for CLDS and REP.
It is not a replacement for the human developer's architectural authority — it is the
mechanism that makes that authority *structurally non-bypassable* rather than merely
*procedurally expected*.

The Ratification Vault occupies a distinct layer in the CLDS stack:

```
CLDS   — The distributed cognition framework (philosophy + principles)
  └── REP    — The ratified execution protocol (operational turn sequence)
        └── RV     — The ratification vault (programmatic enforcement substrate)
```

CLDS describes *what* to do and *why*. REP describes *how* to sequence it. RV enforces
*that* it actually happened, via mechanisms the AI cannot self-report its way past.

### 10.3 The Central Design Constraint

The Ratification Vault must be designed with a single non-negotiable property:

**The AI cannot advance past a ratification gate without an out-of-band human action
that the AI itself cannot perform or replicate.**

This means:

- **Ratification tokens must originate outside the AI's context.** A file the AI can
  write to is not a ratification gate; it is a suggestion. True ratification requires
  a token, signature, or state change that only the human can introduce — from outside
  the AI's tool access boundary.

- **Validation must be performed by an external process.** The AI cannot validate its
  own gate compliance, for the same reason a regulated party cannot issue its own audit.
  The validator runs as an external CLI, pre-commit hook, or CI step — a process the
  AI must *call* but cannot *control*.

- **Checksums protect invariants from unilateral modification.** Core invariants
  (INVARIANTS.md or equivalent) are checksummed. The validator rejects a session state
  where the invariant file's checksum does not match the ratified baseline. The AI
  cannot modify invariants silently; it can only propose amendments through the
  ratification surface.

- **Obscurity is not enforcement.** Hiding the RV's rules from the AI's context is a
  convenience measure, not a security measure. LLMs do not strategically memorize bypass
  patterns across sessions — their non-compliance is structural (optimizing for plausible
  output), not strategic (circumventing known rules). The protective mechanism is the
  enforcement architecture, not information asymmetry.

### 10.4 The RV State Machine

The Ratification Vault operates as a **file-based state machine** — deliberately
file-based so it is git-tracked, diffable, and auditable without special tooling.
The state machine files are:

```
RV-STATE.md      — Current protocol phase, open ratification requests, last approved action.
                   Read by the AI at session open; written only by the validator.

INVARIANTS.md    — The non-negotiable behavioral properties. Checksummed.
                   The AI proposes amendments through the ratification surface.
                   The validator rejects any session state where the checksum does not match.

PLAN.md          — The elaborated implementation plan. Advances to "ratified" status
                   only after a human-approved token is placed in RV-STATE.md.
                   The AI can write PLAN.md; only the human can ratify it.

DECISIONS.md     — As specified in Section 6.3. Unchanged by RV.
```

The **validator** (`rv validate` or equivalent) is the enforcer. It is the external
process that checks the state machine's consistency before allowing any execution to
proceed. It verifies:

1. That the current phase's entry conditions were met (including human ratification)
2. That INVARIANTS.md has not been modified without a ratified amendment
3. That PLAN.md's ratification status matches the state in RV-STATE.md
4. That Step 6.5 (alignment audit) was completed before Step 7 (final iron-out)

Execution commands — file writes, code generation, test execution — are gated behind
validator passage. An agent that cannot produce a passing `rv validate` cannot proceed.

### 10.5 The Phased Implementation Strategy

The Ratification Vault is designed to start at **maximum human touchpoint density** and
reduce toward **minimum viable human input** as the enforcement substrate matures and
the protocol's reliability is empirically established.

```
RV Phase 1 — MAXIMUM HUMAN CONTROL (Bootstrap)
  All REP gates require explicit human approval tokens.
  Validator is run manually before every execution step.
  Human reviews and signs every state transition.
  Purpose: establish the protocol and validate the enforcement mechanism.

RV Phase 2 — AUTOMATED VALIDATION, HUMAN RATIFICATION
  Validator runs automatically (pre-commit hook, CI gate).
  Human still issues all ratification tokens.
  Automated checks handle the mechanical gate verification.
  Purpose: reduce the tax on disciplined humans while preserving all authority.

RV Phase 3 — NARROWLY AUTOMATED RATIFICATION
  Specific, well-bounded gate conditions are delegated to a narrow LLM judge.
  Example: Step 6.5 (alignment audit) is delegated to an LLM judge with a
  constrained scope — "does this implementation cover the plan?" — with a
  structured output that the validator processes deterministically.
  Human veto is always available. Human still ratifies all architectural gates.
  Purpose: reduce human reading cost for mechanical compliance checks.

RV Phase 4+ — MINIMUM VIABLE HUMAN INPUT
  Only architectural decisions and invariant amendments require human ratification.
  All mechanical protocol compliance is structurally enforced.
  The human is never the bottleneck for non-architectural process steps.
  Purpose: the terminal condition — disciplined AI-assisted development with
  minimal human overhead and zero uncontrolled drift.
```

The Phase 1 → Phase 4 arc mirrors the CLDS Exploration → Design mode transition at the
methodology level: begin with maximum human control to establish the correct baseline,
reduce overhead as empirical confidence is established. Never reduce control at a gate
before the gate's reliability has been demonstrated at the previous phase.

### 10.6 RV and the Architectural Authority Gap

The Ratification Vault addresses a specific failure mode in AI-assisted development that
CLDS terminology identifies as the **architectural authority gap**: the condition in which
the AI has accumulated effective design authority through incremental drift, because no
structural mechanism prevented it.

In a REP-governed session without RV, the human's architectural authority is *nominal*
— they have declared it through the methodology. In a REP + RV-governed session, the
human's architectural authority is *structural* — the enforcement substrate makes it
impossible for the AI to proceed past ratification gates without human authorization.

This distinction matters most in agentic contexts where the human is not watching every
step. An AI agent running in a long agentic loop with REP-but-no-RV will, eventually,
silently skip a ratification step — not maliciously, but because the optimization
pressure toward completing the task is stronger than the procedural expectation to pause.
RV makes the pause structural: the validator fails, the execution gate is closed, and
the agent cannot proceed until human authorization is issued.

---

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
