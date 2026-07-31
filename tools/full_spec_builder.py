#!/usr/bin/env python3
"""full_spec_builder.py

Assembles canonical Specification Fragments (`spec/*/SPEC.md`) into a single
epoch-suffixed monolithic document (`CLDS_<epoch_time>.md`) and updates `CLDS.md`.
Automatically moves historical builds to `archive/`. Performs Tier 1 Glossary
Collision checks unconditionally.
"""

import glob
import os
import re
import shutil
import sys
import time

SPEC_DIR = "spec"
ARCHIVE_DIR = "archive"
ROOT_SPEC = "CLDS.md"


def check_glossary_collisions(fragments):
    """Tier 1 Glossary Collision Detection across fragments.

    Parses glossary terms in Appendix C to ensure zero duplicate key collisions.
    """
    seen_terms = {}
    collisions = []

    term_pattern = re.compile(r"^\*\*(?P<term>[^*]+)\*\*\s*—")

    for path, content in fragments:
        # Scope strict glossary collision checking to the appendices/glossary fragment
        if "11_appendices" in path:
            lines = content.splitlines()
            for idx, line in enumerate(lines, 1):
                match = term_pattern.match(line.strip())
                if match:
                    term = match.group("term").strip().lower()
                    if term in seen_terms:
                        collisions.append((term, seen_terms[term], (path, idx)))
                    else:
                        seen_terms[term] = (path, idx)

    if collisions:
        print("[FAIL] CRITICAL: Tier 1 Glossary Collision(s) Detected!")
        for term, prev, current in collisions:
            print(
                f"  - Term '{term}' defined in {current[0]}:{current[1]} "
                f"collides with definition in {prev[0]}:{prev[1]}"
            )
        sys.exit(1)
    else:
        print("[OK] Tier 1 Glossary Collision Check Passed (0 collisions).")


def build_full_spec():
    if not os.path.exists(SPEC_DIR):
        print(f"[FAIL] Error: Specification directory '{SPEC_DIR}' does not exist.")
        sys.exit(1)

    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # 1. Discover all spec fragments in numeric directory order
    fragment_files = sorted(glob.glob(os.path.join(SPEC_DIR, "*", "SPEC.md")))
    if not fragment_files:
        print(f"[FAIL] Error: No SPEC.md fragments found under '{SPEC_DIR}/'.")
        sys.exit(1)

    fragments = []
    for filepath in fragment_files:
        with open(filepath, "r", encoding="utf-8") as f:
            fragments.append((filepath, f.read()))

    print(f"[INFO] Discovered {len(fragments)} specification fragments.")

    # 2. Run Tier 1 Glossary Collision Detection
    check_glossary_collisions(fragments)

    # 3. Assemble complete specification content
    full_content_parts = []
    for _filepath, content in fragments:
        full_content_parts.append(content)

    full_content = "".join(full_content_parts)

    # 4. Generate timestamp and filenames
    epoch_time = int(time.time())
    new_spec_name = f"CLDS_{epoch_time}.md"

    # 5. Archive old timestamped CLDS_*.md files in root
    old_builds = glob.glob("CLDS_[0-9]*.md")
    for old_build in old_builds:
        archive_path = os.path.join(ARCHIVE_DIR, old_build)
        shutil.move(old_build, archive_path)
        print(f"[ARCHIVE] Moved: {old_build} -> {archive_path}")

    # 6. Write new timestamped build artifact
    with open(new_spec_name, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"[BUILD] Created: {new_spec_name}")

    # 7. Update root CLDS.md copy
    with open(ROOT_SPEC, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"[UPDATE] Updated pointer file: {ROOT_SPEC}")


if __name__ == "__main__":
    build_full_spec()
