from __future__ import annotations

from app.state import AgentState
from app.tools.report_io import write_report


def write_report_node(state: AgentState) -> AgentState:
    goal = state.get("goal", "")
    plan = state.get("plan", [])
    rows = state.get("comparison_rows", [])
    errors = state.get("errors", [])

    lines = [
        "# Research Report\n",
        f"## Goal\n{goal}\n",
        "## Research Plan",
    ]
    lines.extend([f"- {item}" for item in plan])
    lines.append("\n## Comparison Summary")

    if not rows:
        lines.append("No high-confidence relevant competitors were extracted.")

    for row in rows:
        lines.append(f"### {row.get('Company', 'Unknown')} - {row.get('Product', '')}")
        lines.append(f"- ICP: {row.get('ICP', '')}")
        lines.append(f"- Strengths: {row.get('Core strengths', '')}")
        lines.append(f"- Weaknesses: {row.get('Weaknesses', '')}")
        lines.append(f"- AI capabilities: {row.get('AI capabilities', '')}")
        lines.append(f"- Pricing notes: {row.get('Pricing notes', '')}")
        lines.append(f"- Confidence: {row.get('Confidence', '')}")
        lines.append(f"- Evidence: {row.get('Evidence URL', '')}\n")

    if errors:
        lines.append("## Errors / Gaps")
        lines.extend([f"- {err}" for err in errors])

    markdown = "\n".join(lines)
    path = write_report(markdown)

    return {
        **state,
        "report_md": markdown,
        "report_path": path,
        "status": "completed",
    }