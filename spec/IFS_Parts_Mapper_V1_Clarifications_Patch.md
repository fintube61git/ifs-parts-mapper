# IFS Parts Mapper V1 — Clarifications Patch

This document resolves remaining ambiguities in the V1 specification.

It does not add features or expand scope.
It only clarifies existing rules to prevent drift.

If any earlier spec documents conflict with this patch, this patch takes precedence.

---

## Clarification 001 — Notes Length Limit (V1)

Issue:
Specs state that notes must be “short” but do not define a limit.

Resolution (V1 Final):
- Part.notes and Relationship.notes must be ≤ 280 characters.
- If the limit is exceeded, validation must fail.

Rationale:
- Prevents journaling and PHI risk.
- Enforces descriptive, not narrative, usage.

---

## Clarification 002 — intensity and strength Data Type (V1)

Issue:
Specs describe intensity and strength conceptually but do not define type.

Resolution (V1 Final):
- intensity and strength are optional integers.
- Valid range: 0–10 inclusive.
- If present and invalid, validation must fail.

Rationale:
- Prevents drift into scoring systems.
- Ensures consistent schema enforcement.

---

## Clarification 003 — Unknown Fields on Import (V1)

Issue:
Specs inconsistently describe whether unknown fields should be rejected or flagged.

Resolution (V1 Final):
- Unknown fields in imported JSON must be rejected.
- Import must fail if any unknown fields are present.

Rationale:
- Prevents silent schema drift.
- Enforces strict canonical structure.

---

## Clarification 004 — schema_version Import Rule (V1)

Issue:
schema_version behavior is partially specified but not explicitly enforced.

Resolution (V1 Final):
- Export must always emit schema_version = "1.0.0".
- Import must accept only schema_version matching 1.x.x.
- Import must reject any other schema_version.

---

## Clarification 005 — Trailhead Language in UI (V1)

Issue:
UI specs use “tags” language that implies ontology or taxonomy.

Resolution (V1 Final):
- dominant_protector_patterns and core_vulnerability_themes are lists of short descriptive phrases (strings).
- No controlled vocabulary, ontology, or semantic inference is permitted.

UI wording must avoid the term “tags” in V1.

---

## Clarification 006 — Bulk Linking Scope (V1)

Issue:
Bulk linking is required but its scope is not fully specified.

Resolution (V1 Final):
- Bulk linking applies only to:
  - protects relationships
  - between protectors and exiles
- Bulk linking must not apply to:
  - polarized_with relationships
  - other category pairings in V1.

Rationale:
- Prevents ontology creep.
- Aligns with V1 UI wireframe and scope freeze.

---

## Priority Order Update (V1)

For V1 interpretation, precedence is now:

1. Errata file
2. Clarifications Patch (this document)
3. Minimal Canonical JSON Schema
4. Master Spec Hardened
5. All other spec documents

If conflicts exist, higher-precedence documents win.
