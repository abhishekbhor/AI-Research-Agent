from __future__ import annotations

from app.state import AgentState
from app.tools.web_search import web_search


def search_node(state: AgentState) -> AgentState:
    queries = state.get("queries", [])
    sources = []

    for query in queries:
        sources.extend(web_search(query=query, max_results=3))

    return {
        **state,
        "sources": sources,
        "status": "searched",
    }