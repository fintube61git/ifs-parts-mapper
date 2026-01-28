# IFS Parts Mapper V1 — Supreme Authority

This file defines the final authority rules for V1.

No other spec files should be edited to resolve conflicts.
If any documents disagree, follow the rules below.

---

## Authority Order (V1)

1. Errata
2. Clarifications Patch
3. Minimal Canonical JSON Schema
4. Model Contract
5. Master Spec Hardened
6. All other documents (UI, Build Map, Mapping Table, etc.)

If any document conflicts with a higher item, the higher item wins.

---

## Trigger Rule (V1)

trailhead.trigger is a string in V1.

UI descriptions that imply tags or structured trigger fields must be ignored.

---

## Numeric Fields (V1)

intensity and strength are optional integers in range 0–10.

---

## Import Rule (V1)

Unknown fields in JSON imports must be rejected.
