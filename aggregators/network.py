import json
from paths import SNAPSHOTS_DIR, AGGREGATES_DIR

OUTPUT_DIR = AGGREGATES_DIR / "network"
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

        interfaces.append({
            "snapshot": snapshot.name,
            "raw": ip_file.read_text().splitlines()
        })

        ports.append({
            "snapshot": snapshot.name,
            "routes": route_file.read_text().splitlines(),
            "open_ports": ports_file.read_text().splitlines(),
        })

    output = {
        "type": "network",
        "source_snapshots": snapshots,
        "interfaces": interfaces,
        "ports_routes": ports,
    }

    with (OUTPUT_DIR / "network.json").open("w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    aggregate_network()
