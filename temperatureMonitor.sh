#!/bin/zsh

hostname=$(hostname)

case $hostname in
  "Home")
    GPU_TEMP=$(sensors | grep -i 'edge:' | awk '{print $2}' | tr -d '+°C')
    CPU_TEMP=$(sensors | grep -i 'temp1:' | awk '{print substr($2, 1, length($2)-2)}' | tr -d '+' | paste -sd ',' -)
    echo "CPU:"$CPU_TEMP"|""GPU:"$GPU_TEMP 🥵
    ;;
  "Mr12Lab")
    GPU_TEMP=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)
    CPU_TEMP=$(sensors | grep 'Core' | awk '{print int($3)}' | paste -sd ',')
    echo "CPU:"$CPU_TEMP"|""GPU:"$GPU_TEMP 🥵
    ;;
  *)
    echo "Unknown hostname. Performing default task..."
    # Add your default commands here
    ;;
esac
