from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from models import MapModel, Part, Relationship, Trailhead, PartCategory, RelationshipType


# =========================
# Error Model (No User Content)
# =========================

@dataclass(frozen=True, slots=True)
class ValidationIssue:
    """
    Privacy rule: must not include user content (labels/trailhead text/etc).
    Provide only a stable code + a structural path.
    """
    code: str
    path: str


class ValidationError(Exception):
    """
    Raised when strict validation fails.
    """
    def __init__(self, issues: Sequence[ValidationIssue]):
        super().__init__("Validation failed")
        self.issues = list(issues)


# =========================
# Constants (V1)
# =========================

ALLOWED_PART_CATEGORIES: Set[str] = {"Manager", "Firefighter", "Exile", "SelfLike", "Other"}
ALLOWED_RELATIONSHIP_TYPES: Set[str] = {"protects", "polarized_with"}

EXPORT_SCHEMA_VERSION: str = "1.0.0"


# =========================
# Utilities
# =========================

def _is_str(x: Any) -> bool:
    return isinstance(x, str)

def _is_nonempty_str(x: Any) -> bool:
    return isinstance(x, str) and x.strip() != ""

def _is_list(x: Any) -> bool:
    return isinstance(x, list)

def _is_dict(x: Any) -> bool:
    return isinstance(x, dict)

def _unknown_keys(obj: Dict[str, Any], allowed: Set[str]) -> Set[str]:
    return set(obj.keys()) - allowed

def _path(parent: str, child: str) -> str:
    if not parent:
        return child
    return f"{parent}.{child}"

def _idx_path(parent: str, idx: int) -> str:
    return f"{parent}[{idx}]"

def _semver_is_1_x_x(s: str) -> bool:
    # Accept only "1.x.x" strictly numeric segments.
    parts = s.split(".")
    if len(parts) != 3:
        return False
    if parts[0] != "1":
        return False
    return all(p.isdigit() for p in parts)

def canonicalize_polarized_endpoints(a: str, b: str) -> Tuple[str, str]:
    """
    Deterministic endpoint ordering for 'polarized_with' relationships.
    V1 rule: stored once, deterministic endpoint ordering.
    We use lexicographic ordering on part IDs.
    """
    return (a, b) if a <= b else (b, a)


# =========================
# Dict-level Strict Validation (Unknown fields forbidden)
# =========================

