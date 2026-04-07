from __future__ import annotations

from typing import Any, Dict
import time


class Timer:
    def __init__(self) -> None:
        self.started_at = 0.0

    def __enter__(self) -> "Timer":
        self.started_at = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    @property
    def elapsed_ms(self) -> float:
        return round((time.perf_counter() - self.started_at) * 1000, 2)


def usage_summary() -> Dict[str, Any]:
    return {
        "latency_ms": 0,
        "estimated_cost_usd": 0,
        "notes": "Populate after adding model usage accounting.",
    }