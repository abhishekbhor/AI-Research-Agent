from __future__ import annotations

from app.state import AgentState
from app.tools.spreadsheet import write_comparison_sheet


def build_sheet_node(state: AgentState) -> AgentState:
    rows = state.get("comparison_rows", [])
    path = write_comparison_sheet(rows)

    return {
        **state,
        "spreadsheet_path": path,
        "status": "sheet_built",
    }