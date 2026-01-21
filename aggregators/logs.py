import json
from collections import Counter

from paths import SNAPSHOTS_DIR, AGGREGATES_DIR

OUTPUT_DIR = AGGREGATES_DIR / "logs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def aggregate_journal_errors():
    error_counter = Counter()
    source_snapshots = []

    for snapshot in SNAPSHOTS_DIR.iterdir():
        journal_file = snapshot / "logs" / "journal.json"
        if not journal_file.exists():
            continue

        source_snapshots.append(snapshot.name)

        with journal_file.open() as f:
            for line in f:
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue

                priority = entry.get("PRIORITY")
                if priority is None or int(priority) > 3:
                    continue

                unit = entry.get("_SYSTEMD_UNIT", "unknown")
                error_counter[unit] += 1

    output = {
        "type": "journal_error_aggregation",
        "source_snapshots": source_snapshots,
        "errors_by_service": [
            {"service": svc, "count": cnt}
            for svc, cnt in error_counter.most_common()
        ],
    }

    with (OUTPUT_DIR / "errors_by_service.json").open("w") as f:
        json.dump(output, f, indent=2)
