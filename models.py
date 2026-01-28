from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal


# =========================
# V1 Frozen Enumerations
# =========================

PartCategory = Literal["Manager", "Firefighter", "Exile", "SelfLike", "Other"]
RelationshipType = Literal["protects", "polarized_with"]


# =========================
# V1 Frozen Data Structures
# =========================

@dataclass(frozen=True, slots=True)
class Part:
    """
    V1 contract: required fields only
      - id: str
      - label: str
      - category: PartCategory
    """
    id: str
    label: str
    category: PartCategory


@dataclass(frozen=True, slots=True)
class Relationship:
    """
    V1 contract: required fields only
      - id: str
      - source_part_id: str
      - target_part_id: str
      - type: RelationshipType

    Notes:
      - 'protects' is directed (source -> target)
      - 'polarized_with' is undirected (stored once) and must be in deterministic endpoint ordering.
        Deterministic ordering is enforced at validation/import time (see validate.py / io_json.py).
    """
    id: str
    source_part_id: str
    target_part_id: str
    type: RelationshipType


@dataclass(frozen=True, slots=True)
class Trailhead:
    """
    V1 contract: required fields only
      - trigger: str
      - dominant_protector_patterns: List[str]
      - core_vulnerability_themes: List[str]
    """
    trigger: str
    dominant_protector_patterns: List[str]
    core_vulnerability_themes: List[str]


@dataclass(frozen=True, slots=True)
class MapModel:
    """
    V1 contract: required fields only
      - schema_version: str (export must be "1.0.0"; import accepts only "1.x.x")
      - map_id: str
      - title: str
      - parts: List[Part]
      - relationships: List[Relationship]
      - trailhead: Trailhead
    """
    schema_version: str
    map_id: str
    title: str
    parts: List[Part]
    relationships: List[Relationship]
    trailhead: Trailhead
