#!/bin/bash

# Define a regex pattern for a URL with common image formats
url_regex="^(http|https|ftp)://.*"

# Function to open an image URL directly with feh
open_with_feh() {
    local url="$1"
    if feh "$url" >/dev/null 2>&1; then
        echo "Logging - Opened direct using feh"
        return 0
    else
        return 1
    fi
}

# Function to download an image to a temp folder and open it with feh
download_and_open() {
    local url="$1"
    local temp_file=$(mktemp /tmp/feh_image.XXXXXX)

    # Download the image
    if curl -s "$url" -o "$temp_file"; then
        # Open the downloaded image with feh
        echo "Logging - Opened after download using feh"
        feh "$temp_file"
        rm -f "$temp_file" # Clean up the temp file
    else
        echo "Failed to download the image."
    fi
}

# Determine if the script is running in a terminal
if [[ -t 1 ]]; then
    echo "Running from terminal"

    while true; do
        # Prompt for input
        read -p "Enter URL (or type 'exit' to quit): " url

        # Check if the user wants to exit
        if [ "$url" == "exit" ]; then
            echo "Exiting..."
            break
        fi

        # Remove any single quotes from the URL
        url=$(echo "$url" | tr -d "'")

        # Check if the URL matches the pattern
        if [[ $url =~ $url_regex ]]; then
            # Try to open the URL directly
            if ! open_with_feh "$url"; then
                # If direct opening fails, download and open
                echo "Logging - Feh has failed"
                download_and_open "$url"
            fi
        else
            echo "Invalid URL or not an image."
        fi
    done
else
    # Check if clipboard content is a URL
    clipboard=$(xclip -o)
    if [[ $clipboard =~ $url_regex ]]; then
        # Try to open the URL from the clipboard directly
        if ! open_with_feh "$clipboard"; then
            # If direct opening fails, download and open
            download_and_open "$clipboard"
        fi
    else
        echo "Clipboard does not contain a valid image URL."
    fi
fi
