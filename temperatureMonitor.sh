#!/bin/zsh

# Get CPU temperature
GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)


# Get GPU temperature
CPU_TEMP=$(sensors | grep 'Core' | awk '{print int($3)}' | paste -sd ',')

# Default values if not found
#[ -z "$CPU_TEMP" ] && CPU_TEMP="N/A"
#[ -z "$GPU_TEMP" ] && GPU_TEMP="N/A"

# Print the output
echo "CPU:"$CPU_TEMP"|""GPU:"$GPU_TEMP 🥵
