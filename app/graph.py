from __future__ import annotations

from langgraph.graph import START, END, StateGraph
from app.state import AgentState
from app.nodes.planner import planner_node
from app.nodes.search import search_node
from app.nodes.fetch_sources import fetch_sources_node
from app.nodes.extract import extract_node
from app.nodes.validate import validate_node
from app.nodes.build_sheet import build_sheet_node
from app.nodes.write_report import write_report_node


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("search", search_node)
    graph.add_node("fetch_sources", fetch_sources_node)
    graph.add_node("extract", extract_node)
    graph.add_node("validate", validate_node)
    graph.add_node("build_sheet", build_sheet_node)
    graph.add_node("write_report", write_report_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "search")
    graph.add_edge("search", "fetch_sources")
    graph.add_edge("fetch_sources", "extract")
    graph.add_edge("extract", "validate")
    graph.add_edge("validate", "build_sheet")
    graph.add_edge("build_sheet", "write_report")
    graph.add_edge("write_report", END)

    return graph.compile()