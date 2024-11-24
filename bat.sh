#!/bin/bash

# Get the battery capacity
capacity=$(cat /sys/class/power_supply/BAT1/capacity)

# Get the charging status
status=$(cat /sys/class/power_supply/BAT1/status)


# Check if the battery is charging and display an icon accordingly
if [[ "$status" == "Charging" ]]; then
	echo "${capacity}🔌"	
else
	echo "${capacity}🔋"
fi
