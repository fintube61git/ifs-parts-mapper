# Minimal Canonical JSON Schema (Human-Readable, V1)

This defines the **canonical V1 JSON shape** the data model must match.
It is intentionally human-readable and spec-locked.

This document is binding for V1 canonical JSON import/export.

NOTE:
- This schema defines the importable/exportable JSON artifact only.
- Share/print exports (PDF) are separate non-importable artifacts and are governed by Errata.

---

## V1 Freeze Decision (Non-Negotiable)

### trailhead.trigger shape (V1)
**Frozen for V1:** `trigger` is a **string** (may be empty).

Rationale:
- Lowest ambiguity and lowest drift risk
- Minimal schema surface area
- Avoids pressure toward tag vocabularies, suggestion systems, or “smartness”

No alternate trigger shapes are permitted in V1.

---

## Top-Level Map (Required Object)

Required keys (must exist):
- schema_version
- map_id
- title
- parts
- relationships
- trailhead

Rules:
- schema_version must be "1.0.1" on export
- import must accept schema_version 1.x.x only
- unknown top-level keys are rejected (anti-drift)

---

## trailhead (Required Object)

Required keys (must exist):
- trigger
- dominant_protector_patterns
- core_vulnerability_themes

Required shapes (V1):
- trigger: string (may be empty)
- dominant_protector_patterns: [string]
- core_vulnerability_themes: [string]

Example:
{
  "trigger": "",
  "dominant_protector_patterns": [],
  "core_vulnerability_themes": []
}

Rules:
- All keys must exist even if empty
- Unknown keys are rejected (anti-drift)

---

## parts (Required Array)

Each element is a Part object.

Required keys:
- id (string)
- label (string)
- category (string)

Optional keys:
- subtype (string)
- intensity (integer; 0–10 inclusive)
- notes (string; ≤ 280 chars)
- tags ([string])
- self_like (boolean)
- avatar (object; presentation-only)
- position (object; geometry-only)

Allowed category values (V1 only):
- "Manager"
- "Firefighter"
- "Exile"
- "Other"

self_like rules (V1):
- self_like is a boolean badge that may apply to any Part
- if absent, it is treated as false
- self_like must not be used to infer meaning or create a "Self" Part

avatar shape (V1):
{
  "kind": "person" | "animal" | "symbol",
  "token": string,
  "presentation": "neutral" | "woman" | "man" (optional; only when kind="person"),
  "tone": integer (0–5 inclusive; only when kind="person")
}

avatar rules (V1):
- avatar is user-declared only (no inference)
- token must refer to a stable identifier from an open-source icon library
- presentation is allowed only when kind="person"
- tone scale is neutral:
  - 0 = unspecified/default
  - 1–5 = increasing darkness
- tone must be 0 or absent when kind != "person"
- avatar must not affect category or relationships (presentation-only)

position shape (V1):
{
  "x": number,
  "y": number
}

position rules (V1):
- position is geometry-only metadata (no inference)
- position is user-driven (e.g., drag/move)
- if position is absent, the Part is still valid
- x and y must be numbers if present
- position must not affect category or relationships

Hard rules:
- id must be non-empty after trimming
- label must be non-empty after trimming
- category must be one of the allowed values
- category must never be "Self"
- unknown keys in a Part object are rejected (anti-drift)

---

## relationships (Required Array)

Each element is a Relationship object.

Required keys:
- id (string)
- source_part_id (string)
- target_part_id (string)
- type (string)

Optional keys (allowed by spec):
- strength (integer; 0–10 inclusive)
- notes (string; ≤ 280 chars)

Allowed type values (V1 only):
- "protects" (directional)
- "polarized_with" (undirected; stored once)

Hard rules:
- id must be non-empty after trimming
- source_part_id != target_part_id (no self-loops)
- source_part_id and target_part_id must refer to existing Part ids
- type must be one of the allowed values
- unknown keys in a Relationship object are rejected (anti-drift)

Duplicate rules:
- protects duplicates are not allowed (same source_part_id + target_part_id + type)
- polarized_with is undirected and stored once:
  - Never store both A→B and B→A
  - Canonical form must treat (A,B) the same as (B,A)

---

## Map-Wide Integrity Rules (V1)

- Part ids must be unique
- Relationship ids must be unique
- Deleting a Part deletes its Relationships
- No self-loops
- No duplicates (as defined above)
- trailhead object must exist and contain all required keys (even if empty)

---

## Import/Export Note (V1)

This schema defines the canonical JSON map file (importable).

Share/print exports (PDF) are separate artifacts:
- Not importable
- Must faithfully represent the on-screen map (see Errata)

