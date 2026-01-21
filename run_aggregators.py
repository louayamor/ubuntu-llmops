import json
from pathlib import Path
from datetime import datetime

from ubuntu_llmops.aggregators import logs, system, processes, services, network

PROJECT_ROOT = Path(__file__).resolve().parent
AGGREGATES_DIR = PROJECT_ROOT / "data" / "aggregates"
AGGREGATES_DIR.mkdir(parents=True, exist_ok=True)

def run_all():
    summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "aggregators_run": [],
        "output_files": [],
    }

    logs.aggregate_journal_errors()
    summary["aggregators_run"].append("logs")
    summary["output_files"].append("logs/errors_by_service.json")

    system.aggregate_system()
    summary["aggregators_run"].append("system")
    summary["output_files"].append("system/system_metrics.json")

    processes.aggregate_processes()
    summary["aggregators_run"].append("processes")
    summary["output_files"].append("processes/processes.json")

    services.aggregate_services()
    summary["aggregators_run"].append("services")
    summary["output_files"].append("services/failed_services.json")

    network.aggregate_network()
    summary["aggregators_run"].append("network")
    summary["output_files"].append("network/network.json")

    metadata_file = AGGREGATES_DIR / "metadata.json"
    with metadata_file.open("w") as f:
        json.dump(summary, f, indent=2)

    print(f"Aggregates complete. Metadata written to {metadata_file}")

if __name__ == "__main__":
    run_all()
