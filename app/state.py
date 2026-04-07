from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class AgentState(TypedDict, total=False):
    goal: str
    plan: List[str]
    queries: List[str]
    sources: List[Dict[str, Any]]
    fetched_sources: List[Dict[str, Any]]
    extracted_facts: List[Dict[str, Any]]
    comparison_rows: List[Dict[str, Any]]
    report_md: str
    spreadsheet_path: str
    report_path: str
    usage: Dict[str, Any]
    errors: List[str]
    status: str