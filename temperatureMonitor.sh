#!/bin/zsh

hostname=$(hostname)

case $hostname in
  "mr12Home")
    # Read CPU temperature from "Package id 0:"; if not available, fallback to "temp1:"
    CPU_TEMP=$(sensors | awk '/Package id 0:/ {gsub(/[+°C]/, "", $4); print $4; exit}')
    if [[ -z "$CPU_TEMP" ]]; then
      CPU_TEMP=$(sensors | grep -i 'temp1:' | awk '{gsub(/[+°C]/, "", $2); print $2; exit}')
    fi
    GPU_TEMP=$(sensors | grep -i 'edge:' | awk '{print $2}' | tr -d '+°C')
    echo "CPU:${CPU_TEMP} | GPU:${GPU_TEMP} 🥵"
    ;;
  "Mr12Lab")
    # Calculate the average CPU temperature from all "Core" readings
    CPU_TEMPS=($(sensors | grep 'Core' | awk '{gsub(/[+°C]/, "", $3); print $3}'))
    sum=0
    count=0
    for temp in "${CPU_TEMPS[@]}"; do
      (( sum += temp ))
      (( count++ ))
    done
    if (( count > 0 )); then
      avg=$(printf "%.0f" "$(echo "$sum / $count" | bc -l)")
      CPU_TEMP=${avg}
    else
      CPU_TEMP="N/A"
    fi
    GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)
    echo "CPU:${CPU_TEMP} | GPU:${GPU_TEMP} 🥵"
    ;;
  *)
    echo "Unknown hostname. Performing default task..."
    ;;
esac
