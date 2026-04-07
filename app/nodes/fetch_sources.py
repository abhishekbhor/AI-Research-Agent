from __future__ import annotations

from app.state import AgentState
from app.tools.page_fetcher import fetch_page_content
from app.tools.relevance import filter_relevant_sources


def fetch_sources_node(state: AgentState) -> AgentState:
    raw_sources = state.get("sources", [])
    errors = state.get("errors", [])
    fetched_sources = []

    for source in raw_sources:
        url = source.get("url", "")
        if not url:
            continue
        try:
            page = fetch_page_content(url)
            merged = {
                **source,
                "page_title": page.get("title", ""),
                "content": page.get("content", ""),
            }
            fetched_sources.append(merged)
        except Exception as exc:
            errors.append(f"Failed to fetch {url}: {exc}")

    filtered_sources = filter_relevant_sources(fetched_sources, min_score=4)

    return {
        **state,
        "fetched_sources": filtered_sources,
        "errors": errors,
        "status": "sources_fetched",
    }