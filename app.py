from __future__ import annotations

import re
from collections import Counter

import streamlit as st

import io_json
from models import MapModel, Part, Relationship, Trailhead
from session_state import init_session_state, get_map, set_map, get_issues, set_issues
from validate import ValidationError


st.set_page_config(page_title="IFS Parts Mapper (V1)", layout="wide")

CATEGORY_ORDER = ["Manager", "Firefighter", "Exile", "SelfLike", "Other"]
REL_TYPE_ORDER = ["protects", "polarized_with"]


def _cat_rank(cat: str) -> int:
    try:
        return CATEGORY_ORDER.index(cat)
    except ValueError:
        return 999


def _rel_type_rank(t: str) -> int:
    try:
        return REL_TYPE_ORDER.index(t)
    except ValueError:
        return 999


def _safe_filename_component(s: str) -> str:
    s2 = re.sub(r"[^A-Za-z0-9_-]+", "_", s.strip())
    return s2[:80] if s2 else "map"


def _example_map_model_protects() -> MapModel:
    return MapModel(
        schema_version="1.0.0",
        map_id="example-map-001",
        title="Example Map V1 (protects)",
        parts=[
            Part(id="p_exile_1", label="Example part A", category="Exile"),
            Part(id="p_mgr_1", label="Example part B", category="Manager"),
        ],
        relationships=[
            Relationship(id="r1", source_part_id="p_mgr_1", target_part_id="p_exile_1", type="protects"),
        ],
        trailhead=Trailhead(
            trigger="Example trigger",
            dominant_protector_patterns=["example-pattern-1", "example-pattern-2"],
            core_vulnerability_themes=["example-theme-1"],
        ),
    )


def _example_map_model_polarized() -> MapModel:
    return MapModel(
        schema_version="1.0.0",
        map_id="example-map-002",
        title="Example Map V1 (polarized_with)",
        parts=[
            Part(id="a_part", label="Example part A", category="Manager"),
            Part(id="b_part", label="Example part B", category="Firefighter"),
        ],
        relationships=[
            Relationship(id="r1", source_part_id="a_part", target_part_id="b_part", type="polarized_with"),
        ],
        trailhead=Trailhead(
            trigger="Example trigger",
            dominant_protector_patterns=["example-pattern-1"],
            core_vulnerability_themes=["example-theme-1"],
        ),
    )


def _blank_template_model() -> MapModel:
    # Smallest validator-safe V1 template:
    # - Neutral placeholders (no interpretation)
    # - 1 placeholder Part to satisfy any non-empty constraints
    # - No relationships
    return MapModel(
        schema_version="1.0.0",
        map_id="new-map",
        title="New Map",
        parts=[
            Part(id="p1", label="PLACEHOLDER", category="Other"),
        ],
        relationships=[],
        trailhead=Trailhead(
            trigger="PLACEHOLDER",
            dominant_protector_patterns=["PLACEHOLDER"],
            core_vulnerability_themes=["PLACEHOLDER"],
        ),
    )


def _render_spec_guard() -> None:
    with st.expander("V1 Spec Guard (read-only)", expanded=True):
        st.markdown(
            """
**This tool is V1 and intentionally limited.**

**Allowed:**
- Session-only viewing of a map
- JSON import/export only

**Forbidden (hard stops):**
- “Self” as a node/category (SelfLike is allowed; Self is never a node)
- Interpretation, inference, scoring, ranking, analytics
- Autosave, telemetry, cloud sync, persistence beyond explicit JSON export
- New relationship types or extra fields beyond the canonical schema

**V1 fixed enums**
- Part categories: Manager / Firefighter / Exile / SelfLike / Other  
- Relationship types: protects / polarized_with
"""
        )


def _render_issues() -> None:
    issues = get_issues()
    if not issues:
        return
    st.error("Import failed (privacy-safe):")
    st.write([{"code": iss.code, "path": iss.path} for iss in issues])


def _round_trip_status(m: MapModel) -> str:
    try:
        exported = io_json.export_map_to_json_text(m, indent=2)
        m2 = io_json.import_map_from_json_text(exported)
        ok = (
            m2.schema_version == m.schema_version
            and len(m2.parts) == len(m.parts)
            and len(m2.relationships) == len(m.relationships)
            and m2.map_id == m.map_id
        )
        return "PASS" if ok else "FAIL"
    except Exception:
        return "FAIL"


def _render_integrity_panel() -> None:
    m = get_map()
    with st.expander("Integrity / Structure (V1)", expanded=True):
        if m is None:
            st.info("No map loaded. Import JSON (or load an example/template) to view structure.")
            return

        part_categories = Counter([p.category for p in m.parts])
        rel_types = Counter([r.type for r in m.relationships])
        polarized_pairs = sum(1 for r in m.relationships if r.type == "polarized_with")
        rt = _round_trip_status(m)

        st.write(
            {
                "schema_version": m.schema_version,
                "parts_count": len(m.parts),
                "relationships_count": len(m.relationships),
                "polarized_pairs_count": polarized_pairs,
                "round_trip_export_import": rt,
            }
        )

        st.subheader("Parts by Category")
        rows = []
        for cat in CATEGORY_ORDER:
            if cat in part_categories:
                rows.append({"category": cat, "count": int(part_categories[cat])})
        for cat in sorted([c for c in part_categories.keys() if c not in CATEGORY_ORDER]):
            rows.append({"category": cat, "count": int(part_categories[cat])})
        st.dataframe(rows, use_container_width=True, hide_index=True)

        st.subheader("Relationships by Type")
        rel_rows = []
        for t in REL_TYPE_ORDER:
            if t in rel_types:
                rel_rows.append({"type": t, "count": int(rel_types[t])})
        for t in sorted([x for x in rel_types.keys() if x not in REL_TYPE_ORDER]):
            rel_rows.append({"type": t, "count": int(rel_types[t])})
        st.dataframe(rel_rows, use_container_width=True, hide_index=True)


