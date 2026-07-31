# Cognitive Load Distribution System (CLDS)

[![Specification Architecture](https://img.shields.io/badge/Specification-Fragmented-blue.svg)](#specification-architecture)
[![Build Tooling](https://img.shields.io/badge/Builder-full__spec__builder.py-green.svg)](#build-tooling)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

> *"The specification artifacts are not documentation. They are infrastructure."*

**CLDS** (Cognitive Load Distribution System) is a living, meta-methodological framework designed specifically for human-AI software co-creation. It distributes cognitive labor across the fundamental asymmetry of AI development: human design vision vs. AI implementation capability without persistent memory.

---

## Specification Architecture

This repository adopts the **Fragmented Specification Architecture** (CLDS Section 3.6). Rather than maintaining a monolithic specification document by hand, specifications are organized into canonical, per-module **Specification Fragments** (`spec/*/SPEC.md`).

```
CLDS/
├── spec/                                # Canonical, hand-edited specification fragments
│   ├── 00_preamble/SPEC.md              # Core thesis, cognitive asymmetry, era contingency
│   ├── 01_two_regimes/SPEC.md           # Terminal-Goal Software vs Open-Ended Creative Tooling
│   ├── 02_development_lifecycle/SPEC.md # Dominant Modes (Exploration vs Design) & 7 Phases
│   ├── 03_toolstack/SPEC.md             # Structural Models, YAML Specs, Audit Layer
│   ├── 04_specification_loop/SPEC.md    # Domain Crystallization, Drift vs Evolution
│   ├── 05_rep/SPEC.md                   # Ratified Execution Protocol (REP 7-step sequence)
│   ├── 06_session_management/SPEC.md    # Context management & session closing protocols
│   ├── 07_refactor_phase/SPEC.md        # Architectural Audit & Feature Inventory
│   ├── 08_principles/SPEC.md            # The 15 Core Principles
│   ├── 09_anti_patterns/SPEC.md         # Anti-Patterns 1 through 14
│   ├── 10_ratification_vault/SPEC.md    # Programmatic enforcement substrate (RV)
│   └── 11_appendices/SPEC.md            # Quick Ref, Minimum Viable Spec, Glossary
├── tools/
│   └── full_spec_builder.py             # Assembles fragments -> timestamped monoliths
├── archive/                             # Historical CLDS_[epoch].md builds (gitignored)
└── pyproject.toml                       # Tooling configuration (Ruff)
```

---

## Build System & Workflow

The monolithic build artifacts are **generated** from `spec/` fragments using `full_spec_builder.py`. The top-level monolith is never hand-edited directly (Principle 2: *Intent Flows Downward*).

### 1. Build the Monolithic Spec
Run the builder script to run Tier 1 Glossary Collision checks, archive previous builds, and emit a timestamped output:

```bash
python tools/full_spec_builder.py
```

Outputs:
* `CLDS_<epoch_timestamp>.md` — Timestamped build artifact.
* `archive/` — Outdated timestamped builds are automatically moved here.

### 2. Linting & Formatting
Python tooling is enforced using `ruff`:

```bash
python -m ruff check tools/
python -m ruff format tools/
```

---

## Core Infrastructure Principles

1. **Principle 1: The Specification Is Infrastructure** — Specs encode intent across session boundaries.
2. **Principle 3: The AI Proposes; You Ratify** — Human maintains structural authority; AI implements ratified specifications.
3. **Principle 11: Enforcement Over Assertion** — Gate compliance is structurally enforced, not self-reported.
4. **Principle 13: Cost-Ordered Verification** — Cheap deterministic checks run unconditionally; expensive probabilistic checks are gated.

---

## License

Private Repository — All Rights Reserved.
