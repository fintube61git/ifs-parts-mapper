# IFS Parts Mapper — Implementation Red Flags (V1)

This document is a companion to the Master Spec.
It lists the most common ways developers (or AI coding agents) will accidentally violate the spec.
If any item below occurs, stop and fix it immediately.

---

## 1) Self Reification Red Flags

### RED FLAG: A “Self” node appears anywhere
Examples:
- Category includes “Self”
- Default map centers on “Self”
- A special Self hub or Self anchor exists

Why this is a violation:
- Self is not representable as a part or node.

Correct behavior:
- SelfLike is the closest allowed category.
- No “center” node is privileged.

---

## 2) Diagnostic Drift Red Flags

### RED FLAG: Any diagnostic or trait framing
Examples:
- “You are anxious” or “This part is your anxiety disorder”
- “Symptoms,” “severity,” “risk,” “screening,” “assessment,” “treatment outcomes”
- Any field named diagnosis, disorder, symptom, trait, pathology

Why this is a violation:
- The tool is phenomenological and non-clinical by design.

Correct behavior:
- Only user-declared structure and descriptions.
- No psychological conclusions.

---

## 3) Inference / Insights Red Flags

### RED FLAG: Derived meaning or interpretation
Examples:
- “Most dominant part”
- “Core exile”
- “Your system is avoidant”
- “This pattern indicates trauma”
- Auto-suggested interpretations or recommended interventions

Why this is a violation:
- The system must not infer meaning beyond user-declared nodes/edges.

Correct behavior:
- The tool stores and displays only what the user entered.
- No computed psychological conclusions.

---

## 4) Visual Meaning-Leak Red Flags

### RED FLAG: Visual encoding implies dominance or health
Examples:
- Node size based on number of connections
- Color gradients implying good/bad parts
- “Heat maps” or “activation meters”
- “Central” layout described as “core” or “true”

Why this is a violation:
- Layout is for readability only; it must not imply psychological truth.

Correct behavior:
- Node styling is neutral (at most category-based).
- No centrality-based meaning shown to user.

---

## 5) Relationship Semantics Red Flags

### RED FLAG: Polarization stored or displayed as two directed edges
Examples:
- A → B polarized_with AND B → A polarized_with
- Polarization treated as directional

Correct behavior:
- polarized_with is stored once, undirected.

### RED FLAG: protects treated as hierarchical power
Examples:
- UI language implying dominance (“protector controls exile”)
- Visual ranking (“protector is higher / exile is lower” as meaning)

Correct behavior:
- protects is directional but functional, not hierarchical.

---

## 6) Privacy Violations (Most Dangerous)

### RED FLAG: Any persistence outside explicit export/import
Examples:
- Saving maps automatically to disk or database
- Caching user content in a way that persists across sessions
- “Autosave” to server

Correct behavior:
- Session-only state.
- Persistence only via user-controlled export/import.

### RED FLAG: Content appears in logs or error traces
Examples:
- Exceptions printing part labels or notes
- Logging user-entered JSON payloads
- “Debug mode” that prints map content

Correct behavior:
- No map content in logs.
- Errors must be content-redacted.

### RED FLAG: Telemetry or analytics
Examples:
- “Track usage”
- “Send crash reports with user data”

Correct behavior:
- No analytics containing user content.

---

## 7) Notes / PHI Risk Red Flags

### RED FLAG: Long free-text clinical narratives are encouraged or easy
Examples:
- Large free-text journaling areas
- “Tell your trauma story here”
- No warnings or limits

Correct behavior:
- Notes remain short.
- Persistent reminder to avoid identifying or clinical details.
- Hard character limit enforced in UI/spec.

---

## 8) Scope Creep Red Flags

### RED FLAG: New relationship types in v1
Examples:
- triggers, soothes, blocks, allies, etc.
- Any third relationship type added “because it’s easy”

Correct behavior:
- v1 has exactly two: protects, polarized_with.

### RED FLAG: Analytics dashboards
Examples:
- “System summary”
- “Part counts and dominance”
- “Progress” or “health” score

Correct behavior:
- None of these in v1.

### RED FLAG: Accounts / sharing / cloud
Examples:
- login, user profiles, sync, sharing links

Correct behavior:
- none in v1.

---

## 9) UX Language Drift Red Flags

### RED FLAG: Identity language in UI copy
Examples:
- “Define who you are”
- “Your personality parts”
- “Your core self”

Correct behavior:
- “Add a part that shows up”
- “Current map / snapshot”
- “You can revise this anytime”

---

## 10) Structural Integrity Red Flags

### RED FLAG: Deleting a part leaves broken relationships
Correct behavior:
- Deleting a part removes its relationships automatically.

### RED FLAG: Import accepts unknown fields silently
Risk:
- Hidden schema drift and feature creep by import.

Correct behavior:
- Strict import by default (reject unknown fields or warn explicitly).

---

## 11) Stop Conditions (Immediate Halt)

Stop development immediately if any of these appear:
- Self node exists
- diagnostic/typology language appears
- any interpretive “insight” feature exists
- any persistence beyond explicit export/import exists
- any map content appears in logs

Fix before proceeding.

---

## 12) Quick Compliance Check (5 Questions)

1) Can a user ever create a Self node?  (Must be NO)
2) Does the system ever infer meaning?  (Must be NO)
3) Does anything save without explicit export?  (Must be NO)
4) Does the UI imply hierarchy or dominance?  (Must be NO)
5) Does import/export preserve maps without schema drift?  (Must be YES)

If any answer is wrong, v1 is not compliant.
