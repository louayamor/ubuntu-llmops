import json
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS_DIR = PROJECT_ROOT / "data" / "snapshots"
OUTPUT_DIR = PROJECT_ROOT / "data" / "aggregates" / "services"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def aggregate_services():
    snapshots = []
    failed_counter = Counter()

    for snapshot in SNAPSHOTS_DIR.iterdir():
        failed_file = snapshot / "services" / "failed.txt"
        if not failed_file.exists():
            continue
        snapshots.append(snapshot.name)
        with failed_file.open() as f:
            for line in f:
                service = line.strip()
                if service:
                    failed_counter[service] += 1

    output = {
        "type": "services",
        "source_snapshots": snapshots,
        "failed_services_count": [
            {"service": svc, "count": cnt}
            for svc, cnt in failed_counter.most_common()
        ]
    }

    with (AGGREGATES_DIR / "failed_services.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_services()
