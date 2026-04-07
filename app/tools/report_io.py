from __future__ import annotations

import os
from app.config import OUTPUT_DIR


def write_report(markdown_text: str, filename: str = "report.md") -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    return output_path