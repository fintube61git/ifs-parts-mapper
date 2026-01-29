# V1 CANONICAL MODEL — IFS PARTS MAPPER

This file is a one-page, implementation-facing statement of the canonical V1 model.
It exists to prevent ambiguity and AI drift.

Authority: This file is a summary and must remain consistent with the canonical hierarchy defined in:
- spec/IFS_Parts_Mapper_V1_Supreme_Authority.md
- spec/SPEC_AUTHORITY_MAP.md

If a conflict is found, follow the authority hierarchy (Errata → Clarifications Patch → Schema → Model Contract → Hardened).

---

## 1) Core Entities (V1)

V1 recognizes only these top-level entities:

- Part
- Relationship
- Map

No other entity types are allowed in V1.

---

## 2) Part Categories (V1 Closed Set)

A Part’s category must be exactly one of:

- Manager
- Firefighter
- Exile
- SelfLike
- Other

Notes:
- “Self” must NOT be represented as a Part.
- “SelfLike” is a category used as a label/badge in V1 representation; it does not authorize interpretive behavior.
- Category is always user-declared. No auto-classification.

---

## 3) Relationships (V1 Closed Set)

A Relationship’s type must be exactly one of:

- protects
- polarized_with

Pairing constraints (V1):
- protects relationships: between protectors and exiles
- polarized_with relationships: for other category pairings in V1

Notes:
- Relationship type is always user-declared. No auto-creation.
- No additional relationship labels exist in V1.

---

## 4) Non-Interpretation (Hard Boundary)

The system must not:
- interpret Parts or relationships
- infer meaning
- generate insights/summaries about what a map “means”
- suggest categories or relationships
- provide therapy guidance or analysis
- rank, score, or evaluate Parts

This is a recording instrument, not an authority.

---

## 5) Import/Export and Validation (V1)

- The binding JSON schema is: spec/IFS_Parts_Mapper_Minimal_Canonical_JSON_Schema_V1.md
- Import must reject unknown fields / keys and non-V1 schema versions.
- No autosave without explicit user action.
- Maps are user-owned and stored locally by default (per canonical specs).

---

## 6) Non-Canonical Warning

The file spec/IFS_PARTS_MAPPER_MASTER_SPEC.md is NOT canonical for V1 and must not be used to define:
- categories
- relationship types
- import/export fields
- validation rules

END V1 CANONICAL MODEL
