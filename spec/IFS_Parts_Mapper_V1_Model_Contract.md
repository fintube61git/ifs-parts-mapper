# IFS Parts Mapper (V1) — Model Contract

This document defines the binding contract between the V1 specification and the implementation of the core data model and validation layer.

This is a spec artifact, not code.
It must be treated as authoritative for V1 model behavior.

If any implementation contradicts this document, the implementation is wrong.
If any other spec contradicts this document, the higher-precedence rules in Errata and Clarifications apply.

---

## 0) Scope of This Contract

This contract applies to:

* Canonical data structures
* Validation rules
* Canonical JSON import/export (the importable artifact)
* Deterministic behavior and constraints

This contract also defines the model-layer requirements that support share/print export fidelity (without defining UI rendering).

Explicitly excluded:

* UI logic (Streamlit)
* Graph rendering implementation details (pyvis / Graphviz / canvas libs)
* Persistence beyond explicit user actions
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
* Other

Optional fields (and only these):

* subtype: string
* intensity: integer (0–10 inclusive)
* notes: string (≤ 280 characters)
* tags: list of strings
* self_like: boolean
* avatar: object (presentation-only)
* position: object (geometry-only)

self_like rules:

* self_like is a boolean badge that may apply to any Part.
* If self_like is absent, it is treated as false.
* self_like must not create or imply a literal "Self" Part.
* self_like must not trigger inference, interpretation, ranking, or guidance.
* self_like is always user-declared.

avatar shape:

{
  "kind": "person" | "animal" | "symbol",
  "token": string,
  "presentation": "neutral" | "woman" | "man" (optional; only when kind="person"),
  "tone": integer (0–5 inclusive; only when kind="person")
}

avatar rules:

* avatar is user-declared only (no inference).
* token must refer to a stable identifier from an open-source icon library.
* presentation is allowed only when kind="person".
* tone scale is neutral:
  * 0 = unspecified/default
  * 1–5 = increasing darkness
* tone must be 0 or absent when kind != "person".
* avatar must not affect category, relationships, validation, or meaning.
* avatar must not be used to infer psychological, demographic, or clinical attributes.

position shape:

{
  "x": number,
  "y": number
}

position rules:

* position is geometry-only metadata used to preserve user-chosen layout.
* position must be user-driven (e.g., explicit drag/move actions).
* If position is absent, the Part remains valid.
* If position is present:
  * x must be a number
  * y must be a number
* position must not affect category, relationships, or meaning.
* position must not trigger inference or interpretation.

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

* export must emit "1.0.1"
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

Layout support (V1):

* update_part_position(part_id, x, y)

Rules:
- position updates must result only from explicit user actions (e.g., drag/move)
- no background autosave of position without explicit user action to save/export

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
* numeric ranges for intensity/strength
* structural validity for avatar and position

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

## 4) Import/Export Contract (V1)

### 4.1 Canonical Map Export (Importable JSON)

Export behavior:

* output must match canonical JSON shape exactly
* no inferred or derived fields
* schema_version fixed to "1.0.1"
* must include all user-declared data, including avatar and position (when present)

Import behavior:

* strict schema enforcement
* rejection of unknown fields
* enforcement of all constraints
* import must accept only canonical JSON maps (1.x.x)

The importer must not accept share/print artifacts.

---

### 4.2 Share/Print Export Support (Non-Importable)

V1 requires support for a user-initiated share/print export artifact.

Rules:

* share/print export must be PDF (V1 primary)
* share/print export is NOT importable and must not be accepted by the importer
* share/print export must be a faithful representation of the on-screen map, including:
  - node positions (from Part.position, when present)
  - node labels
  - categories
  - relationship lines and directionality
  - relationship types (protects / polarized_with)
  - avatars (when present)
  - map title and a minimal legend
* share/print export must not add meaning, summaries, insights, advice, or recommendations

This contract does not prescribe the rendering engine; it prescribes fidelity and non-interpretation.

---

## 5) Anti-Drift Guarantees

The model layer must make the following impossible or invalid:

* creation of a Self node
* introduction of new relationship types
* implicit meaning, scoring, ranking, or inference
* persistence outside explicit user actions
* leakage of user content into logs or errors
* acceptance of non-canonical artifacts as importable data

---

## 6) Compliance Criteria

The system is compliant with V1 only if:

* all constraints in this contract are enforced
* canonical JSON import/export round-trip is lossless
* share/print export is faithful and non-interpretive
* privacy constraints are upheld
* no interpretive or diagnostic features exist
* user ownership and explicit action are preserved

---

## 7) Authority and Precedence

For V1 interpretation, precedence is:

1. Errata file
2. Clarifications Patch
3. Minimal Canonical JSON Schema
4. This Model Contract
5. V1 Canonical Model
6. Master Spec Hardened
7. All other documents

If conflicts exist, higher-precedence documents win.
