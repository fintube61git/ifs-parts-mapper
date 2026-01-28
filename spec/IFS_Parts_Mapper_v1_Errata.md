# IFS Parts Mapper V1 — Errata

This document records binding corrections to the V1 specification.

If any earlier spec documents conflict with this errata, this errata takes precedence.

---

## Errata 001 — Trailhead.trigger Shape (V1 Freeze)

Issue:
Earlier V1 specs allowed multiple possible shapes for `trailhead.trigger`.

Resolution (V1 Final):
In V1, `trailhead.trigger` is a string.

Canonical rule:
- trailhead.trigger: string (may be empty)
- Structured trigger objects (e.g., tags/description) are explicitly forbidden in V1.

Impact:
- Any schema or implementation supporting non-string trigger shapes is non-compliant with V1.
- Future structured trigger formats are deferred to V2 or later.

UI Constraint:
- UI specifications must not imply or expose structured trigger fields in V1.

---

## Authority Clarification

For V1 schema questions, the following precedence applies:

1. This Errata file
2. Minimal Canonical JSON Schema (V1)
3. Master Spec Hardened
4. All other spec documents

If conflicts exist, the higher-precedence document wins.
