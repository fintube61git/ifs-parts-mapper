# IFS Parts Mapper V1 — Clarifications Patch (Binding)

This document clarifies ambiguous areas of the V1 specification.

This file does not expand scope beyond V1.
It resolves wording conflicts and prevents interpretive drift.

Precedence order:

1) Errata
2) This Clarifications Patch
3) Minimal Canonical JSON Schema
4) Model Contract
5) V1 Canonical Model
6) Master Spec Hardened
7) All other documents

If conflicts exist, higher-precedence documents win.

---

## Clarification 001 — Parts vs Self

Self must never be represented as a Part.

Parts are user-declared representational elements.

SelfLike is not a Part category.
SelfLike is a boolean badge (`self_like`) that may apply to any Part.

No inference, interpretation, or transformation of SelfLike is permitted.

---

## Clarification 002 — Intensity and Strength Semantics

The fields:

- Part.intensity
- Relationship.strength

must be interpreted as user-declared integers in the range 0–10.

Rules:

- No normalization or rescaling is permitted.
- No semantic interpretation is permitted.
- Absence of these fields must not trigger default scoring or inference.

---

## Clarification 003 — Tags and Subtype

The fields:

- tags
- subtype

are purely descriptive user metadata.

Rules:

- They must not be interpreted.
- They must not drive classification or inference.
- They must not trigger UI automation or suggestions.

---

## Clarification 004 — Schema Versioning (V1)

Schema versioning rules:

- Export must emit schema_version = "1.0.1".
- Import must accept only schema versions in the 1.x.x range.
- Unknown or incompatible versions must be rejected.

schema_version indicates structural compatibility, not feature richness.

---

## Clarification 005 — Presentation Metadata (Avatars)

The optional Part field `avatar` is presentation-only metadata.

Rules:

- avatar must not affect category, relationships, or validation.
- avatar must not be interpreted psychologically or clinically.
- avatar must not trigger inference, ranking, or guidance.
- avatar is always user-declared.

avatar exists solely to support visual externalization.

---

## Clarification 006 — Geometry Metadata (Positions)

The optional Part field `position` is geometry-only metadata.

Rules:

- position preserves user-chosen layout (e.g., freeform drag/move).
- position must not be interpreted as psychological meaning by the system.
- position must not affect category, relationships, or validation beyond type checking.
- position is always user-driven; no inference or suggestions are permitted.

position exists solely to preserve the user’s visual externalization.

---

## Clarification 007 — Dual Export Artifacts (V1)

V1 export supports two distinct artifacts:

A) Canonical Map Export (Importable JSON)
- Strict canonical JSON (schema_version "1.0.1")
- The only importable artifact

B) Share/Print Export (Human-readable PDF)
- Not importable
- Must visually match, as closely as possible, what the user saw on screen
- Must include only user-declared content and layout (including Part.position when present)
- Must not add meaning, summaries, insights, advice, or recommendations

The importer must accept only the canonical JSON artifact.

---

## Clarification 008 — Non-Interpretation Principle

The system must not:

- interpret Parts or relationships
- infer meaning, intent, or diagnosis
- generate insights, summaries, or recommendations
- auto-classify or auto-link Parts
- suggest categories, relationships, avatars, or positions

All representational meaning is supplied by the user.

---

## Clarification 009 — Explicit User Action

All state changes must result from explicit user action.

Rules:

- No autosave without user intent.
- No automatic relationship creation.
- No implicit mutation of Parts or Maps.

---

END CLARIFICATIONS PATCH
