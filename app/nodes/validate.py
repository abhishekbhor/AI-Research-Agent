from __future__ import annotations

from app.state import AgentState


def validate_node(state: AgentState) -> AgentState:
    rows = state.get("comparison_rows", [])
    errors = state.get("errors", [])

    if not rows:
        errors.append("No comparison rows generated.")

    deduped = []
    seen = set()

    for row in rows:
        key = (
            row.get("Company", "").strip().lower(),
            row.get("Evidence URL", "").strip().lower(),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    high_quality = []
    for row in deduped:
        company = row.get("Company", "").strip()
        confidence = row.get("Confidence", "").strip().lower()
        if company and confidence in {"high", "medium"}:
            high_quality.append(row)

    return {
        **state,
        "comparison_rows": high_quality,
        "errors": errors,
        "status": "validated",
    }