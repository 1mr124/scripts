#!/bin/bash

# Get CPU temperature
GPU_TEMP=$(sensors | grep -i 'edge:' | awk '{print $2}' | tr -d '+°C')


# Get GPU temperature
CPU_TEMP=$(sensors | grep -i 'temp1:' | awk '{print substr($2, 1, length($2)-2)}' | tr -d '+' | paste -sd ',' -
)

# Default values if not found
#[ -z "$CPU_TEMP" ] && CPU_TEMP="N/A"
#[ -z "$GPU_TEMP" ] && GPU_TEMP="N/A"

# Print the output
echo "CPU:"$CPU_TEMP"|""GPU:"$GPU_TEMP 🥵
