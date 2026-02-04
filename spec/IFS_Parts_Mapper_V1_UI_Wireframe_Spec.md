# IFS Parts Mapper — V1 UI Wireframe Specification

Status: LOCKED  
Scope: V1 ONLY  
Type: UI states and transitions (design-only)  
Code: NONE  

This document defines the authoritative V1 user-interface flow for the
IFS Parts Mapper application.

It is derived strictly from the frozen canonical specifications and the
approved UI-flow decisions.

This document is a governance artifact.
If implementation conflicts with this document, the implementation is wrong.

────────────────────────────────────────────
CORE PRINCIPLES
────────────────────────────────────────────

• Non-clinical
• Phenomenological
• Privacy-first
• Local-first
• User-owned
• No interpretation
• No inference
• No autosave
• No guidance
• No persistence without explicit export

────────────────────────────────────────────
STATE 1 — ENTRY / NEW MAP
────────────────────────────────────────────

Screen ID: ENTRY_NEW_MAP

Visible:
• Primary action: “Start a new map”
• Anchored empty canvas (orientation only, non-interactive)

Not visible:
• No map name
• No save or export
• No parts
• No categories
• No help or tutorial

User actions:
• Start a new map

Transition:
• Start a new map → MAP_ACTIVE_EMPTY

────────────────────────────────────────────
STATE 2 — ACTIVE MAP (EMPTY)
────────────────────────────────────────────

Screen ID: MAP_ACTIVE_EMPTY

Visible:
• Interactive empty canvas
• Primary action: “Add a part”

Not visible:
• No relationships
• No export
• No save
• No completion language

User actions:
• Add a part
• Leave the app

Transition:
• Add a part → PART_CREATE

────────────────────────────────────────────
STATE 3 — CREATE PART
────────────────────────────────────────────

Screen ID: PART_CREATE

Visible:
• Input: Part name (required)
• Selector: Category
  – Manager
  – Firefighter
  – Exile
  – Other
• Optional:
  – Self-like (boolean badge only)
  – Avatar (visual metadata only)
• Confirm action

Not visible:
• No examples
• No suggestions
• No guidance text
• No interpretation

User actions:
• Confirm creation
• Cancel

Transition:
• Confirm → PART_PLACEMENT
• Cancel → return to prior map state

────────────────────────────────────────────
STATE 4 — PLACE PART
────────────────────────────────────────────

Screen ID: PART_PLACEMENT

Visible:
• Newly created part on canvas
• Part is draggable

Not visible:
• No grid
• No snapping
• No auto-layout
• No meaning attached to position

User actions:
• Drag part
• Leave part where it appears

Transition:
• Placement complete → MAP_ACTIVE_WITH_PARTS

────────────────────────────────────────────
STATE 5 — ACTIVE MAP (WITH PARTS)
────────────────────────────────────────────

Screen ID: MAP_ACTIVE_WITH_PARTS

Visible:
• Canvas with one or more parts
• Actions:
  – Add a part
  – Add a relationship (only if two or more parts exist)

Not visible:
• No progress indicators
• No “next” step
• No required actions

User actions:
• Add part
• Add relationship
• Reposition parts
• Leave the app

Transition:
• Add part → PART_CREATE
• Add relationship → RELATIONSHIP_CREATE
• First arrival only → BOUNDARY_NOTICE

────────────────────────────────────────────
STATE 6 — ONE-TIME BOUNDARY NOTICE
────────────────────────────────────────────

Screen ID: BOUNDARY_NOTICE

Visible (dismissible notice):

“This map exists only in this session unless you export it.
Closing the app will discard it.”

Not visible:
• No save button
• No export button
• No urgency language

User actions:
• Dismiss notice

Transition:
• Dismiss → MAP_ACTIVE_WITH_PARTS
• Notice never shown again this session

────────────────────────────────────────────
STATE 7 — CREATE RELATIONSHIP
────────────────────────────────────────────

Screen ID: RELATIONSHIP_CREATE

Visible:
• Selector: Part A
• Selector: Part B
• Selector: Relationship type
  – protects (directional)
  – polarized_with (undirected)
• Direction control shown only for protects
• Confirm action

Not visible:
• No suggested relationships
• No inferred links
• No meaning or weighting

User actions:
• Confirm
• Cancel

Transition:
• Confirm → MAP_ACTIVE_WITH_PARTS
• Cancel → MAP_ACTIVE_WITH_PARTS

────────────────────────────────────────────
STATE 8 — EXPORT CHOICE
────────────────────────────────────────────

Screen ID: EXPORT_CHOICE

Visible:
Title:
“What would you like to do with this map?”

Options:
• Save for later use
  “Creates a file you can open again in this app.”
• Create a read-only copy
  “Creates a copy you can view or share.”

Not visible:
• No file formats
• No defaults
• No recommendations

User actions:
• Choose option
• Cancel

Transition:
• Choose option → OS_SAVE_DIALOG
• Cancel → MAP_ACTIVE_WITH_PARTS

────────────────────────────────────────────
STATE 9 — NATIVE OS SAVE DIALOG
────────────────────────────────────────────

Screen ID: OS_SAVE_DIALOG

Visible:
• Operating system native save dialog
  – Windows
  – macOS
  – Linux

Pre-dialog text (single line):
“You’ll choose where this file is saved on your computer.”

Not visible:
• No app-defined folders
• No path explanations
• No storage assumptions

User actions:
• Save
• Cancel

Transition:
• Save → MAP_ACTIVE_WITH_PARTS
• Cancel → MAP_ACTIVE_WITH_PARTS

────────────────────────────────────────────
END OF DOCUMENT
────────────────────────────────────────────
