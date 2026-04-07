from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

print("DEBUG ENV PATH:", ENV_PATH)
print("DEBUG KEY PREFIX:", OPENAI_API_KEY[:12] if OPENAI_API_KEY else "MISSING")
print("DEBUG KEY SUFFIX:", OPENAI_API_KEY[-6:] if OPENAI_API_KEY else "MISSING")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is missing. Check your .env file.")

DATA_DIR = "data"
OUTPUT_DIR = f"{DATA_DIR}/outputs"
CACHE_DIR = f"{DATA_DIR}/cache"
LOG_DIR = f"{DATA_DIR}/logs"