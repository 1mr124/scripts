#!/bin/bash

WORD=$1
DELAY=${2:-0.1}
COLUMNS=$(tput cols)
LINES=$(tput lines)

clear
while true; do
    for (( i=0; i<${#WORD}; i++ )); do
        CHAR=${WORD:$i:1}
        POS_COL=$((RANDOM % COLUMNS))
        POS_ROW=$((RANDOM % LINES))
        tput cup $POS_ROW $POS_COL
        echo -ne "\e[32m$CHAR\e[0m"
        sleep $DELAY
    done
    tput cup 0 0
done
