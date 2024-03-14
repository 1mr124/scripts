#!/usr/bin/env bash

selectedAi=$(echo -e "Twitter\nYouTubeStudio\nWarMap" | dmenu -p "Select an App:")


case $selectedAi in
  Twitter)
	exec google-chrome-stable --profile-directory="Profile 4" --app=https://twitter.com/home &
    ;;
  WarMap)
	exec google-chrome-stable --profile-directory="Default" --app=https://egypt.liveuamap.com/ar &
    ;;
  YouTubeStudio)
        exec google-chrome-stable --profile-directory="Profile 4" --app=https://studio.youtube.com/channel/UCwVrRFtadPEZeP1KvdvyaVQ &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

