import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS_DIR = PROJECT_ROOT / "data" / "snapshots"
OUTPUT_DIR = PROJECT_ROOT / "data" / "aggregates" / "processes"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def aggregate_processes():
    snapshots = []
    top_cpu = []
    top_mem = []

    for snapshot in SNAPSHOTS_DIR.iterdir():
        cpu_file = snapshot / "processes" / "top_cpu.txt"
        mem_file = snapshot / "processes" / "top_mem.txt"
        if not cpu_file.exists() or not mem_file.exists():
            continue
        snapshots.append(snapshot.name)

        with cpu_file.open() as f:
            top_cpu.append({"snapshot": snapshot.name, "raw": f.read().splitlines()})
        with mem_file.open() as f:
            top_mem.append({"snapshot": snapshot.name, "raw": f.read().splitlines()})

    output = {
        "type": "processes",
        "source_snapshots": snapshots,
        "top_cpu_processes": top_cpu,
        "top_memory_processes": top_mem
    }

    with (AGGREGATES_DIR / "processes.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_processes()
