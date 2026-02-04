# IFS Parts Mapper — Specification Authority Map (V1)

This document defines the canonical hierarchy of specification documents.

When specifications conflict, the higher-precedence document always wins.

Implementations must follow this hierarchy strictly.

---

## Authority Hierarchy (Highest → Lowest)

### Level 1 — Errata (Highest Authority)

Binding corrections to the V1 specification.

Files:

- spec/IFS_Parts_Mapper_v1_Errata.md

Characteristics:

- May modify or correct model structure.
- May introduce minimal structural changes required for real-world usability.
- Overrides all other documents.

---

### Level 2 — Clarifications Patch

Binding clarifications that resolve ambiguity without expanding scope.

Files:

- spec/IFS_Parts_Mapper_V1_Clarifications_Patch.md

Characteristics:

- Clarifies meaning and intent of V1 rules.
- Must not contradict Errata.
- Must not introduce interpretive or therapeutic logic.

---

### Level 3 — Canonical Schema Definition

The authoritative structural definition of V1 data.

Files:

- spec/IFS_Parts_Mapper_Minimal_Canonical_JSON_Schema_V1.md

Characteristics:

- Defines exact JSON shape and allowed fields.
- Enforces strict validation and anti-drift rules.
- Must align with Errata and Clarifications.

---

### Level 4 — Model Contract

Operational interpretation of the canonical schema.

Files:

- spec/IFS_Parts_Mapper_V1_Model_Contract.md

Characteristics:

- Defines validation rules and model-layer behavior.
- Must align with higher-precedence documents.
- Must remain non-interpretive.

---

### Level 5 — Canonical Model Summary

Human-readable conceptual model.

Files:

- spec/V1_CANONICAL_MODEL.md

Characteristics:

- Summarizes the conceptual meaning of V1 entities.
- Must not contradict structural or contractual documents.
- Serves as explanatory guidance only.

---

### Level 6 — Master Specification

Comprehensive design narrative and constraints.

Files:

- spec/IFS_Parts_Mapper_Master_Spec_Hardened.md

Characteristics:

- Provides broader context and rationale.
- Must defer to all higher-precedence documents.
- Must not introduce new model structures.

---

### Level 7 — Supporting and Guidance Documents (Lowest Authority)

Non-binding reference materials.

Examples:

- spec/START_HERE.md
- spec/IFS_PARTS_MAPPER_MASTER_SPEC.md (explicitly non-canonical)
- README_DEV.md
- UI wireframes and design notes
- exploratory or draft documents

Characteristics:

- Guidance only.
- Must never override canonical specifications.
- May be incomplete or experimental.

---

## Conflict Resolution Rule

If two documents conflict:

1) Identify the higher-precedence document in this hierarchy.
2) Follow the higher-precedence document.
3) Treat the lower-precedence document as incorrect or outdated.

No implementation may rely on lower-precedence documents when higher-precedence documents exist.

---

## V1 Scope Boundary

All documents in this hierarchy enforce the V1 scope:

The system must NOT:

- interpret Parts or relationships
- infer meaning, intent, or diagnosis
- generate insights, summaries, or recommendations
- auto-classify or auto-link Parts
- rank, score, or evaluate Parts
- provide therapeutic guidance
- apply AI/ML to interpret Maps

The system must remain:

- non-clinical
- phenomenological
- representational
- privacy-first
- user-owned

---

END SPEC AUTHORITY MAP
