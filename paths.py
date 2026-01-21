from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
SNAPSHOTS_DIR = DATA_DIR / "snapshots"
AGGREGATES_DIR = DATA_DIR / "aggregates"

AGGREGATES_DIR.mkdir(parents=True, exist_ok=True)