def validate_map_dict_strict(map_dict: Any) -> MapModel:
    """
    Strict validation for incoming JSON-like dict.
    Unknown fields forbidden everywhere.
    Raises ValidationError with privacy-safe issues.
    Returns MapModel (dataclasses) on success.
    """
    issues: List[ValidationIssue] = []

    if not _is_dict(map_dict):
        raise ValidationError([ValidationIssue(code="TYPE_NOT_OBJECT", path="$")])

    # Top-level keys
    allowed_top = {"schema_version", "map_id", "title", "parts", "relationships", "trailhead"}
    extra = _unknown_keys(map_dict, allowed_top)
    if extra:
        issues.append(ValidationIssue(code="UNKNOWN_FIELD", path="$"))

    # Required fields presence
    for k in allowed_top:
        if k not in map_dict:
            issues.append(ValidationIssue(code="MISSING_FIELD", path=_path("$", k)))

    if issues:
        raise ValidationError(issues)

    schema_version = map_dict.get("schema_version")
    if not _is_nonempty_str(schema_version):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.schema_version"))
    else:
        if not _semver_is_1_x_x(schema_version):
            issues.append(ValidationIssue(code="SCHEMA_VERSION_NOT_1_X_X", path="$.schema_version"))

    map_id = map_dict.get("map_id")
    if not _is_nonempty_str(map_id):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.map_id"))

    title = map_dict.get("title")
    if not _is_nonempty_str(title):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.title"))

    # parts
    parts_raw = map_dict.get("parts")
    if not _is_list(parts_raw):
        issues.append(ValidationIssue(code="TYPE_NOT_LIST", path="$.parts"))
        parts_raw = []
    parts: List[Part] = []
    seen_part_ids: Set[str] = set()

    allowed_part = {"id", "label", "category"}
    for i, p in enumerate(parts_raw):
        p_path = _idx_path("$.parts", i)
        if not _is_dict(p):
            issues.append(ValidationIssue(code="TYPE_NOT_OBJECT", path=p_path))
            continue
        if _unknown_keys(p, allowed_part):
            issues.append(ValidationIssue(code="UNKNOWN_FIELD", path=p_path))

        for k in allowed_part:
            if k not in p:
                issues.append(ValidationIssue(code="MISSING_FIELD", path=_path(p_path, k)))

        pid = p.get("id")
        if not _is_nonempty_str(pid):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(p_path, "id")))
            pid = None
        else:
            if pid in seen_part_ids:
                issues.append(ValidationIssue(code="DUPLICATE_ID", path=_path(p_path, "id")))
            else:
                seen_part_ids.add(pid)

        label = p.get("label")
        if not _is_nonempty_str(label):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(p_path, "label")))

        cat = p.get("category")
        if not _is_str(cat):
            issues.append(ValidationIssue(code="TYPE_NOT_STRING", path=_path(p_path, "category")))
            cat_val: Optional[PartCategory] = None
        else:
            if cat not in ALLOWED_PART_CATEGORIES:
                issues.append(ValidationIssue(code="INVALID_ENUM", path=_path(p_path, "category")))
                cat_val = None
            else:
                cat_val = cat  # type: ignore[assignment]

        if pid is not None and _is_nonempty_str(label) and cat_val is not None:
            parts.append(Part(id=pid, label=label, category=cat_val))

    # trailhead
    trail_raw = map_dict.get("trailhead")
    if not _is_dict(trail_raw):
        issues.append(ValidationIssue(code="TYPE_NOT_OBJECT", path="$.trailhead"))
        trail_raw = {}

    allowed_trail = {"trigger", "dominant_protector_patterns", "core_vulnerability_themes"}
    if _is_dict(trail_raw) and _unknown_keys(trail_raw, allowed_trail):
        issues.append(ValidationIssue(code="UNKNOWN_FIELD", path="$.trailhead"))

    for k in allowed_trail:
        if k not in trail_raw:
            issues.append(ValidationIssue(code="MISSING_FIELD", path=_path("$.trailhead", k)))

    trigger = trail_raw.get("trigger")
    if not _is_nonempty_str(trigger):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.trailhead.trigger"))
        trigger = ""

    dpp = trail_raw.get("dominant_protector_patterns")
    if not _is_list(dpp):
        issues.append(ValidationIssue(code="TYPE_NOT_LIST", path="$.trailhead.dominant_protector_patterns"))
        dpp = []
    else:
        for j, item in enumerate(dpp):
            if not _is_nonempty_str(item):
                issues.append(ValidationIssue(
                    code="NONEMPTY_STRING_REQUIRED",
                    path=_idx_path("$.trailhead.dominant_protector_patterns", j),
                ))

    cvt = trail_raw.get("core_vulnerability_themes")
    if not _is_list(cvt):
        issues.append(ValidationIssue(code="TYPE_NOT_LIST", path="$.trailhead.core_vulnerability_themes"))
        cvt = []
    else:
        for j, item in enumerate(cvt):
            if not _is_nonempty_str(item):
                issues.append(ValidationIssue(
                    code="NONEMPTY_STRING_REQUIRED",
                    path=_idx_path("$.trailhead.core_vulnerability_themes", j),
                ))

    trailhead = Trailhead(
        trigger=trigger if _is_str(trigger) else "",
        dominant_protector_patterns=[x for x in dpp if _is_nonempty_str(x)],
        core_vulnerability_themes=[x for x in cvt if _is_nonempty_str(x)],
    )

    # relationships
    rels_raw = map_dict.get("relationships")
    if not _is_list(rels_raw):
        issues.append(ValidationIssue(code="TYPE_NOT_LIST", path="$.relationships"))
        rels_raw = []

    allowed_rel = {"id", "source_part_id", "target_part_id", "type"}
    relationships: List[Relationship] = []
    seen_rel_ids: Set[str] = set()
    seen_polarized_pairs: Set[Tuple[str, str]] = set()

    for i, r in enumerate(rels_raw):
        r_path = _idx_path("$.relationships", i)
        if not _is_dict(r):
            issues.append(ValidationIssue(code="TYPE_NOT_OBJECT", path=r_path))
            continue

        if _unknown_keys(r, allowed_rel):
            issues.append(ValidationIssue(code="UNKNOWN_FIELD", path=r_path))

        for k in allowed_rel:
            if k not in r:
                issues.append(ValidationIssue(code="MISSING_FIELD", path=_path(r_path, k)))

        rid = r.get("id")
        if not _is_nonempty_str(rid):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "id")))
            rid = None
        else:
            if rid in seen_rel_ids:
                issues.append(ValidationIssue(code="DUPLICATE_ID", path=_path(r_path, "id")))
            else:
                seen_rel_ids.add(rid)

        src = r.get("source_part_id")
        tgt = r.get("target_part_id")
        if not _is_nonempty_str(src):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "source_part_id")))
            src = None
        if not _is_nonempty_str(tgt):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "target_part_id")))
            tgt = None

        rtype = r.get("type")
        if not _is_str(rtype):
            issues.append(ValidationIssue(code="TYPE_NOT_STRING", path=_path(r_path, "type")))
            rtype_val: Optional[RelationshipType] = None
        else:
            if rtype not in ALLOWED_RELATIONSHIP_TYPES:
                issues.append(ValidationIssue(code="INVALID_ENUM", path=_path(r_path, "type")))
                rtype_val = None
            else:
                rtype_val = rtype  # type: ignore[assignment]

        # Structural constraints
        if src is not None and tgt is not None:
            if src == tgt:
                issues.append(ValidationIssue(code="SELF_LOOP_FORBIDDEN", path=r_path))

        # Referential integrity
        if src is not None and src not in seen_part_ids:
            issues.append(ValidationIssue(code="BAD_REFERENCE", path=_path(r_path, "source_part_id")))
        if tgt is not None and tgt not in seen_part_ids:
            issues.append(ValidationIssue(code="BAD_REFERENCE", path=_path(r_path, "target_part_id")))

        if rid is None or src is None or tgt is None or rtype_val is None:
            continue

        # polarized_with must be undirected and stored once with deterministic endpoint ordering
        if rtype_val == "polarized_with":
            a, b = canonicalize_polarized_endpoints(src, tgt)
            if (a, b) in seen_polarized_pairs:
                issues.append(ValidationIssue(code="DUPLICATE_POLARIZED_PAIR", path=r_path))
                continue
            seen_polarized_pairs.add((a, b))

            if (src, tgt) != (a, b):
                issues.append(ValidationIssue(code="POLARIZED_NOT_CANONICAL_ORDER", path=r_path))
                continue

        relationships.append(Relationship(id=rid, source_part_id=src, target_part_id=tgt, type=rtype_val))

    if issues:
        raise ValidationError(issues)

    return MapModel(
        schema_version=schema_version,
        map_id=map_id,
        title=title,
        parts=parts,
        relationships=relationships,
        trailhead=trailhead,
    )


