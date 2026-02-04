# V1 Canonical Model — IFS Parts Mapper

This document summarizes the canonical V1 conceptual model.

It is a human-readable reference layer that must remain consistent with:

1) Errata
2) Clarifications Patch
3) Minimal Canonical JSON Schema
4) Model Contract

If conflicts exist, higher-precedence documents win.

---

## Core Principle

The system does not model the psyche.

It models what the user chooses to represent.

The application is a recording instrument, not an authority.

No interpretation, inference, ranking, or therapeutic guidance is permitted.

---

## Core Entities (V1)

### Part

A Part is a user-declared element of experience.

Each Part has:

Required:
- id
- label
- category

Allowed categories (V1):
- Manager
- Firefighter
- Exile
- Other

Optional attributes:
- subtype (short descriptor)
- intensity (0–10 integer)
- notes (≤ 280 characters)
- tags (list of strings)
- self_like (boolean badge)
- avatar (presentation-only metadata)
- position (geometry-only metadata)

---

### SelfLike (Badge, Not a Part Type)

SelfLike is not a Part category.

SelfLike is a boolean badge that may apply to any Part.

Rules:
- self_like = true marks a Part as Self-like in quality.
- self_like must not create or imply a literal “Self” Part.
- Self must never be represented as a Part.
- SelfLike does not authorize interpretive behavior.
- SelfLike is always user-declared.

---

### Avatar (Presentation Metadata)

avatar is optional, presentation-only metadata attached to a Part.

avatar shape:

- kind: "person" | "animal" | "symbol"
- token: stable identifier from an open-source icon library
- presentation: "neutral" | "woman" | "man" (only when kind="person")
- tone: integer 0–5 (only when kind="person")

Rules:

- avatar is user-declared only.
- avatar must not affect category, relationships, or validation.
- avatar must not be used to infer psychological, demographic, or clinical meaning.
- tone scale is neutral:
  - 0 = unspecified
  - 1–5 = increasing darkness
- tone must be 0 when kind != "person".

Purpose:

Avatars support visual externalization without introducing interpretation.

---

### Position (Geometry Metadata)

position is optional, geometry-only metadata attached to a Part.

position shape:

- x: number
- y: number

Rules:

- position preserves user-chosen spatial layout (e.g., freeform drag).
- position is user-driven and must not be interpreted as meaning by the system.
- position must not affect category, relationships, or validation beyond type checking.
- If position is absent, the Part remains valid.

Purpose:

Position enables faithful re-opening of maps and faithful share/print exports.

---

### Relationship

A Relationship connects two Parts.

Allowed relationship types (V1):
- protects (directional)
- polarized_with (undirected)

Rules:

- Relationship types are user-declared only.
- No additional relationship types are permitted in V1.
- No inference or auto-creation of relationships is allowed.

Optional attributes:
- strength (0–10 integer)
- notes (≤ 280 characters)

---

### Map

A Map is a container for Parts and Relationships.

Each Map includes:
- schema_version
- map_id
- title
- parts
- relationships
- trailhead

Maps are user-owned and portable.

---

### Trailhead

Trailhead is contextual metadata for a Map.

Required fields:
- trigger (string, may be empty)
- dominant_protector_patterns (list of strings)
- core_vulnerability_themes (list of strings)

Rules:

- Trailhead fields are user-declared only.
- No interpretation or inference is permitted.
- Structured trigger objects are forbidden in V1.

---

## Import/Export Artifacts (V1)

A user-initiated Export action must be capable of producing:

1) Canonical Map Export (Importable JSON)
- Strict canonical JSON (schema_version "1.0.1")
- Purpose: re-open/edit in the app
- The only importable artifact

2) Share/Print Export (Human-readable PDF)
- Not importable
- Purpose: print/share with people who do not have the app
- Must visually match, as closely as possible, what the user saw on screen, including:
  - node positions (from Part.position, when present)
  - node labels
  - categories
  - relationship lines and directionality
  - relationship types
  - avatars (when present)
  - title and minimal legend
- Must not add meaning, summaries, insights, advice, or recommendations

---

## Hard Boundaries (V1)

The system must NOT:

- interpret Parts or relationships
- infer meaning or intent
- generate insights or summaries
- suggest categories, relationships, avatars, or positions
- auto-classify or auto-link Parts
- rank or evaluate Parts
- provide therapeutic guidance
- autosave without explicit user action
- apply AI/ML to interpret Maps

If a feature answers “What does this mean?”, it is out of scope for V1.

---

## Summary of V1 Model Structure

Parts:
- functional category (Manager / Firefighter / Exile / Other)
- optional SelfLike badge
- optional visual avatar
- optional geometry position (x,y)
- optional intensity, notes, tags, subtype

Relationships:
- protects
- polarized_with

Maps:
- user-owned
- portable via canonical JSON
- shareable via faithful PDF export
- strictly validated
- non-interpretive

END V1 CANONICAL MODEL
