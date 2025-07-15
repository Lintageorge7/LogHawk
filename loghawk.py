#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        sys.exit(1)

def detect_failed_logins(lines):
    print("\n[🔐] Detecting failed logins...")
    failed_logins = defaultdict(int)
    for line in lines:
        if "Failed password" in line or "401" in line:
            match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
            if match:
                failed_logins[match.group()] += 1
    for ip, count in failed_logins.items():
        if count >= 2:
            print(f"⚠️  {count} failed login attempts from {ip}")

def detect_traffic_spikes(lines):
    print("\n[🌐] Detecting traffic spikes...")
    traffic = defaultdict(int)
    for line in lines:
        match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
        if match:
            traffic[match.group()] += 1
    for ip, count in traffic.items():
        if count > 100:
            print(f"⚠️  {ip} made {count} requests")

def detect_critical_errors(lines):
    print("\n[🔥] Detecting system errors...")
    for line in lines:
        if "CRITICAL" in line or "ERROR" in line:
            print(f"❗ {line.strip()}")

def detect_script_activity(lines):
    print("\n[🦠] Detecting suspicious script activity...")
    keywords = ["curl", "wget", "/tmp", ".sh", "bash", "nc"]
    for line in lines:
        if any(k in line for k in keywords):
            print(f"🚩 Suspicious: {line.strip()}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 loghawk.py /path/to/logfile.log")
        sys.exit(1)

    log_file = sys.argv[1]
    lines = read_log(log_file)

    detect_failed_logins(lines)
    detect_traffic_spikes(lines)
    detect_critical_errors(lines)
    detect_script_activity(lines)

if __name__ == "__main__":
    main()
