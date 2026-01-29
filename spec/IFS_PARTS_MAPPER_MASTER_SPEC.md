# IFS PARTS MAPPER  
## MASTER SPECIFICATION (FINAL)

---

## Canonical Authority

This document is the single source of truth for the IFS Parts Mapper.

If implementation conflicts with this specification, the implementation is wrong.

No feature, design, or behavior may override this specification unless it is explicitly revised.

---

## 1) Purpose of the Application

The IFS Parts Mapper is a visual application for representing Parts and related experiences described in Internal Family Systems (IFS).

The application allows users to:

- represent Parts,
- label Parts,
- map relationships between Parts.

The application does not interpret, explain, evaluate, or judge Parts or relationships.

It only records how the user chooses to represent their experience.

---

## 2) IFS Concepts vs Application Representation

In Internal Family Systems:

- the internal system includes Self and Parts,
- Self is distinct from Parts,
- Parts are aspects of experience with their own perspectives and roles.

In this application:

- Parts and related experiences are represented as map elements,
- Self is not represented as a Part or map node,
- users may optionally mark Parts as “Self-like” to indicate perceived qualities associated with Self.

The application does not define or interpret Self.  
It only represents user-declared elements and attributes.

---

## 3) Meaning of “Part” in the Application

In this application, a Part is not defined by a single job, feeling, or burden.

A Part may include:

- roles or strategies,
- emotions or sensations,
- memories or images,
- beliefs or impulses,
- or other patterns of experience.

Parts are not reduced to what they do, what they feel, or what they carry.

In Internal Family Systems, Parts are not considered “bad.”  
The application does not judge, rank, or evaluate Parts.

The application only records how the user chooses to represent them.

---

## 4) Attributes of a Part

Every Part represented in the map has three independent attributes:

1) Symbol (visual representation)  
2) Type (IFS category chosen by the user)  
3) Self-like badge (optional)

These attributes are independent:

- Symbol does not determine Type.
- Type does not determine meaning.
- Self-like does not mean Self.

The application does not infer or reconcile these attributes.

---

## 5) Symbols

A Symbol is the visual form used to represent a Part.

Symbols may include:

- human figures (adult, child, neutral),
- animals,
- symbolic or archetypal figures,
- abstract shapes or forms,
- custom icons.

Rules:

- any Symbol may be used for any Type,
- the application does not infer Type from Symbol.

Symbols are metaphors chosen by the user.

---

## 6) Part Types (IFS Structure)

Every Part must be labeled by the user as one of three Types:

1) Protector  
2) Exile  
3) Unclassified  

The Type label is always visible on the map.

The application does not infer, correct, or validate Type.

---

### 6.1 Protector

In IFS, Protectors are Parts experienced as trying to manage, prevent, or respond to difficulty.

Every Protector must be one of two subtypes:

- Manager  
- Firefighter  

There are no other Protector subtypes.

Rules:

- every Manager is a Protector,
- every Firefighter is a Protector,
- Exiles cannot be Managers or Firefighters,
- Unclassified elements cannot be Managers or Firefighters,
- a Part cannot be both Manager and Firefighter.

#### Manager (Protector subtype)

In IFS, Managers are typically experienced as Parts that try to prevent problems before they happen.

The application does not evaluate whether a Part is preventative.  
The user chooses this label.

#### Firefighter (Protector subtype)

In IFS, Firefighters are typically experienced as Parts that respond to distress that is already happening.

The application does not evaluate whether a Part is reactive.  
The user chooses this label.

---

### 6.2 Exile

In IFS, Exiles are typically experienced as Parts that carry vulnerable, painful, or unmet experiences.

Rules:

- Exiles have no subtypes in the application,
- the application does not determine whether something is an Exile,
- the user chooses this label.

---

### 6.3 Unclassified

Unclassified includes anything the user chooses to represent that is not clearly labeled as a Protector or an Exile.

This may include:

- Parts whose role is unclear,
- emerging or ambiguous experiences,
- elements that do not clearly fit Protector or Exile,
- or phenomena that may not be Parts in the strict IFS sense.

Unclassified may therefore include experiences sometimes described in IFS as “Unattached Burdens,” without requiring advanced terminology.

Rules:

- Unclassified does not mean invalid or meaningless,
- the application does not interpret what Unclassified represents,
- the user may reclassify or leave elements Unclassified indefinitely.

---

## 7) Self-like Badge

Any Part may optionally be marked as “Self-like.”

In IFS, “Self-like” refers to qualities associated with Self (e.g., calmness, clarity, groundedness).

In this application:

- Self-like is a user-chosen badge, not a Type,
- Self-like does not mean the Part is Self,
- Self-like can be added or removed at any time,
- Self-like does not affect logic or relationships.

The application does not interpret Self-like status.

---

## 8) Relationships Between Parts

Relationships describe how the user experiences connections between Parts or other represented elements.

The application records relationships but does not interpret them.

Each relationship has:

- a source element,
- a target element,
- a label,
- a direction (one-way or two-way).

Relationships are structural representations, not psychological explanations.

---

### 8.1 Relationship Types

The application supports the following relationship labels:

protects (one-way)  
polarized with (two-way)  
works with (two-way)  
blocks (one-way)  
directs (one-way)  
activated by (one-way)  
connected to (one-way or two-way)

The application does not infer meaning from relationship labels.

---

## 9) Non-Interpretive Boundary

The application does not:

- interpret Parts,
- analyze relationships,
- suggest meanings,
- diagnose patterns,
- evaluate correctness,
- or guide therapy.

The user brings meaning.  
The application provides structure.

---

## 10) Meaning of Maps

Maps are representations, not explanations.

---

## 11) Language in the Application

The application uses non-technical language:

- Save my map
- Open a map
- Part
- Connection
- Map view

Technical concepts are not exposed to users.

---

## 12) Core Boundary Statement

The application is a mapping tool, not a therapeutic authority.

It does not define what Parts “really are.”  
It does not define what maps “mean.”

It only provides a structured way for users to externalize and organize their experience.

---

## 13) Drift Prevention Rules

The application must not:

- generate interpretations or insights,
- infer psychological meaning,
- suggest Part types or relationships,
- provide therapeutic guidance,
- rank or evaluate Parts,
- introduce new Part Types,
- represent Self as a Part,
- apply AI interpretation,
- autosave or upload maps without explicit user action.

When in doubt, prefer neutrality over explanation.

---
