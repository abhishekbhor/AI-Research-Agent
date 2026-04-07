from __future__ import annotations

import json
from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.state import AgentState

client = OpenAI(api_key=OPENAI_API_KEY)


EXTRACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "company": {"type": "string"},
        "product": {"type": "string"},
        "icp": {"type": "string"},
        "core_strengths": {"type": "array", "items": {"type": "string"}},
        "weaknesses": {"type": "array", "items": {"type": "string"}},
        "ai_capabilities": {"type": "array", "items": {"type": "string"}},
        "pricing_notes": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "string"},
    },
    "required": [
        "company",
        "product",
        "icp",
        "core_strengths",
        "weaknesses",
        "ai_capabilities",
        "pricing_notes",
        "confidence",
    ],
    "additionalProperties": False,
}

def extract_node(state: AgentState) -> AgentState:
    sources = state.get("fetched_sources", [])
    extracted_facts = []
    comparison_rows = []
    errors = state.get("errors", [])

    for source in sources:
        prompt = f"""
You are extracting competitor research for observability platforms.
Use only facts supported by the source text.
If a field is missing, return an empty string or empty list.
Do not infer pricing, AI features, or weaknesses unless explicitly supported.

Return strict JSON matching this schema.

Title: {source.get('title', '')}
Page title: {source.get('page_title', '')}
URL: {source.get('url', '')}
Snippet: {source.get('snippet', '')}
Source text:
{source.get('content', '')}
""".strip()

        try:
            response = client.responses.create(
                model=OPENAI_MODEL,
                input=prompt,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "competitor_extract",
                        "schema": EXTRACTION_SCHEMA,
                        "strict": True,
                    }
                },
            )

            content = response.output_text.strip()
            parsed = json.loads(content)

            extracted_facts.append({
                "source": source,
                "content": parsed,
            })

            comparison_rows.append({
                "Company": parsed.get("company", ""),
                "Product": parsed.get("product", ""),
                "ICP": parsed.get("icp", ""),
                "Core strengths": " | ".join(parsed.get("core_strengths", [])),
                "Weaknesses": " | ".join(parsed.get("weaknesses", [])),
                "AI capabilities": " | ".join(parsed.get("ai_capabilities", [])),
                "Pricing notes": " | ".join(parsed.get("pricing_notes", [])),
                "Confidence": parsed.get("confidence", ""),
                "Evidence URL": source.get("url", ""),
                "Date accessed": source.get("source_date", ""),
            })
        except Exception as exc:
            errors.append(f"Extraction failed for {source.get('url', '')}: {exc}")

    return {
        **state,
        "extracted_facts": extracted_facts,
        "comparison_rows": comparison_rows,
        "errors": errors,
        "status": "extracted",
    }