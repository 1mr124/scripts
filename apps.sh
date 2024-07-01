#!/usr/bin/env bash

selectedAi=$(echo -e "twitter\nTweetDeck\nwhatsApp\nyouTubeStudio\nwarMap" | dmenu -p "Select an App:")

'''
2-Temp
3-No
4-rewind
6-pubg
7-black
Default - gleedbeso
'''
case $selectedAi in
  twitter)
	exec google-chrome-stable --profile-directory="Profile 4" --app=https://twitter.com/home &
    ;;
  whatsApp)
        exec google-chrome-stable --profile-directory="Profile 3" --app=https://web.whatsapp.com/ &
    ;;
  warMap)
	exec google-chrome-stable --profile-directory="Profile 3" --app=https://egypt.liveuamap.com/ar &
    ;;
  youTubeStudio)
        exec google-chrome-stable --profile-directory="Default" --app=https://studio.youtube.com/channel/UCwVrRFtadPEZeP1KvdvyaVQ &
    ;;
  TweetDeck)
	      exec google-chrome-stable --profile-directory="Profile 6" --app=https://x.com/i/tweetdeck &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

