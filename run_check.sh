#!/bin/bash
# Check RootedCON for free virtual CTFs
# Runs both Python and Node.js monitors

cd /Users/statick/apps/ctf

echo "=== Running Python monitor ==="
/usr/bin/python3 /Users/statick/apps/ctf/rootedcon_monitor.py

echo "=== Running Browser monitor ==="
/usr/local/bin/node /Users/statick/apps/ctf/rootedcon_monitor_browser.js
