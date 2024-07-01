#!/usr/bin/env zsh

# Function to check if a string is numeric
isNumeric() {
    [[ "$1" =~ ^[0-9]+$ ]]
}

# Check if the argument is numeric First
if isNumeric "$1"; then
        watch -n $(("$1*60")) "sayit.py '$1 minutes has passed Sir.'"
else
    echo "$1 is not a numeric value."
fi
