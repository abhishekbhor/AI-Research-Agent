from __future__ import annotations

from app.graph import build_graph


def main() -> None:
    graph = build_graph()
    goal = "Analyze top observability platforms for enterprise engineering teams"

    result = graph.invoke({
        "goal": goal,
        "errors": [],
        "usage": {},
    })

    print("\nResearch complete")
    print(f"Status: {result.get('status')}")
    print(f"Report: {result.get('report_path')}")
    print(f"Spreadsheet: {result.get('spreadsheet_path')}")


if __name__ == "__main__":
    main()