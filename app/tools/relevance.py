from __future__ import annotations

from typing import Dict, List


OBSERVABILITY_KEYWORDS = {
    "observability",
    "apm",
    "application performance monitoring",
    "monitoring",
    "logs",
    "logging",
    "tracing",
    "distributed tracing",
    "infrastructure monitoring",
    "error tracking",
    "incident response",
    "telemetry",
    "metrics",
    "rum",
    "real user monitoring",
    "cloud monitoring",
    "sre",
    "devops",
}


VENDOR_KEYWORDS = {
    "datadog",
    "dynatrace",
    "new relic",
    "grafana",
    "elastic",
    "splunk",
    "honeycomb",
    "appdynamics",
    "sumo logic",
    "openobserve",
    "sigNoz",
    "signoz",
    "chronosphere",
}

BAD_TOPIC_KEYWORDS = {
    "shopify",
    "ecommerce",
    "pos",
    "square",
    "project management",
    "jira alternative",
    "marketing automation",
}


def score_source(source: Dict[str, str]) -> int:
    haystack = " ".join([
        source.get("title", ""),
        source.get("snippet", ""),
        source.get("content", ""),
        source.get("url", ""),
    ]).lower()

    score = 0

    for keyword in OBSERVABILITY_KEYWORDS:
        if keyword in haystack:
            score += 2

    for vendor in VENDOR_KEYWORDS:
        if vendor in haystack:
            score += 3

    for bad in BAD_TOPIC_KEYWORDS:
        if bad in haystack:
            score -= 5

    return score


def is_relevant_source(source: Dict[str, str], min_score: int = 4) -> bool:
    return score_source(source) >= min_score


def filter_relevant_sources(sources: List[Dict[str, str]], min_score: int = 4) -> List[Dict[str, str]]:
    kept = []
    seen_urls = set()

    for source in sources:
        url = source.get("url", "")
        if not url or url in seen_urls:
            continue
        if is_relevant_source(source, min_score=min_score):
            kept.append(source)
            seen_urls.add(url)

    return kept