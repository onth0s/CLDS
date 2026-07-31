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

