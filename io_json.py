from __future__ import annotations

import json
from typing import Any, Dict, Optional

from models import MapModel
from validate import (
    EXPORT_SCHEMA_VERSION,
    ValidationError,
    canonicalize_polarized_endpoints,
    validate_map_dict_strict,
    validate_map_model_for_export,
)


# =========================
# Import / Export (Strict, Venv-safe, No extra deps)
# =========================

def import_map_from_json_text(json_text: str) -> MapModel:
    """
    Strict import:
      - JSON must parse to an object
      - schema_version must be 1.x.x
      - unknown fields forbidden everywhere
      - polarized_with must be stored once and already canonical-ordered (reject otherwise)
      - no self-loops; referential integrity enforced
      - errors contain NO user content
    """
    try:
        data = json.loads(json_text)
    except json.JSONDecodeError:
        raise ValidationError([])  # privacy-safe: no content, no parse details

    return validate_map_dict_strict(data)


def import_map_from_file(path: str, encoding: str = "utf-8") -> MapModel:
    with open(path, "r", encoding=encoding) as f:
        return import_map_from_json_text(f.read())


def export_map_to_dict(model: MapModel) -> Dict[str, Any]:
    """
    Strict export:
      - schema_version must be exactly "1.0.0"
      - model must satisfy all relational constraints
      - produces dict with ONLY canonical fields (no extras)
    """
    validate_map_model_for_export(model)

    return {
        "schema_version": EXPORT_SCHEMA_VERSION,
        "map_id": model.map_id,
        "title": model.title,
        "parts": [
            {"id": p.id, "label": p.label, "category": p.category}
            for p in model.parts
        ],
        "relationships": [
            {
                "id": r.id,
                "source_part_id": r.source_part_id,
                "target_part_id": r.target_part_id,
                "type": r.type,
            }
            for r in model.relationships
        ],
        "trailhead": {
            "trigger": model.trailhead.trigger,
            "dominant_protector_patterns": list(model.trailhead.dominant_protector_patterns),
            "core_vulnerability_themes": list(model.trailhead.core_vulnerability_themes),
        },
    }


def export_map_to_json_text(model: MapModel, *, indent: int = 2) -> str:
    """
    Deterministic JSON output (stable keys).
    """
    data = export_map_to_dict(model)
    return json.dumps(data, ensure_ascii=False, indent=indent, sort_keys=True)


def export_map_to_file(model: MapModel, path: str, *, indent: int = 2, encoding: str = "utf-8") -> None:
    text = export_map_to_json_text(model, indent=indent)
    with open(path, "w", encoding=encoding, newline="\n") as f:
        f.write(text)


# =========================
# Helper: canonicalize relationships (NOT used automatically)
# =========================

def canonicalize_polarized_with_in_model(model: MapModel) -> MapModel:
    """
    This function exists for *developer-only* remediation workflows.
    V1 runtime rules are strict; import rejects non-canonical ordering.
    If you want a repair tool later, call this intentionally (but do not wire into UI without spec permission).
    """
    from models import Relationship, MapModel as MM  # local import to avoid cycles

    new_rels = []
    for r in model.relationships:
        if r.type == "polarized_with":
            a, b = canonicalize_polarized_endpoints(r.source_part_id, r.target_part_id)
            new_rels.append(Relationship(id=r.id, source_part_id=a, target_part_id=b, type=r.type))
        else:
            new_rels.append(r)

    return MM(
        schema_version=model.schema_version,
        map_id=model.map_id,
        title=model.title,
        parts=model.parts,
        relationships=new_rels,
        trailhead=model.trailhead,
    )
