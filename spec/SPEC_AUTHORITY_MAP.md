# IFS PARTS MAPPER — SPEC AUTHORITY MAP (V1)

This file defines the authoritative hierarchy of specifications for IFS Parts Mapper V1.

If any documents conflict, the higher-priority document always overrides lower-priority ones.

---

## Governance Rule (Tier 0)

spec/IFS_Parts_Mapper_V1_Supreme_Authority.md

This file defines the final authority rules for V1.
No other spec files should be edited to resolve conflicts; follow its authority order.

---

## Canonical Authority Order (V1)

1) spec/IFS_Parts_Mapper_v1_Errata.md  
2) spec/IFS_Parts_Mapper_V1_Clarifications_Patch.md  
3) spec/IFS_Parts_Mapper_Minimal_Canonical_JSON_Schema_V1.md  
4) spec/IFS_Parts_Mapper_V1_Model_Contract.md  
5) spec/IFS_Parts_Mapper_Master_Spec_Hardened.md  
6) All other documents (UI, Build Map, Mapping Table, etc.)

If any document conflicts with a higher item, the higher item wins.

---

## Non-Canonical / Archive (Must Not Be Used As Authority)

The following file is NOT canonical for V1 because it conflicts with the governance hierarchy and/or the binding V1 data contract:

- spec/IFS_PARTS_MAPPER_MASTER_SPEC.md

It may be retained as an archive/reference, but it must not be treated as the source of truth.

---

## Global Non-Drift Rule (Applies to ALL Documents)

No document and no implementation may introduce:

- new Part Types (closed system)
- Self as a Part (forbidden)
- interpretive logic or inferred meaning
- therapeutic guidance or analysis
- automatic classification, inference, or pattern detection
- autosave without explicit user action
- accounts, default uploads, or telemetry about Parts/maps

Only the user declares meaning. The system records what the user chooses to represent.

END SPEC AUTHORITY MAP (V1)
