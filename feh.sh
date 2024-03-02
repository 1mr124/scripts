#!/bin/bash


# Continue reading URLs and opening them in feh
while true; do
    # Prompt for input
    read -p "Enter URL (or type 'exit' to quit): " url

    # Check if the user wants to exit
    if [ "$url" == "exit" ]; then
        echo "Exiting..."
        break
    fi

    {
	url=$(echo $url | tr -d "'")
	feh "$url" >/dev/null 2>&1 &
    } || { 
        echo 'error'
    }
done
