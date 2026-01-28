# IFS Parts Mapper — Master Specification (V1, Hardened)

This document is the single authoritative specification for the IFS Parts Mapper v1.
It merges philosophy, scope, architecture, behavior, data model, privacy rules, and acceptance criteria.
It has been hardened to remove ambiguity and prevent conceptual drift.

This document replaces all prior specs.

---

## 1) Purpose and Identity

The IFS Parts Mapper is a public, non-clinical, privacy-first tool for visually mapping Internal Family Systems (IFS) parts and their relationships.

The tool is a lens for exploration, not a diagnostic system and not a model of the person.

Core aims:
- phenomenological, not diagnostic
- privacy-by-design
- relational clarity
- many-to-many relationships
- visual intelligibility
- user-owned data

---

## 2) Non-Negotiable Principles

### 2.1 Clinical / Epistemic

- Parts are experiences, not identities.
- Maps are snapshots, not truths.
- No diagnosis, scoring, typology, ranking, or inference.
- Self is never represented as a part or node (SelfLike is allowed).
- All maps must remain revisable.

### 2.2 Privacy

- No server-side persistence of user data.
- No disk writes of user data except explicit export.
- No content logging (labels, notes, trailhead text must never appear in logs or errors).
- No telemetry or analytics containing user content.
- No accounts in v1.
- Import/export is the only persistence mechanism.

### 2.3 Scope Discipline

- Minimal visible complexity.
- Latent conceptual depth.
- No feature creep in v1.

---

## 3) Core Conceptual Objects

### 3.1 Part

A Part represents a user-described experiential pattern.

Required attributes:
- id
- label
- category

Optional attributes:
- subtype
- intensity
- notes
- tags

Allowed categories:
- Manager
- Firefighter
- Exile
- SelfLike
- Other

Constraints:
- Self is not a valid category.
- Labels must be non-empty.
- Parts are mutable and revisable.
- Notes must be short and non-identifying (see Section 8).

---

### 3.2 Relationship

A Relationship represents a connection between parts.

Required attributes:
- id
- source_part_id
- target_part_id
- type

Optional attributes:
- strength
- notes

Allowed types (v1):
- protects (directional; functional, not hierarchical)
- polarized_with (non-directional)

Constraints:
- source_part_id ≠ target_part_id.
- Both parts must exist.
- No duplicate relationships.
- polarized_with is stored once (undirected).

Duplicate definition:
- protects duplicates: same source, same target, same type.
- polarized_with duplicates: same unordered pair, same type.

---

### 3.3 Map

A Map is a system snapshot.

Required attributes:
- schema_version
- map_id
- title
- parts
- relationships
- trailhead

Trailhead fields:
- trigger
- dominant_protector_patterns
- core_vulnerability_themes

Trailhead rules:
- Trailhead object must exist.
- Fields may be empty but must exist.

Constraints:
- Maps are provisional snapshots.
- Maps are editable at all times.

---

## 4) Graph Semantics

Structural principles:
- Non-hierarchical topology.
- Relationship primacy.
- Dense, non-linear connectivity.

Visual principles:
- No Self center.
- Node size must not encode dominance, centrality, or importance.
- Edge thickness must not encode psychological meaning automatically.
- No visual dominance or pathology cues.
- Layout implies readability, not meaning.

---

## 5) V1 Scope Definition

V1 MUST include:
- Parts creation, editing, deletion
- Relationships creation, editing, deletion
- Relationship types: protects, polarized_with
- Many-to-many relationships
- Bulk linking (protectors ↔ exiles)
- Interactive graph visualization
- Filtering by category and relationship type
- Trailhead metadata
- JSON import/export
- Visual graph export (graph image only)
- Session-based state
- Privacy safeguards

V1 MUST NOT include:
- Diagnosis or interpretation
- Scoring, ranking, or metrics
- AI inference or suggestions
- Temporal modeling
- Accounts or cloud storage
- Additional relationship types
- Summaries, insights, or psychological conclusions

---

## 6) System Architecture (Conceptual)

Core components:

1. Map Core
2. Part Manager
3. Relationship Manager
4. Graph Renderer
5. Import / Export Layer
6. Session State Container

Responsibilities:

- Map Core: holds parts, relationships, trailhead metadata.
- Part Manager: manages part lifecycle.
- Relationship Manager: manages relationships and bulk linking.
- Graph Renderer: visualizes the map without implying meaning.
- Import/Export Layer: user-controlled persistence.
- Session State: holds all active data.

Principle:
- Conceptual model and visualization are separate.
- System never infers meaning.

---

## 7) Behavioral Rules

### 7.1 Editing

- Parts and relationships can be edited or deleted at any time.
- Deleting a part automatically deletes all related relationships.

### 7.2 Bulk Linking

- Protectors can link to multiple exiles.
- Exiles can link to multiple protectors.
- Existing relationships are skipped, not duplicated.
- Bulk linking must be reversible.

### 7.3 Empty Map Behavior

- When no parts exist, the graph displays an empty canvas with neutral guidance text.
- No sample data is auto-created.

---

## 8) Validation and Safety Rules

Hard constraints:
- Parts must have labels.
- Relationships must reference valid parts.
- Only allowed relationship types.
- No self-loops.
- No duplicate edges.

Soft constraints:
- Notes length must be limited (recommended: short descriptive text).
- UI must display a reminder: “Avoid identifying or clinical details.”

Safeguard constraints:
- No Self node.
- No diagnostic or typological fields.
- No automated interpretation.

---

## 9) Canonical Data Structure (Conceptual JSON)

Top-level map:
- schema_version = "1.0.0"
- map_id
- title
- parts
- relationships
- trailhead

Part:
- id
- label
- category
- subtype (optional)
- intensity (optional)
- notes (optional)
- tags (optional)

Relationship:
- id
- source_part_id
- target_part_id
- type
- strength (optional)
- notes (optional)

Trailhead:
- trigger
- dominant_protector_patterns
- core_vulnerability_themes

Schema rules:
- v1 imports must accept schema_version 1.x.x only.
- Latent ontology fields must not appear in v1 exports.

---

## 10) UX Constraints

The interface must:
- emphasize provisionality
- avoid identity language
- avoid diagnostic framing
- make revision easy

The interface must not:
- rank parts
- evaluate system health
- infer meaning

---

## 11) Acceptance Criteria (V1)

V1 is complete when:

- Complex many-to-many maps are possible.
- Graphs remain visually understandable.
- Maps can be exported and restored without loss.
- Privacy constraints are upheld.
- No diagnostic or interpretive output exists.
- System remains conceptually minimal.

---

## 12) Latent Ontology (Not Exposed in V1)

Latent conceptual dimensions:
- roles
- strategies
- burdens
- coalitions
- activation states
- systemic dynamics
- topology patterns

Design principle:
Latent complexity, visible simplicity.

---

## 13) Core Thesis

The map is not the system.
The system is not the self.
The self is not representable.
The tool is a lens, not a mirror.
