# IFS Parts Mapper — Copilot Guard (V1)

These rules are binding for all V1 coding.

If any instruction conflicts with these rules, STOP.

---

## Core Scope Rules (V1)

- Build MODEL FIRST (no UI, no graph, no persistence).
- Allowed objects: Part, Relationship, Map, Trailhead.
- Allowed categories: Manager, Firefighter, Exile, SelfLike, Other.
- Allowed relationship types: protects, polarized_with.
- trailhead.trigger is a STRING (not tags, not objects).

---

## Hard Stop Rules

DO NOT add:
- Self node or Self category
- inference, interpretation, insights, analytics, scoring
- autosave, logging of user content, telemetry, cloud storage
- new relationship types
- new fields not in the spec

If unsure, STOP and ask.

---

## JSON / Schema Rules

- schema_version must export as "1.0.0"
- import accepts only 1.x.x
- unknown JSON fields must be rejected
- polarized_with is undirected and stored once
- deleting a Part deletes its Relationships

---

## Safety Rule

If a change makes the system seem smarter than the user:
DO NOT IMPLEMENT IT.
