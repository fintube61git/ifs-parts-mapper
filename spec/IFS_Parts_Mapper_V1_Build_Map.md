# IFS Parts Mapper — V1 Build Map (Execution Roadmap)

This document defines the exact construction sequence for v1.
It translates the Master Spec and Dev Starter Pack into a step-by-step build roadmap.

This is not code. It is an operational build plan with pass/fail gates.

---

## 0) Pre-Build Integrity Check (Mandatory)

Before building anything, confirm:

- Master Spec is accepted as supreme authority.
- Red Flags and Anti-Drift Protocol are understood.
- V1 scope is frozen.
- No extra features are planned.

PASS if all confirmed.
FAIL if any ambiguity remains.

---

## 1) Foundation Layer — Core Data Model

### Build Step 1.1 — Part Model

Define conceptual Part structure with:
- id
- label
- category
- optional fields

PASS if:
- categories limited to Manager, Firefighter, Exile, SelfLike, Other
- Self cannot exist as a category
- labels are required and non-empty

FAIL if:
- any diagnostic or typological fields appear.

---

### Build Step 1.2 — Relationship Model

Define Relationship structure with:
- source_part_id
- target_part_id
- type

PASS if:
- only protects and polarized_with exist
- protects is directional
- polarized_with is undirected
- duplicates are prevented
- self-loops are impossible

FAIL if:
- new relationship types appear.

---

### Build Step 1.3 — Map Model

Define Map structure with:
- schema_version
- map_id
- title
- parts
- relationships
- trailhead

PASS if:
- trailhead always exists (even if empty)
- schema_version is fixed for v1
- maps are provisional snapshots

---

## 2) State Layer — Session Model

### Build Step 2.1 — Session State

Define session state containing:
- current map
- selected parts/relationships
- filters

PASS if:
- no persistence exists outside session
- state resets cleanly

FAIL if:
- any autosave or background persistence exists.

---

## 3) Core Functionality Layer

### Build Step 3.1 — Part Manager

Capabilities:
- create part
- edit part
- delete part

PASS if:
- deleting a part removes its relationships
- editing does not infer meaning

---

### Build Step 3.2 — Relationship Manager

Capabilities:
- create relationship
- edit relationship
- delete relationship
- bulk linking

PASS if:
- many-to-many linking works
- bulk linking skips duplicates
- relationships remain purely declarative

---

## 4) Visualization Layer

### Build Step 4.1 — Graph Renderer

Capabilities:
- display nodes and edges
- selection and movement
- neutral layout

PASS if:
- no Self center exists
- no visual dominance cues exist
- layout implies readability only

FAIL if:
- graph implies hierarchy or meaning.

---

### Build Step 4.2 — Filters

Capabilities:
- filter by category
- filter by relationship type

PASS if:
- filtering does not alter underlying data meaning.

---

## 5) Import / Export Layer

### Build Step 5.1 — JSON Export

PASS if:
- export preserves full map structure
- no interpretation is added.

---

### Build Step 5.2 — JSON Import

PASS if:
- import restores maps without loss
- unknown fields are rejected or flagged.

---

### Build Step 5.3 — Visual Export

PASS if:
- export produces graph image only
- no summaries or analytics appear.

---

## 6) UX Safeguards Layer

### Build Step 6.1 — Language Safeguards

PASS if:
- UI avoids identity and diagnostic language
- provisional framing is explicit.

---

### Build Step 6.2 — Privacy Safeguards

PASS if:
- no content appears in logs
- no telemetry exists
- explicit warnings discourage PHI.

---

## 7) Anti-Drift Enforcement Layer

### Build Step 7.1 — Spec Gate

PASS if:
- every feature passes Scope, Epistemic, and Complexity gates.

---

### Build Step 7.2 — Drift Checks

PASS if:
- no inference exists
- no persistence exists
- no hierarchy is implied
- no ontology leaks into v1 UI.

---

## 8) V1 Completion Gate

V1 is complete ONLY if:

- many-to-many maps work reliably
- graphs remain understandable
- import/export is lossless
- privacy rules are upheld
- no interpretive features exist
- system remains minimal and neutral

If any condition fails, v1 is not complete.

---

## 9) Golden Rule of Construction

Build structure, not meaning.
Store relationships, not interpretations.
Enforce humility, not intelligence.

---

## 10) One-Line Developer Instruction

If a feature makes the system seem smarter than the user, do not build it.
