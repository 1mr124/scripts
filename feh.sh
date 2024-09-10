#!/bin/bash


# Continue reading URLs and opening them in feh
clipboard=$(xclip -o)

# Define a regex pattern for a URL
url_regex="^(http|https|ftp)://"

# Check if the clipboard content matches the URL pattern
if [[ $clipboard =~ $url_regex ]]; then
    # Open the URL with feh
    feh "$clipboard"
else
    echo "No valid URL found in the clipboard."

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

fi
