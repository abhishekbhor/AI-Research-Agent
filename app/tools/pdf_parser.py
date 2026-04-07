from __future__ import annotations

from typing import Dict
import fitz


def parse_pdf(file_path: str, max_pages: int = 10) -> Dict[str, str | int]:
    doc = fitz.open(file_path)
    text_parts = []
    page_count = min(len(doc), max_pages)

    for i in range(page_count):
        page = doc[i]
        text_parts.append(page.get_text())

    doc.close()

    return {
        "file_path": file_path,
        "page_count": page_count,
        "text": "\n".join(text_parts),
    }