#!/bin/bash

# Get the active connection name
connection=$(nmcli -t -f NAME connection show --active | head -n 1)

# Check if a connection is active
if [ -n "$connection" ]; then
    echo "$connection"  # Use a Wi-Fi icon or customize
else
    echo "No connection"  # Use a warning icon or customize
fi
