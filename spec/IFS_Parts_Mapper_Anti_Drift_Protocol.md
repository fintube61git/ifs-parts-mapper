# IFS Parts Mapper — Anti-Drift Protocol (V1)

This document defines the rules, processes, and enforcement mechanisms that prevent conceptual, clinical, and product drift in the IFS Parts Mapper project.

It is binding on all developers, designers, and AI agents working on v1.

This document complements the Master Specification and Red Flags documents.

---

## 1) Core Principle

Drift is any change that alters the philosophical, clinical, privacy, or structural identity of the system beyond what is defined in the Master Specification.

If drift occurs, development must stop until corrected.

---

## 2) Supreme Authority Rule

The following documents define the system and override all other considerations:

1) IFS_Parts_Mapper_Master_Spec_Hardened.md  
2) IFS_Parts_Mapper_Implementation_Red_Flags.md  
3) IFS_Parts_Mapper_V1_Master_Summary.md  

Rule:

- If a feature is not defined or implied in the Master Spec, it does not exist.
- If code contradicts the Master Spec, the code is wrong.
- If a proposal contradicts Red Flags, it must be rejected.

---

## 3) V1 Lock Rule (Frozen Core)

Once v1 development begins, the following elements are frozen:

### Frozen Clinical Model
- Part categories: Manager, Firefighter, Exile, SelfLike, Other
- Relationship types: protects, polarized_with
- No Self node
- No inference or diagnosis

### Frozen Data Model
- Part, Relationship, Map objects
- Canonical JSON structure
- schema_version semantics

### Frozen Privacy Model
- No server-side persistence
- No content logging
- No telemetry with user content
- Import/export as the only persistence mechanism

These elements may not be changed in v1 except to fix ambiguity or prevent harm.

---

## 4) Spec Gate (Mandatory Pre-Feature Test)

Before any feature is added, it must pass all three gates:

### Gate 1 — Scope Gate
Question: Is this explicitly required by v1 scope?

- YES → continue
- NO → reject or defer to v2+

### Gate 2 — Epistemic Gate
Question: Does this introduce interpretation, diagnosis, ranking, or typology?

- YES → reject
- NO → continue

### Gate 3 — Complexity Gate
Question: Does this increase visible complexity without necessity?

- YES → reject or defer
- NO → continue

If any gate fails, the feature must not be built.

---

## 5) No-Inference Firewall

Rule:

The system may only store and display user-declared parts and relationships.

The system must not:
- infer psychological meaning
- rank parts
- identify “core” or “dominant” parts
- generate interpretations
- recommend interventions
- classify users or systems

If any derived meaning appears, drift has occurred.

---

## 6) Privacy Enforcement Protocol

### Prohibited Behaviors
- automatic saving to disk or server
- logging map content
- analytics or telemetry with user content
- silent persistence across sessions

### Required Safeguards
- session-only state by default
- explicit user-controlled export/import
- content-redacted error handling

If any prohibited behavior is detected, development must stop.

---

## 7) Visual Meaning Guardrail

The graph must never imply psychological meaning through visuals.

Prohibited visual encodings:
- node size based on centrality or degree
- color gradients implying good/bad
- layouts described as “core,” “true,” or “dominant”
- heat maps or activation meters

Allowed encodings:
- neutral category-based styling
- layout for readability only

If visuals imply meaning, drift has occurred.

---

## 8) Language Drift Control

UI and documentation must avoid identity and diagnostic language.

Prohibited language examples:
- “Who you are”
- “Your personality parts”
- “Core self”
- “Disorder,” “symptom,” “severity,” “risk”

Required framing:
- “Current map”
- “Snapshot”
- “Parts that show up”
- “You can revise this anytime”

If identity or diagnostic framing appears, drift has occurred.

---

## 9) Decision Authority Model

When ambiguity arises:

1) Consult the Master Spec.
2) Consult the Red Flags document.
3) If still ambiguous, default to:
   - less interpretation
   - less persistence
   - less visible complexity

If disagreement persists, pause development and revise the spec before coding.

---

## 10) Drift Detection Checklist

At any milestone, ask:

1) Does the system infer meaning beyond user input?
2) Does anything persist without explicit export?
3) Does any UI imply hierarchy or pathology?
4) Has any new relationship type appeared?
5) Has any new ontology been exposed in v1?
6) Has any identity or diagnostic language appeared?
7) Has any “helpful” feature been added without spec justification?

If any answer is YES, drift has occurred.

---

## 11) Stop Conditions

Development must halt immediately if:

- a Self node exists
- diagnostic or typological features appear
- interpretive insights are generated
- user data persists without explicit export/import
- map content appears in logs
- v1 scope is expanded without spec revision

Fix drift before proceeding.

---

## 12) Allowed Spec Changes (V1)

Spec changes are allowed ONLY if they:

1) resolve ambiguity in the existing spec
2) reduce harm or privacy risk
3) simplify v1 without altering IFS integrity

Spec changes are NOT allowed if they:

- add new features
- add new relationship types
- increase interpretation
- increase visible complexity

---

## 13) Operational Rule of Humility

If uncertain, choose:

- less meaning
- less automation
- less persistence
- less complexity

This preserves IFS epistemology and system integrity.

---

## 14) Core Thesis (Operational Form)

The system models structure, not identity.  
The map represents relationships, not truth.  
The architecture enforces humility, not authority.  
The tool remains a lens, not a mirror.
