#!/bin/bash

# Paths
PACKAGE_DIR="/home/mr124/void-packages"
REPO_DIR="$PACKAGE_DIR/hostdir/binpkgs/nonfree"

# Function to update Discord
update_discord() {
    cd $PACKAGE_DIR
    git pull
    ./xbps-src clean discord
    cd srcpkgs/discord
    ../../xbps-src pkg discord
    sudo xbps-install --repository=$REPO_DIR discord
}

# Function to update Google Chrome
update_google_chrome() {
    cd $PACKAGE_DIR
    git pull
    ./xbps-src clean google-chrome
    cd srcpkgs/google-chrome
    ../../xbps-src pkg google-chrome
    sudo xbps-install --repository=$REPO_DIR google-chrome
}

# Use dmenu to display options and get user input
choice=$(echo -e "Update Discord\nUpdate Google Chrome\nUpdate Both" | dmenu -i -p "Choose an option:")

# Execute based on the choice
case $choice in
    "Update Discord")
        update_discord
        ;;
    "Update Google Chrome")
        update_google_chrome
        ;;
    "Update Both")
        update_discord
        update_google_chrome
        ;;
    *)
        echo "Invalid choice. Exiting."
        ;;
esac
