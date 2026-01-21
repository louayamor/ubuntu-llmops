import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS_DIR = PROJECT_ROOT / "data" / "snapshots"
OUTPUT_DIR = PROJECT_ROOT / "data" / "aggregates" / "system"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def aggregate_system():
    snapshots = []
    memory_records = []
    disk_records = []

    for snapshot in SNAPSHOTS_DIR.iterdir():
        mem_file = snapshot / "system" / "memory.txt"
        disk_file = snapshot / "system" / "disk.txt"
        if not mem_file.exists() or not disk_file.exists():
            continue
        snapshots.append(snapshot.name)

        with mem_file.open() as f:
            lines = f.read().splitlines()
            memory_records.append({"snapshot": snapshot.name, "raw": lines})

        with disk_file.open() as f:
            lines = f.read().splitlines()
            disk_records.append({"snapshot": snapshot.name, "raw": lines})

    output = {
        "type": "system_metrics",
        "source_snapshots": snapshots,
        "memory_snapshots": memory_records,
        "disk_snapshots": disk_records
    }

    with (AGGREGATES_DIR / "system_metrics.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_system()
