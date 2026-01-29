# IFS PARTS MAPPER — SPEC AUTHORITY MAP

This file defines the hierarchy of specifications for the IFS Parts Mapper project.

If any documents conflict, the higher-priority document always overrides lower-priority ones.

---

## TIER 0 — Absolute Canonical Authority (Non-Negotiable)

1) spec/IFS_PARTS_MAPPER_MASTER_SPEC.md

If any other document conflicts with this Master Spec, the other document is wrong.

No other document may override, replace, or reinterpret the Master Spec.

---

## TIER 1 — Enforcement & Guardrails (Must Not Contradict Tier 0)

These documents enforce or constrain implementation, but may not contradict Tier 0:

- spec/AI_CODING_PROMPT_STRICT.md
- spec/IFS_Parts_Mapper_Anti_Drift_Protocol.md
- spec/IFS_Parts_Mapper_Implementation_Red_Flags.md

If any Tier 1 document conflicts with Tier 0, Tier 0 wins.

---

## TIER 2 — Derived / Secondary Specs (Helpful, Not Canon)

These may summarize, harden, or restate rules, but they are NOT canonical:

- spec/IFS_Parts_Mapper_Master_Spec_Hardened.md
- spec/IFS_Parts_Mapper_V1_Supreme_Authority.md

If any Tier 2 document conflicts with Tier 0 or Tier 1, Tier 0/1 wins.

---

## TIER 3 — Implementation Guidance (How-To, Not Behavior Authority)

These documents guide implementation and mapping to code, but do not define app behavior beyond Tier 0:

- spec/IFS_Parts_Mapper_Spec_to_Code_Mapping_Table.md
- spec/IFS_Parts_Mapper_V1_Build_Map.md
- spec/IFS_Parts_Mapper_V1_UI_Wireframe_Spec.md

If Tier 3 conflicts with Tier 0–2, higher tiers win.

---

## TIER 4 — Model Contracts, Schemas, Clarifications, and Errata (Support Only)

These documents clarify or constrain representation formats. They never expand scope:

- spec/IFS_Parts_Mapper_V1_Model_Contract.md
- spec/IFS_Parts_Mapper_Minimal_Canonical_JSON_Schema_V1.md
- spec/IFS_Parts_Mapper_V1_Clarifications_Patch.md
- spec/IFS_Parts_Mapper_v1_Errata.md

If Tier 4 conflicts with Tier 0–3, higher tiers win.

---

## Global Non-Drift Rule (Applies to ALL Tiers)

No document and no implementation may introduce:

- new Part Types (Part Types are a closed system)
- Self as a Part (forbidden)
- interpretive logic or inferred meaning
- therapeutic guidance or analysis
- automatic classification, inference, or pattern detection
- autosave without explicit user action
- accounts, default uploads, or telemetry about Parts/maps

Only the user declares meaning. The system records what the user chooses to represent.

END SPEC AUTHORITY MAP
