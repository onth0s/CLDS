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