# =========================
# Export Validation (Model -> Dict)
# =========================

def validate_map_model_for_export(model: MapModel) -> None:
    """
    Export rule: schema_version must be exactly "1.0.0".
    Also re-check relational constraints to prevent accidental drift.
    """
    issues: List[ValidationIssue] = []

    if model.schema_version != EXPORT_SCHEMA_VERSION:
        issues.append(ValidationIssue(code="EXPORT_SCHEMA_VERSION_MUST_BE_1_0_0", path="$.schema_version"))

    # Non-empty required strings (hardening)
    if not _is_nonempty_str(model.map_id):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.map_id"))
    if not _is_nonempty_str(model.title):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.title"))

    for i, p in enumerate(model.parts):
        p_path = _idx_path("$.parts", i)
        if not _is_nonempty_str(p.id):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(p_path, "id")))
        if not _is_nonempty_str(p.label):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(p_path, "label")))
        if p.category not in ALLOWED_PART_CATEGORIES:
            issues.append(ValidationIssue(code="INVALID_ENUM", path=_path(p_path, "category")))

    if not _is_nonempty_str(model.trailhead.trigger):
        issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path="$.trailhead.trigger"))
    for j, item in enumerate(model.trailhead.dominant_protector_patterns):
        if not _is_nonempty_str(item):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_idx_path("$.trailhead.dominant_protector_patterns", j)))
    for j, item in enumerate(model.trailhead.core_vulnerability_themes):
        if not _is_nonempty_str(item):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_idx_path("$.trailhead.core_vulnerability_themes", j)))

    part_ids = [p.id for p in model.parts]
    if len(set(part_ids)) != len(part_ids):
        issues.append(ValidationIssue(code="DUPLICATE_ID", path="$.parts"))

    seen_polarized: Set[Tuple[str, str]] = set()
    for i, r in enumerate(model.relationships):
        r_path = _idx_path("$.relationships", i)
        if not _is_nonempty_str(r.id):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "id")))
        if not _is_nonempty_str(r.source_part_id):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "source_part_id")))
        if not _is_nonempty_str(r.target_part_id):
            issues.append(ValidationIssue(code="NONEMPTY_STRING_REQUIRED", path=_path(r_path, "target_part_id")))
        if r.type not in ALLOWED_RELATIONSHIP_TYPES:
            issues.append(ValidationIssue(code="INVALID_ENUM", path=_path(r_path, "type")))

        if r.source_part_id == r.target_part_id:
            issues.append(ValidationIssue(code="SELF_LOOP_FORBIDDEN", path=r_path))

        if r.source_part_id not in set(part_ids):
            issues.append(ValidationIssue(code="BAD_REFERENCE", path=_path(r_path, "source_part_id")))
        if r.target_part_id not in set(part_ids):
            issues.append(ValidationIssue(code="BAD_REFERENCE", path=_path(r_path, "target_part_id")))

        if r.type == "polarized_with":
            a, b = canonicalize_polarized_endpoints(r.source_part_id, r.target_part_id)
            if (a, b) in seen_polarized:
                issues.append(ValidationIssue(code="DUPLICATE_POLARIZED_PAIR", path=r_path))
            else:
                seen_polarized.add((a, b))
            if (r.source_part_id, r.target_part_id) != (a, b):
                issues.append(ValidationIssue(code="POLARIZED_NOT_CANONICAL_ORDER", path=r_path))

    if issues:
        raise ValidationError(issues)
