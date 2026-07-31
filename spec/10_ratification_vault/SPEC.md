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

