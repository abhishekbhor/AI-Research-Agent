from __future__ import annotations

from fastapi import FastAPI, HTTPException
from app.graph import build_graph
from app.models import ResearchRequest, ResearchResponse

app = FastAPI(title="AI Research Agent")
graph = build_graph()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/research/run", response_model=ResearchResponse)
def run_research(request: ResearchRequest) -> ResearchResponse:
    try:
        result = graph.invoke({"goal": request.goal, "errors": [], "usage": {}})
        return ResearchResponse(
            goal=result.get("goal", request.goal),
            plan=result.get("plan", []),
            spreadsheet_path=result.get("spreadsheet_path", ""),
            report_path=result.get("report_path", ""),
            status=result.get("status", "unknown"),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc