from __future__ import annotations

import os
import pandas as pd
from typing import List, Dict
from app.config import OUTPUT_DIR


def write_comparison_sheet(rows: List[Dict], filename: str = "comparison.xlsx") -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, filename)

    df = pd.DataFrame(rows)
    df.to_excel(output_path, index=False)
    return output_path