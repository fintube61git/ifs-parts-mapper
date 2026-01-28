from __future__ import annotations

from typing import List, Optional

import streamlit as st

from models import MapModel
from validate import ValidationIssue


MAP_KEY = "ifs_mapper_v1_map"
ISSUES_KEY = "ifs_mapper_v1_issues"


def init_session_state() -> None:
    if MAP_KEY not in st.session_state:
        st.session_state[MAP_KEY] = None
    if ISSUES_KEY not in st.session_state:
        st.session_state[ISSUES_KEY] = []


def get_map() -> Optional[MapModel]:
    return st.session_state.get(MAP_KEY)


def set_map(m: Optional[MapModel]) -> None:
    st.session_state[MAP_KEY] = m


def set_issues(issues: List[ValidationIssue]) -> None:
    st.session_state[ISSUES_KEY] = issues


def get_issues() -> List[ValidationIssue]:
    return st.session_state.get(ISSUES_KEY, [])
