# IFS Parts Mapper — V1 UI Wireframe Specification (No Code)

This document defines the v1 UI wireframe at a conceptual level.
It is intentionally framework-agnostic and contains no code.

Goals:
- minimal visible complexity
- high readability
- low cognitive load
- enforce provisionality, non-diagnostic framing, and privacy rules

---

## 1) Global Layout

Single-page application with three vertical zones:

A) Top Bar (always visible)  
B) Main Work Area (two columns)  
C) Footer / Status (small, always visible)

---

## 2) Top Bar (Zone A)

### 2.1 Left: App Identity
- Title: “IFS Parts Mapper (V1)”
- Subtitle: “A provisional map. Not a diagnosis.”

### 2.2 Center: Map Controls (compact)
- Map Title field (short)
- “New / Clear Session” button (prominent)

### 2.3 Right: Privacy Banner (persistent)
Always visible text:
- “No accounts. No server storage. Export is your save.”
- “Avoid identifying or clinical details.”

Optional: small info icon that expands to show:
- “Session-only. Nothing is saved unless you export.”
- “Maps are snapshots and can be revised anytime.”

---

## 3) Main Work Area (Zone B)

Two columns:

LEFT COLUMN = Controls Panel  
RIGHT COLUMN = Graph Panel

Default width: Controls 35–40%, Graph 60–65%.
(Adjustable if possible, but not required.)

---

## 4) Controls Panel (Left Column)

The Controls Panel is an accordion (collapsible sections) in this order:

1) Trailhead  
2) Parts  
3) Relationships  
4) Filters  
5) Import / Export

Only one section open by default to reduce clutter.

---

### 4.1 Trailhead Section

Purpose: context entry without interpretation.

Fields (all optional but present):
- Trigger: tags (multi-select or short comma list) + optional short description
- Dominant protector patterns: tags list
- Core vulnerability themes: tags list

Microcopy (always present):
- “Descriptive only. No diagnosis. Keep it brief.”

PASS if:
- Trailhead can be edited anytime
- No interpretive prompts appear

---

### 4.2 Parts Section

Purpose: create/edit/delete parts.

Subpanel A: Create Part (top)
- Label (required)
- Category (required dropdown: Manager, Firefighter, Exile, SelfLike, Other)
- Subtype (optional, short)
- Intensity (optional, bounded)
- Notes (optional, short; character limit; warning text)
Buttons:
- “Add Part”

Subpanel B: Parts List (below)
- Search box (optional, v1.1; not required)
- List/table of parts with:
  - label
  - category
  - intensity (if present)
  - actions: Select / Edit / Delete

Editing pattern:
- Selecting a part populates the Create/Edit fields (same form).
- Show “Update Part” and “Cancel Edit”.
- Deleting prompts confirmation: “Delete part and its relationships?”

PASS if:
- Self cannot be created as a category
- Deleting a part removes its relationships
- Notes remain short with visible reminder

---

### 4.3 Relationships Section

Purpose: create/edit/delete relationships + bulk linking.

Subpanel A: Add Relationship (single edge)
- Type dropdown: protects, polarized_with
- Source part dropdown
- Target part dropdown
Buttons:
- “Add Relationship”

Rules enforced at UI:
- No self-loops (disable same source/target)
- For polarized_with: display as “A ↔ B”
- For protects: display as “A → B (protects)”

Subpanel B: Bulk Linking (required in v1)
Two tabs:

Tab 1: Protector → Multiple Exiles (protects)
- Select Protector (single)
- Select Exiles (multi)
- Button: “Link (protects)”
- Note: duplicates skipped

Tab 2: Exile ← Multiple Protectors (protects)
- Select Exile (single)
- Select Protectors (multi)
- Button: “Link (protects)”
- Note: duplicates skipped

Subpanel C: Relationships List
- List/table with:
  - type
  - endpoints
  - actions: Delete (and Edit only if needed)
- Polarization entries appear once (not duplicated).

PASS if:
- polarized_with stored/displayed as one undirected relationship
- duplicates are prevented
- bulk linking works cleanly

---

### 4.4 Filters Section

Purpose: display toggles only (no analytics).

Toggles:
- Show categories: Manager, Firefighter, Exile, SelfLike, Other
- Show relationship types: protects, polarized_with

PASS if:
- Filters never change underlying data
- Filters are reversible

---

### 4.5 Import / Export Section

Purpose: user-controlled persistence.

Buttons:
- Export JSON (canonical)
- Import JSON
- Export Graph Image (graph-only)

Warnings (always present):
- “Export is your save.”
- “Imports must match schema_version 1.x.x.”
- “No summaries are generated.”

PASS if:
- Import restores map without loss
- Unknown fields rejected or flagged
- No persistence occurs without explicit export

---

## 5) Graph Panel (Right Column)

Graph canvas with:

Top row:
- “Graph View” label
- Legend: categories + edge styles (small, neutral)

Main canvas:
- Interactive graph (drag nodes, pan, zoom)
- Clicking a node highlights it and shows a small info card (non-interpretive):
  - label, category, subtype, intensity, notes (if any)
- Clicking an edge shows:
  - type and endpoints (no interpretation)

Bottom row:
- Status text:
  - “Snapshot. Revisable.”
  - “No diagnosis or inference.”

PASS if:
- No Self node appears
- Node styling is neutral (category-based only)
- Node size does not encode centrality

---

## 6) Empty State Design

When map has no parts:
- Graph panel shows an empty canvas with a single instruction:
  - “Add parts on the left to begin.”
- No sample data is auto-created.

---

## 7) Accessibility / Low-Vision Defaults

Required defaults:
- Large base font
- High contrast without “alarm” colors
- Clear spacing
- Avoid tiny icons-only controls
- All critical actions are labeled buttons (not icon-only)
- Keyboard navigation where possible (nice-to-have in v1; required in v1.1+)

---

## 8) UI Compliance Checklist (Wireframe Level)

PASS if all are true:
- No Self node
- No diagnostic or interpretive language
- Notes are short with warnings
- No analytics, ranking, or “insights”
- Export/import is the only persistence
- Bulk linking exists
- polarized_with is undirected and single-instance
- Visuals are neutral and non-hierarchical
