# IFS Parts Mapper — V1 Development Guardrails

This repository implements **V1 only** of the IFS Parts Mapper.

## Canonical Authority (NON-NEGOTIABLE)

All implementation must conform to:

spec/IFS_Parts_Mapper_Master_Spec_Hardened.md

Supporting enforcement documents (must be obeyed):

- spec/IFS_Parts_Mapper_Anti_Drift_Protocol.md
- spec/IFS_Parts_Mapper_Implementation_Red_Flags.md
- spec/IFS_Parts_Mapper_V1_Build_Map.md
- spec/IFS_Parts_Mapper_V1_UI_Wireframe_Spec.md

If code or UX conflicts with the above, **the code is wrong**.

## Hard Stop Conditions (V1)

The following are **not allowed** in any form:

- Self represented as a node
- New relationship types
- AI inference, interpretation, summaries, or recommendations
- Scoring, ranking, timelines, or analytics
- Autosave, accounts, cloud sync, or telemetry
- Persistence other than explicit JSON import/export

If any of the above appear, stop and remove them.

## Golden Rule

If a feature makes the system seem smarter than the user, **do not build it**.

When uncertain, choose:
- less meaning
- less automation
- less persistence
- less visible complexity
