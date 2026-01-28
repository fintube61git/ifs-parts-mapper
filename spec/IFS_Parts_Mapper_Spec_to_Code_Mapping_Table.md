# Spec-to-Code Mapping Table (V1, Spec-Locked)

This table maps the **Hardened Master Spec** requirements to the **data model + validation rules**.
Purpose: prevent drift. If an implementation rule is missing here, it should not exist in v1.

Sources enforced:
- IFS_Parts_Mapper_Master_Spec_Hardened.md
- IFS_Parts_Mapper_Implementation_Red_Flags.md
- IFS_Parts_Mapper_Anti_Drift_Protocol.md

---

## 1) Map Object

| Spec Requirement | Implementation Rule (Model / Validation) |
|---|---|
| Map is a provisional snapshot | UI copy + documentation must state “snapshot” and “revisable”; model does **not** infer permanence |
| Required keys: schema_version, map_id, title, parts, relationships, trailhead | JSON import/export must reject missing required keys |
| schema_version fixed for v1 | Export must emit schema_version = "1.0.0"; import accepts only 1.x.x per spec |
| Trailhead object must exist | trailhead key required; subkeys required but may be empty |
| No server persistence | No writes to disk/server except explicit export action; no autosave |

---

## 2) Trailhead Object

| Spec Requirement | Implementation Rule (Model / Validation) |
|---|---|
| trailhead exists even if empty | trailhead object required |
| keys required: trigger, dominant_protector_patterns, core_vulnerability_themes | all three keys required; values may be empty |
| descriptive, not interpretive | prompts/copy must not solicit diagnosis or conclusions |
| privacy guidance | persistent warning: “Avoid identifying or clinical details.” |

---

## 3) Part Object

| Spec Requirement | Implementation Rule (Model / Validation) |
|---|---|
| Required: id, label, category | reject if missing |
| Allowed categories only | category ∈ {Manager, Firefighter, Exile, SelfLike, Other} |
| Self not allowed | reject category == "Self" or any equivalent |
| label non-empty | trim whitespace; reject empty |
| optional: subtype, intensity, notes, tags | allow only these extras in v1 |
| notes short and non-identifying | enforce hard length limit + warning microcopy |
| No identity/diagnostic framing | no fields like diagnosis/trait/symptom/severity etc. |

---

## 4) Relationship Object

| Spec Requirement | Implementation Rule (Model / Validation) |
|---|---|
| Required: id, source_part_id, target_part_id, type | reject if missing |
| Allowed types only | type ∈ {"protects", "polarized_with"} |
| protects is directional | store as (source → target) |
| polarized_with is undirected | canonicalize endpoint ordering; store once |
| No self-loops | reject if source_part_id == target_part_id |
| Both endpoints exist | validate that both ids exist in parts |
| Optional: strength, notes | allow only these extras in v1 |
| Duplicate definition | protects duplicates: same (source,target,type); polarized_with duplicates: same unordered pair + type |
| protects not hierarchical | no UI copy implying dominance or rank |

---

## 5) Visual Meaning Guardrails (Graph Semantics)

| Spec Requirement | Implementation Rule (Visualization Constraints) |
|---|---|
| No Self center | never create or special-case Self |
| No visual dominance | node size cannot encode centrality/degree; no “dominant part” |
| Layout readability only | no copy suggesting layout equals truth |
| No auto-analytics | no degree metrics, summaries, insights |

---

## 6) Privacy Enforcement

| Spec Requirement | Implementation Rule (Operational) |
|---|---|
| No content logging | logs/errors must never include labels/notes/trailhead text |
| No telemetry with user content | disable analytics; if any error reporting exists it must be content-redacted |
| No persistence except export | no autosave; no background caching to disk |
| Import/export only persistence | all persistence must be explicit user action |

---

## 7) Acceptance Criteria → Testable Checks

| Acceptance Criterion | Concrete Check |
|---|---|
| Many-to-many maps possible | create multiple protectors/exiles with cross-links; system supports without errors |
| Graph understandable | filters work; layout remains readable; no forced hierarchy |
| Export/import lossless | round-trip JSON matches structure and content |
| Privacy upheld | confirm no disk writes except export; no logs contain content |
| No diagnostic output exists | no computed meaning, rankings, “insights,” or labels beyond user input |
| Minimal system | only v1 scope features present |

---

## 8) Stop Conditions (Immediate Halt)

If any of these appear, v1 is noncompliant:
- Self node exists
- diagnostic/typology/inference features exist
- any persistence beyond explicit export/import exists
- map content appears in logs/errors
- extra relationship types exist
- visuals encode dominance/centrality/health
