import json
from datetime import datetime

from aggregators import logs, system, processes, services, network
from paths import AGGREGATES_DIR

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

    with (AGGREGATES_DIR / "metadata.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print("Aggregates complete")

if __name__ == "__main__":
    run_all()
