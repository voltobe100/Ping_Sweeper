import os
import platform
import argparse
import json
import subprocess
import nmap
from ipaddress import ip_network

def ping_host(ip):
    """Ping a single host to check if it's online."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def scan_subnet(subnet):
    """Scan a subnet and return a list of active hosts."""
    active_hosts = []
    for ip in ip_network(subnet).hosts():
        ip = str(ip)
        if ping_host(ip):
            active_hosts.append(ip)
    return active_hosts

def nmap_scan(ip):
    """Perform an Nmap scan on a single IP address."""
    nm = nmap.PortScanner()
    nm.scan(ip, arguments="-O")
    return nm[ip] if ip in nm.all_hosts() else {}

def save_log(results):
    """Save results to a log file."""
    with open("ping_sweeper.log", "a") as log_file:
        log_file.write(json.dumps(results, indent=4) + "\n")

def main():
    parser = argparse.ArgumentParser(description="Ping Sweeper - Scan a Subnet for Active Devices")
    parser.add_argument("--subnet", required=True, help="Subnet to scan (e.g., 192.168.1.0/24)")
    parser.add_argument("--nmap", action="store_true", help="Perform an Nmap scan for additional details")
    parser.add_argument("--log", action="store_true", help="Save results to a log file")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()
    print(f"[+] Scanning subnet: {args.subnet}")

    active_hosts = scan_subnet(args.subnet)
    results = {"subnet": args.subnet, "active_hosts": active_hosts}

    if args.nmap:
        results["nmap_scan"] = {ip: nmap_scan(ip) for ip in active_hosts}

    if args.json:
        print(json.dumps(results, indent=4))
    else:
        for ip in active_hosts:
            print(f"{ip} - Online")

    if args.log:
        save_log(results)

if __name__ == "__main__":
    main()
