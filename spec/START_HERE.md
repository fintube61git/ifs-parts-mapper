# START HERE — IFS Parts Mapper V1 (Canonical Entry Point)

This file is the mandatory entry point for anyone working on the IFS Parts Mapper project.

If you do not understand this file, do not modify the system.

---

## 1) Core Identity of the System

The IFS Parts Mapper is:

- non-clinical
- phenomenological
- representational
- non-interpretive
- privacy-first
- user-owned

The system records what the user chooses to represent.

The system must never act as an authority.

---

## 2) Canonical Authority Hierarchy (Non-Negotiable)

When documents conflict, follow this order:

1) spec/IFS_Parts_Mapper_v1_Errata.md
2) spec/IFS_Parts_Mapper_V1_Clarifications_Patch.md
3) spec/IFS_Parts_Mapper_Minimal_Canonical_JSON_Schema_V1.md
4) spec/IFS_Parts_Mapper_V1_Model_Contract.md
5) spec/V1_CANONICAL_MODEL.md
6) spec/IFS_Parts_Mapper_Master_Spec_Hardened.md
7) All other documents (guidance only)

If implementation conflicts with any of the above, the implementation is wrong.

---

## 3) Canonical V1 Model (Single Source of Truth)

### 3.1 Part Categories (Closed Set)

Allowed Part categories in V1:

- Manager
- Firefighter
- Exile
- Other

SelfLike is NOT a category.

Self must NOT be represented as a Part.

---

### 3.2 SelfLike (Badge, Not a Category)

SelfLike is a boolean badge on a Part:

- Part.self_like = true | false

Rules:

- SelfLike may apply to any Part.
- SelfLike must never imply a literal Self Part.
- SelfLike must never trigger interpretation, inference, ranking, or guidance.
- SelfLike is always user-declared.

---

### 3.3 Avatar (Presentation Metadata)

Parts may optionally include avatar metadata.

avatar is presentation-only and must never affect meaning or logic.

avatar shape (V1):

{
  "kind": "person" | "animal" | "symbol",
  "token": string,
  "presentation": "neutral" | "woman" | "man" (only when kind="person"),
  "tone": integer (0–5 inclusive; only when kind="person")
}

Rules:

- token must be a stable identifier from an open-source icon library.
- avatar is user-declared only.
- avatar must not affect category, relationships, or validation.
- avatar must not be used to infer psychological, demographic, or clinical meaning.
- tone scale is neutral:
  - 0 = unspecified
  - 1–5 = increasing darkness
- tone must be 0 when kind != "person".

---

### 3.4 Position (Geometry Metadata)

Parts may optionally include position metadata.

position is geometry-only and must never affect meaning or logic.

position shape (V1):

{
  "x": number,
  "y": number
}

Rules:

- position preserves user-chosen spatial layout (freeform drag).
- position is user-declared only.
- position must not be interpreted as meaning.
- position must not affect category or relationships.
- absence of position does not invalidate a Part.

---

### 3.5 Relationships (Closed Set)

Allowed relationship types in V1:

- protects (directional)
- polarized_with (undirected)

No additional relationship types are permitted in V1.

Relationships are user-declared only.

No inference or auto-linking is allowed.

---

## 4) Canonical Import / Export Model (V1)

### 4.1 Canonical Map Export (Importable)

Purpose:
- Save and re-open maps inside the application.

Format:
- strict canonical JSON (schema_version "1.0.1")

Rules:

- This is the ONLY importable artifact.
- Must include all user-declared data (including avatar and position when present).
- Must reject unknown fields on import.

Example filename:
- MyMap.ifspm.json

---

### 4.2 Share / Print Export (Human Artifact)

Purpose:
- Share or print maps for people who do not have the app.

Format:
- PDF (V1 primary)

Rules:

- NOT importable.
- Must visually match, as closely as possible, what the user saw on screen, including:
  - node positions
  - node labels
  - categories
  - relationship lines and directionality
  - relationship types
  - avatars (when present)
  - title and minimal legend
- Must not add meaning, summaries, insights, advice, or recommendations.

Example filename:
- MyMap.share.pdf

---

## 5) Hard Boundaries (V1)

The system must NOT:

- interpret Parts or relationships
- infer meaning, intent, or diagnosis
- generate insights, summaries, or recommendations
- auto-classify or auto-link Parts
- suggest categories, relationships, avatars, or positions
- rank or evaluate Parts
- provide therapeutic guidance
- autosave without explicit user action
- apply AI/ML to interpret Maps

If a feature answers “What does this mean?”, it is out of scope for V1.

---

## 6) Implementation Discipline Rule

Before writing or modifying code, developers must verify:

- Part categories remain Manager / Firefighter / Exile / Other.
- SelfLike exists only as Part.self_like (boolean).
- avatar exists only as presentation metadata.
- position exists only as geometry metadata.
- dual export model is preserved (JSON + PDF).
- No interpretive or therapeutic logic is added.
- User ownership and explicit action are preserved.

If any of the above cannot be proven, do not implement the change.

---

END START HERE
