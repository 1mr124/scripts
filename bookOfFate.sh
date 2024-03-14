#!/bin/bash

# Specify the path to the folder
folder_path="/home/mr124/Documents/Pdf/CurrentlyReading"

# Get a list of pdf files in the folder
files=$(find "$folder_path" -name "*.pdf")

# Check if there are any pdf files in the folder
if [ -z "$files" ]; then
  echo "No PDF files found in the folder."
  exit 1
fi

# Get a random file using shuf
random_file=$(echo "$files" | shuf -n 1)
echo "$random_file"

# Open the random file using zathura
zathura "$random_file" &
