# IFS Parts Mapper V1 — Errata (Binding)

This file records binding corrections to the V1 specification.
It has highest precedence in the authority hierarchy.

If any other specification conflicts with this document, this document wins.

---

## Errata 001 — SelfLike is a Badge, Not a Category

Problem:
SelfLike was previously listed as a Part category, but conceptually represents
a quality that may apply to any Part rather than a distinct Part type.

Resolution (V1 Final):

1) Remove "SelfLike" from the Part.category allowed values.
2) Add an optional boolean field to Part: self_like.

Rules:

- self_like: boolean (default false if absent)
- self_like must not create or imply a literal "Self" Part.
- self_like must not trigger inference, interpretation, ranking, or guidance.
- self_like is always user-declared.

Rationale:

This preserves the prohibition against representing "Self" as a Part while allowing
users to mark Parts that phenomenologically resemble Self-like qualities without
reclassifying their functional role.

---

## Errata 002 — Portable Avatar Metadata for Parts (V1)

Problem:
V1 lacked a portable mechanism for user-selected visual externalization of Parts.
UI-only avatars do not survive export or sharing.

Resolution (V1 Final):

Add an optional Part field: avatar.

avatar is presentation-only metadata and must not be used for inference,
classification, interpretation, ranking, or therapeutic guidance.

avatar shape (V1):

{
  "kind": "person" | "animal" | "symbol",
  "token": string,
  "presentation": "neutral" | "woman" | "man" (optional; only when kind="person"),
  "tone": integer (0–5 inclusive; only when kind="person")
}

Rules:

- avatar is user-declared only.
- token must refer to a stable identifier from an open-source icon library.
- presentation is allowed only when kind="person".
- tone scale is neutral:
  - 0 = unspecified/default
  - 1–5 = increasing darkness
- tone must be 0 or absent when kind != "person".
- avatar must not affect category, relationships, validation, or meaning.
- avatar must not be used to infer psychological, demographic, or clinical attributes.

Rationale:

This enables portable visual externalization while preserving the non-interpretive,
privacy-first nature of the system and avoiding ontology creep.

---

## Errata 003 — Schema Version Update

Problem:
The Part structure changed due to Errata 001 and Errata 002, requiring a schema update.

Resolution (V1 Final):

- Export must emit schema_version = "1.0.1".
- Import must continue to accept only 1.x.x schema versions.
- Implementations must reject schema versions outside the 1.x.x range.

Rationale:

This preserves backward compatibility within the V1 family while ensuring that
structural changes are explicitly versioned.

---

## Errata 004 — Non-Interpretation Guarantee (Reaffirmed)

The introduction of self_like and avatar does not alter the core identity of the system.

The system must NOT:

- interpret Parts or relationships
- infer meaning or intent
- generate insights or summaries
- suggest categories, relationships, or avatars
- rank, score, or evaluate Parts
- provide therapeutic guidance

All such behavior remains explicitly out of scope for V1.

---

## Errata 005 — Part Position (Geometry) for Freeform Drag Layout (V1)

Problem:
A representational mapping tool must allow users to externalize lived structure.
Without storing user-chosen node positions, map layout cannot be preserved across
sessions and share/print exports cannot match what the user saw on screen.

Resolution (V1 Final):

Add an optional Part field: position.

position is purely geometric metadata and must not be used for inference,
classification, interpretation, ranking, or therapeutic guidance.

position shape (V1):

{
  "x": number,
  "y": number
}

Rules:

- position is user-driven (via explicit drag/move actions).
- position must not be auto-interpreted as psychological meaning.
- If position is absent, the Part is still valid.
- Implementations may compute a default initial position, but must not autosave
  position changes unless initiated by explicit user action.
- position must not affect category, relationships, or validation beyond type checking.

Rationale:

This preserves user ownership of spatial representation while keeping the system
strictly non-interpretive.

---

## Errata 006 — Dual Export Artifacts (Importable JSON + Share/Print) (V1)

Problem:
Users need export files that are:
1) importable for future editing, and
2) understandable and shareable for humans who do not have the app.

A raw JSON file alone is not a usable share/print artifact for typical users.

Resolution (V1 Final):

A single user-initiated Export action must be capable of producing:

A) Canonical Map Export (Importable)
- Format: strict canonical JSON (schema_version "1.0.1")
- Purpose: re-open/edit in the app
- This is the ONLY importable artifact.

B) Share/Print Export (Human-readable)
- Format: PDF (V1 primary share/print artifact)
- Purpose: printing/sharing with people who do not have the app
- Must visually match, as closely as possible, what the user saw on screen, including:
  - node positions (from Part.position, when present)
  - node labels
  - categories
  - relationship lines and directionality
  - relationship types (protects / polarized_with)
  - avatars (when present)
  - map title and a minimal legend

Rules:

- Share/print export must be a faithful representation, not an interpretation.
- Share/print export must not add summaries, insights, advice, meaning, or recommendations.
- Share/print export is NOT importable and must not be accepted by the importer.
- All exports must result only from explicit user action (no autosave).

Rationale:

This preserves strict canonical import/export while producing a usable artifact
for real-world sharing and printing without introducing interpretive drift.

---

END ERRATA
