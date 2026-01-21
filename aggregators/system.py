import json
from paths import SNAPSHOTS_DIR, AGGREGATES_DIR

OUTPUT_DIR = AGGREGATES_DIR / "system"
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

        memory_records.append({
            "snapshot": snapshot.name,
            "raw": mem_file.read_text().splitlines()
        })

        disk_records.append({
            "snapshot": snapshot.name,
            "raw": disk_file.read_text().splitlines()
        })

    output = {
        "type": "system_metrics",
        "source_snapshots": snapshots,
        "memory_snapshots": memory_records,
        "disk_snapshots": disk_records,
    }

    with (OUTPUT_DIR / "system_metrics.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_system()
