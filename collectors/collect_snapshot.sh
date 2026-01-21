#!/bin/bash
set -e

TS=$(date -u +"%Y-%m-%dT%H-%M-%SZ")
BASE="data/snapshots/$TS"

mkdir -p \
  $BASE/{logs,system,services,network,processes,hardware,security}

# ---------------- SYSTEM ----------------
uname -a > $BASE/system/kernel.txt
cat /etc/os-release > $BASE/system/os.txt
uptime -p > $BASE/system/uptime.txt
who > $BASE/system/users.txt
last -n 20 > $BASE/system/last_logins.txt

# ---------------- HARDWARE ----------------
lscpu > $BASE/hardware/cpu.txt
lsmem > $BASE/hardware/memory_layout.txt || true
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT > $BASE/hardware/blocks.txt

# ---------------- RESOURCES ----------------
free -m > $BASE/system/memory.txt
df -h > $BASE/system/disk.txt
df -i > $BASE/system/inodes.txt
vmstat 1 5 > $BASE/system/vmstat.txt

# ---------------- PROCESSES ----------------
ps aux --sort=-%cpu | head -50 > $BASE/processes/top_cpu.txt
ps aux --sort=-%mem | head -50 > $BASE/processes/top_mem.txt

# ---------------- SERVICES ----------------
systemctl list-units --type=service --state=running > $BASE/services/running.txt
systemctl list-units --type=service --state=failed > $BASE/services/failed.txt
systemctl list-unit-files --type=service > $BASE/services/enabled.txt

# ---------------- NETWORK ----------------
ip a > $BASE/network/ip.txt
ip route > $BASE/network/routes.txt
ss -tulnp > $BASE/network/ports.txt
cat /etc/resolv.conf > $BASE/network/dns.txt

# ---------------- SECURITY ----------------
dmesg -T | tail -200 > $BASE/security/dmesg_tail.txt
journalctl -p err --since "24 hours ago" > $BASE/logs/errors_24h.log
journalctl --since "24 hours ago" --output=json > $BASE/logs/journal.json

# ---------------- CLASSIC LOGS ----------------
for f in syslog auth.log kern.log; do
  [ -f /var/log/$f ] && cp /var/log/$f $BASE/logs/
done

# ---------------- METADATA ----------------
cat <<EOF > $BASE/metadata.json
{
  "snapshot_id": "$TS",
  "timestamp": "$(date +"%Y-%m-%dT%H:%M:%S")",
  "hostname": "$(hostname)",
  "os": "Ubuntu",
  "kernel": "$(uname -r)",
  "architecture": "$(uname -m)",
  "collector": {
    "name": "collect_snapshot.sh",
    "version": "v2"
  }
}
EOF

