# V1 Truth Table — Canonical Model & Validation (IFS Parts Mapper)

This file is a compact, implementation-facing truth table for V1.

It defines what is:
- required
- optional
- allowed
- forbidden

Authority order reference:
1) Errata
2) Clarifications Patch
3) Minimal Canonical JSON Schema
4) Model Contract
5) V1 Canonical Model
6) Master Spec Hardened

If conflicts exist, higher-precedence documents win.

---

## A) Top-Level Map Object (Required)

Required keys (MUST exist):
- schema_version (string)
- map_id (string)
- title (string)
- parts (array)
- relationships (array)
- trailhead (object)

Export rule:
- schema_version MUST be exactly "1.0.1"

Import rule:
- schema_version MUST match 1.x.x only

Forbidden:
- Any unknown top-level key (IMPORT FAIL)

---

## B) trailhead (Required Object)

Required keys (MUST exist, even if empty):
- trigger (string; may be empty)
- dominant_protector_patterns (array of strings)
- core_vulnerability_themes (array of strings)

Forbidden:
- trigger as object/array/number (IMPORT FAIL)
- any unknown key inside trailhead (IMPORT FAIL)

---

## C) Part Object (Element of parts[])

### C1) Required fields
- id: string (non-empty after trim)
- label: string (non-empty after trim)
- category: string (MUST be one of allowed values)

Allowed category values (V1 only):
- "Manager"
- "Firefighter"
- "Exile"
- "Other"

Explicitly forbidden:
- "Self"
- "SelfLike" (SelfLike is NOT a category)

Unknown keys in Part:
- forbidden (IMPORT FAIL)

---

### C2) Optional fields (ONLY these may appear)
- subtype: string
- intensity: integer (0–10 inclusive)
- notes: string (≤ 280 characters)
- tags: array of strings
- self_like: boolean
- avatar: object (presentation-only)
- position: object (geometry-only)

---

### C3) self_like (Optional badge)
- type: boolean
- if absent: treated as false
- MUST NOT imply or create a literal Self Part
- MUST NOT drive inference/interpretation/ranking

---

### C4) avatar (Optional presentation metadata)

avatar shape:
- kind: "person" | "animal" | "symbol"
- token: string (non-empty)
- presentation: "neutral" | "woman" | "man" (optional; only when kind="person")
- tone: integer 0–5 (optional; only when kind="person")

Rules:
- avatar is user-declared only
- token must reference a stable identifier from an open-source icon library
- avatar MUST NOT affect category, relationships, or meaning

Constraints:
- if kind != "person":
  - tone MUST be 0 or absent
  - presentation MUST be absent or ignored

---

### C5) position (Optional geometry metadata)

position shape:
- x: number
- y: number

Rules:
- position preserves user-chosen spatial layout (freeform drag)
- position is user-declared only
- position MUST NOT affect category, relationships, or meaning
- x and y MUST be numbers if present

---

## D) Relationship Object (Element of relationships[])

### D1) Required fields
- id: string (non-empty after trim)
- source_part_id: string
- target_part_id: string
- type: string (MUST be one of allowed values)

Allowed relationship types (V1 only):
- "protects"
- "polarized_with"

Unknown keys in Relationship:
- forbidden (IMPORT FAIL)

---

### D2) Optional fields (ONLY these may appear)
- strength: integer (0–10 inclusive)
- notes: string (≤ 280 characters)

---

### D3) Hard constraints
- source_part_id != target_part_id (no self-loops)
- source_part_id and target_part_id MUST refer to existing Part ids
- no duplicate relationship ids

Duplicate prevention:
- protects: duplicates forbidden for identical (source_part_id, target_part_id, type)
- polarized_with: undirected; stored once
  - A↔B must not be duplicated as B↔A
  - canonical ordering must treat (A,B) same as (B,A)

---

## E) Map-Wide Integrity Rules

- Part ids unique
- Relationship ids unique
- Deleting a Part deletes its Relationships (cascade)
- No inference, no auto-linking, no auto-classification
- No autosave without explicit user action
- Errors/logs MUST NOT include user content (labels/notes/trailhead text)

---

## F) Import vs Share Export (V1)

### F1) Canonical Map Export (Importable)

Format:
- strict canonical JSON (schema_version "1.0.1")

Rules:
- ONLY this artifact is importable
- must include avatar and position when present
- unknown fields cause import failure

Example filename:
- MyMap.ifspm.json

---

### F2) Share / Print Export (Human Artifact)

Format:
- PDF (V1 primary)

Rules:
- NOT importable
- must visually match the on-screen map, including:
  - node positions (from Part.position)
  - labels
  - categories
  - relationship lines and directionality
  - relationship types
  - avatars
  - title and minimal legend
- must not add meaning, summaries, insights, advice, or recommendations

Example filename:
- MyMap.share.pdf

---

## G) Valid vs Invalid Examples

### G1) Valid Part (minimal)

{
  "id": "p1",
  "label": "Planner",
  "category": "Manager"
}

---

### G2) Valid Part (with SelfLike + avatar + position)

{
  "id": "p2",
  "label": "Calm Witness",
  "category": "Other",
  "self_like": true,
  "avatar": {
    "kind": "person",
    "token": "office_worker",
    "presentation": "neutral",
    "tone": 3
  },
  "position": {
    "x": 320,
    "y": 180
  }
}

---

### G3) Invalid Part (SelfLike as category) — FAIL

{
  "id": "p3",
  "label": "Self-ish one",
  "category": "SelfLike"
}

---

### G4) Valid Relationship (protects)

{
  "id": "r1",
  "source_part_id": "p1",
  "target_part_id": "p2",
  "type": "protects"
}

---

### G5) Invalid Relationship (unknown type) — FAIL

{
  "id": "r2",
  "source_part_id": "p1",
  "target_part_id": "p2",
  "type": "influences"
}

---

### G6) Invalid Part (position wrong type) — FAIL

{
  "id": "p4",
  "label": "Mover",
  "category": "Manager",
  "position": {
    "x": "left",
    "y": "top"
  }
}

---

### G7) Invalid: Unknown key anywhere — FAIL

Any extra key not explicitly allowed in this truth table must cause import rejection.

---

END V1 TRUTH TABLE
