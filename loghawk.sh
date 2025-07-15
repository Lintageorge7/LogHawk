#!/bin/bash

# Check if file path was provided
if [ -z "$1" ]; then
    echo "Usage: ./loghawk.sh /path/to/logfile"
    exit 1
fi

FILE="$1"

echo "[🔐] Checking for failed SSH logins..."
grep "Failed password" "$FILE" | awk '{print $(NF-3)}' | sort | uniq -c | awk '$1 > 5 {print "⚠️  " $1 " failed login attempts from " $2}'

echo "[🔥] Checking for system errors..."
grep -E "ERROR|CRITICAL" "$FILE"

echo "[🦠] Checking for suspicious script activity..."
grep -E "wget|curl|bash|\.sh|/tmp" "$FILE"
