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