def _render_export_preview() -> None:
    m = get_map()
    with st.expander("Export JSON Preview (read-only)", expanded=False):
        if m is None:
            st.info("No map loaded.")
            return
        try:
            json_text = io_json.export_map_to_json_text(m, indent=2)
            st.text_area("Export JSON", value=json_text, height=320)
        except ValidationError as e:
            set_issues(e.issues)
            st.error("Export blocked by validation (privacy-safe).")
            st.write([{"code": iss.code, "path": iss.path} for iss in e.issues])


def _render_map_view() -> None:
    m = get_map()
    if m is None:
        st.info("No map loaded. Import JSON (or load an example/template) to begin.")
        return

    st.subheader("Map")
    st.write(
        {
            "schema_version": m.schema_version,
            "map_id": m.map_id,
            "title": m.title,
            "parts_count": len(m.parts),
            "relationships_count": len(m.relationships),
        }
    )

    st.subheader("Trailhead")
    st.write(
        {
            "trigger": m.trailhead.trigger,
            "dominant_protector_patterns": m.trailhead.dominant_protector_patterns,
            "core_vulnerability_themes": m.trailhead.core_vulnerability_themes,
        }
    )

    st.subheader("Parts (sorted)")
    parts_sorted = sorted(m.parts, key=lambda p: (_cat_rank(p.category), p.label.lower(), p.id.lower()))
    st.dataframe(
        [{"id": p.id, "label": p.label, "category": p.category} for p in parts_sorted],
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Relationships (sorted)")
    rels_sorted = sorted(
        m.relationships,
        key=lambda r: (_rel_type_rank(r.type), r.source_part_id.lower(), r.target_part_id.lower(), r.id.lower()),
    )
    st.dataframe(
        [
            {
                "id": r.id,
                "type": r.type,
                "source_part_id": r.source_part_id,
                "target_part_id": r.target_part_id,
            }
            for r in rels_sorted
        ],
        use_container_width=True,
        hide_index=True,
    )


def _load_model_into_session(m: MapModel) -> None:
    canonical_json = io_json.export_map_to_json_text(m, indent=2)
    m2 = io_json.import_map_from_json_text(canonical_json)
    set_map(m2)
    set_issues([])


def main() -> None:
    init_session_state()

    st.title("IFS Parts Mapper (V1)")
    st.caption("Non-clinical • phenomenological • privacy-first • session-based • JSON import/export only")

    _render_spec_guard()

    with st.sidebar:
        st.header("Import / Export")

        if st.button("Load blank template", type="secondary"):
            try:
                _load_model_into_session(_blank_template_model())
                st.success("Blank template loaded.")
            except ValidationError as e:
                set_map(None)
                set_issues(e.issues)
                st.error("Template failed validation (privacy-safe).")

        if st.button("Load example: protects", type="secondary"):
            try:
                _load_model_into_session(_example_map_model_protects())
                st.success("Example loaded.")
            except ValidationError as e:
                set_map(None)
                set_issues(e.issues)
                st.error("Example failed validation (privacy-safe).")

        if st.button("Load example: polarized_with", type="secondary"):
            try:
                _load_model_into_session(_example_map_model_polarized())
                st.success("Example loaded.")
            except ValidationError as e:
                set_map(None)
                set_issues(e.issues)
                st.error("Example failed validation (privacy-safe).")

        st.divider()

        uploaded = st.file_uploader("Import JSON (.json)", type=["json"], accept_multiple_files=False)
        if uploaded is not None:
            try:
                text = uploaded.getvalue().decode("utf-8", errors="strict")
                m = io_json.import_map_from_json_text(text)
                set_map(m)
                set_issues([])
                st.success("Imported.")
            except UnicodeDecodeError:
                set_map(None)
                set_issues([])
                st.error("Import failed: file is not valid UTF-8.")
            except ValidationError as e:
                set_map(None)
                set_issues(e.issues)

        st.divider()

        m = get_map()
        if m is None:
            st.download_button(
                "Export JSON (disabled - no map loaded)",
                data="",
                file_name="ifs_parts_map.json",
                disabled=True,
            )
        else:
            fname = f"ifs_parts_map_{_safe_filename_component(m.map_id)}.json"
            try:
                json_text = io_json.export_map_to_json_text(m, indent=2)
                st.download_button(
                    "Export JSON",
                    data=json_text.encode("utf-8"),
                    file_name=fname,
                    mime="application/json",
                )
            except ValidationError as e:
                set_issues(e.issues)
                st.download_button(
                    "Export JSON (blocked by validation)",
                    data="",
                    file_name=fname,
                    disabled=True,
                )

        st.divider()

        if st.button("Clear session map", type="secondary"):
            set_map(None)
            set_issues([])

    _render_issues()
    _render_integrity_panel()
    _render_export_preview()
    _render_map_view()


if __name__ == "__main__":
    main()
