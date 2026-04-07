from __future__ import annotations

from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.state import AgentState

client = OpenAI(api_key=OPENAI_API_KEY)


def planner_node(state: AgentState) -> AgentState:
    goal = state["goal"]

    prompt = f"""
You are a research planner.
Break the following goal into 4 concise research sub-questions.
Return only a plain newline-separated list.

Goal: {goal}
""".strip()

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt,
    )

    text = response.output_text.strip()
    plan = [line.strip("- ").strip() for line in text.splitlines() if line.strip()]

    return {
        **state,
        "plan": plan,
        "queries": plan,
        "status": "planned",
    }