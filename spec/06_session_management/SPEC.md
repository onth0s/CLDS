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

