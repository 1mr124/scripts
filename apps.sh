#!/usr/bin/env bash

selectedAi=$(echo -e "Twitter\nWarMap" | dmenu -p "Select an App:")


case $selectedAi in
  Twitter)
	exec google-chrome-stable --profile-directory="Profile 2" --app=https://twitter.com/home &
    ;;
  WarMap)
	exec google-chrome-stable --profile-directory="Default" --app=https://egypt.liveuamap.com/ar &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

