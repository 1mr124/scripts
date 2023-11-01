#!/bin/bash

interface="eth0"  # Replace with your specific network interface

read -r rx_bytes tx_bytes < <(cat "/sys/class/net/$interface/statistics/rx_bytes" "/sys/class/net/$interface/statistics/tx_bytes")
sleep 1
read -r new_rx_bytes new_tx_bytes < <(cat "/sys/class/net/$interface/statistics/rx_bytes" "/sys/class/net/$interface/statistics/tx_bytes")

rx_speed=$((new_rx_bytes - rx_bytes))
tx_speed=$((new_tx_bytes - tx_bytes))
rx_speed=$((rx_speed * 8))
tx_speed=$((tx_speed * 8))

echo "down_speed=$rx_speed up_speed=$tx_speed"
