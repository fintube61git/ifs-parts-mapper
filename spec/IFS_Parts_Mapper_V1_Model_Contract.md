# IFS Parts Mapper (V1) — Model Contract

This document defines the binding contract between the V1 specification and the implementation of the core data model and validation layer.

This is a spec artifact, not code.
It must be treated as authoritative for V1 model behavior.

If any implementation contradicts this document, the implementation is wrong.
If any other spec contradicts this document, the higher-precedence rules in Errata and Clarifications apply.

---

## 0) Scope of This Contract

This contract applies ONLY to the model layer:

Included:

* Data structures
* Validation rules
* Canonical JSON import/export shape
* Deterministic behavior and constraints

Explicitly excluded:

* UI logic (Streamlit)
* Graph rendering (pyvis / Graphviz)
* Persistence beyond explicit JSON import/export
* Analytics, inference, ranking, summaries, or insights

The model layer must remain framework-agnostic and purely structural.

---

## 1) Canonical Domain Objects

### 1.1 Part

Required fields:

* id: string
* label: string
* category: string

Allowed categories (V1 only):

* Manager
* Firefighter
* Exile
* SelfLike
* Other

Optional fields (and only these):

* subtype: string
* intensity: integer (0–10 inclusive)
* notes: string (≤ 280 characters)
* tags: list of strings

Hard constraints:

* label must be non-empty after trimming
* category must be one of the allowed values
* category must never be "Self"
* unknown fields are forbidden

---

### 1.2 Relationship

Required fields:

* id: string
* source_part_id: string
* target_part_id: string
* type: string

Allowed types (V1 only):

* protects
* polarized_with

Optional fields (and only these):

* strength: integer (0–10 inclusive)
* notes: string (≤ 280 characters)

Hard constraints:

* source_part_id != target_part_id (no self-loops)
* both endpoints must exist in parts
* unknown fields are forbidden

Duplicate rules:

* protects: duplicates forbidden for identical (source, target, type)
* polarized_with: undirected; stored once; duplicates forbidden for unordered pairs

Canonicalization rule:

* polarized_with endpoints must be ordered deterministically before storage

---

### 1.3 Trailhead

Trailhead object must exist even if empty.

Required fields:

* trigger: string (may be empty)
* dominant_protector_patterns: list of strings
* core_vulnerability_themes: list of strings

Hard constraints:

* trigger must be a string (structured trigger objects forbidden in V1)
* unknown fields are forbidden

---

### 1.4 Map

Required fields:

* schema_version: string
* map_id: string
* title: string
* parts: list of Part
* relationships: list of Relationship
* trailhead: Trailhead

schema_version rules:

* export must emit "1.0.0"
* import must accept only 1.x.x

Map-level constraints:

* part ids must be unique
* relationship ids must be unique
* deleting a part deletes all related relationships
* unknown top-level fields are forbidden

---

## 2) Model Operations (Conceptual API)

The model layer must support the following operations:

Parts:

* add_part
* update_part
* delete_part (with cascading relationship deletion)
* get_part

Relationships:

* add_relationship
* update_relationship
* delete_relationship
* get_relationship

Bulk linking (V1 only):

* bulk_link_protects(protector → multiple exiles)
* bulk_link_protects_reverse(exile ← multiple protectors)

Bulk linking constraints:

* applies only to protects relationships
* duplicates must be skipped
* polarized_with is excluded from bulk linking

---

## 3) Validation Contract

Validation must enforce:

Field-level validation:

* required fields present
* correct data types
* allowed values only
* length limits for notes

Cross-object validation:

* referential integrity between parts and relationships
* duplicate prevention
* polarization semantics
* uniqueness of ids

Import behavior:

* unknown fields must cause import failure
* all structural violations must be reported

Error handling:

* error messages must not include user content
* labels, notes, and trailhead text must never appear in logs or exceptions

---

## 4) Canonical JSON Contract

Export behavior:

* output must match canonical JSON shape exactly
* no inferred or derived fields
* schema_version fixed to "1.0.0"

Import behavior:

* strict schema enforcement
* rejection of unknown fields
* enforcement of all constraints

No persistence occurs at the model layer.

---

## 5) Anti-Drift Guarantees

The model layer must make the following impossible or invalid:

* creation of a Self node
* introduction of new relationship types
* implicit meaning, scoring, ranking, or inference
* persistence outside explicit JSON import/export
* leakage of user content into logs or errors

---

## 6) Compliance Criteria

The model layer is compliant with V1 only if:

* all constraints in this contract are enforced
* import/export round-trip is lossless
* privacy constraints are upheld
* no interpretive or diagnostic features exist
* system behavior remains purely structural

---

## 7) Authority and Precedence

For V1 interpretation, precedence is:

1. Errata file
2. Clarifications Patch
3. Minimal Canonical JSON Schema
4. This Model Contract
5. Master Spec Hardened
6. All other spec documents

If conflicts exist, higher-precedence documents win.
