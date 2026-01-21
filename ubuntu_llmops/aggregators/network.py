import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS_DIR = PROJECT_ROOT / "data" / "snapshots"
OUTPUT_DIR = PROJECT_ROOT / "data" / "aggregates" / "network"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def aggregate_network():
    snapshots = []
    interfaces = []
    ports = []

    for snapshot in SNAPSHOTS_DIR.iterdir():
        ip_file = snapshot / "network" / "ip.txt"
        route_file = snapshot / "network" / "routes.txt"
        ports_file = snapshot / "network" / "ports.txt"
        if not ip_file.exists() or not route_file.exists() or not ports_file.exists():
            continue
        snapshots.append(snapshot.name)

        with ip_file.open() as f:
            interfaces.append({"snapshot": snapshot.name, "raw": f.read().splitlines()})
        with route_file.open() as f:
            routes = f.read().splitlines()
        with ports_file.open() as f:
            open_ports = f.read().splitlines()

        ports.append({"snapshot": snapshot.name, "routes": routes, "open_ports": open_ports})

    output = {
        "type": "network",
        "source_snapshots": snapshots,
        "interfaces": interfaces,
        "ports_routes": ports
    }

    with (AGGREGATES_DIR / "network.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_network()
