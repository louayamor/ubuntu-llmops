import json
from paths import SNAPSHOTS_DIR, AGGREGATES_DIR

OUTPUT_DIR = AGGREGATES_DIR / "processes"
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

        top_cpu.append({
            "snapshot": snapshot.name,
            "raw": cpu_file.read_text().splitlines()
        })

        top_mem.append({
            "snapshot": snapshot.name,
            "raw": mem_file.read_text().splitlines()
        })

    output = {
        "type": "processes",
        "source_snapshots": snapshots,
        "top_cpu_processes": top_cpu,
        "top_memory_processes": top_mem,
    }

    with (OUTPUT_DIR / "processes.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_processes()
