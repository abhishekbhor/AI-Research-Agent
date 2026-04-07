from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List


class ResearchRequest(BaseModel):
    goal: str = Field(..., min_length=10)


class ResearchResponse(BaseModel):
    goal: str
    plan: List[str]
    spreadsheet_path: str
    report_path: str
    status: str