# IFS Parts Mapper V1 — Model-to-Code Blueprint

Purpose: Map the frozen V1 Model Contract to implementation responsibilities.
Scope: MODEL LAYER ONLY (models.py, validate.py, io_json.py).
Rule: If code contradicts this document or the Model Contract, the code is wrong.

---

## 1) File Responsibilities (Non-Negotiable)

models.py — Structural definitions only.
Defines canonical data structures. No inference, no persistence, no UI logic.

Objects:
- Part
- Relationship
- Trailhead
- Map

Rules:
- Only fields explicitly allowed by the Model Contract exist.
- No computed fields, no semantic defaults.
- No side effects.

---

validate.py — All constraints and enforcement.

Part validation:
Required:
- id: string
- label: string (trimmed, non-empty)
- category: one of {Manager, Firefighter, Exile, SelfLike, Other}

Optional:
- subtype: string
- intensity: integer 0–10
- notes: string ≤ 280 chars
- tags: list of strings

Forbidden:
- category == "Self"
- unknown fields

---

Relationship validation:
Required:
- id: string
- source_part_id: string
- target_part_id: string
- type: one of {protects, polarized_with}

Optional:
- strength: integer 0–10
- notes: string ≤ 280 chars

Constraints:
- source_part_id != target_part_id
- endpoints must exist in parts
- unknown fields forbidden

Duplicate rules:
- protects: no duplicate (source, target, type)
- polarized_with: undirected; stored once; no duplicates for unordered pairs

Canonicalization:
- polarized_with endpoints ordered deterministically before storage

---

Trailhead validation:
Required:
- trigger: string (may be empty)
- dominant_protector_patterns: list of strings
- core_vulnerability_themes: list of strings

Constraints:
- trigger must be string (no structured objects)
- unknown fields forbidden

---

Map validation:
Required:
- schema_version: string
- map_id: string
- title: string
- parts: list of Part
- relationships: list of Relationship
- trailhead: Trailhead

Constraints:
- export schema_version = "1.0.0"
- import accepts only 1.x.x
- part IDs unique
- relationship IDs unique
- deleting a part deletes related relationships
- unknown top-level fields forbidden

---

Privacy rules:
- validation errors must not include user content
- labels, notes, trailhead text must never appear in logs or exceptions

---

io_json.py — Canonical import/export only.

Export:
- canonical JSON shape exactly
- schema_version fixed to "1.0.0"
- no derived fields

Import:
- strict schema enforcement
- unknown fields cause failure
- all validation rules applied

Persistence rule:
- no persistence beyond explicit JSON import/export

---

## 2) Anti-Drift Guarantees

The model layer must make impossible:
- creation of a "Self" node
- new relationship types
- inference, scoring, ranking, interpretation
- persistence outside JSON import/export
- leakage of user content into logs or errors

---

## 3) Compliance Criteria

The model layer is V1-compliant only if:
- all constraints are enforced
- import/export round-trip is lossless
- no interpretive logic exists
- schema drift is impossible
