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

