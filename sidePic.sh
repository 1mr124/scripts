#!/usr/bin/env bash

#


# Specify the path to the folder
folder_path="/home/mr124/Pictures/maze"

# Get a list of files in the folder
files=("$folder_path"/*)

# Check if there are any files in the folder
if [ ${#files[@]} -eq 0 ]; then
  echo "No files found in the folder."
  exit 1
fi

# Get a random index within the range of the number of files
random_index=$((RANDOM % ${#files[@]}))

# Get the random file using the random index
random_file="${files[$random_index]}"

feh $random_file &
