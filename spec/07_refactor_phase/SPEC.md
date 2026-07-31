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

