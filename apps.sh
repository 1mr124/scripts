#!/usr/bin/env bash

selectedAi=$(echo -e "twitter\ntweetDeck\nbrainLab\nspotify\nwhatsApp\nsoundCloud\nyouTubeStudio\nwarMap\nslack" | dmenu -p "Select an App:")

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
	exec google-chrome-stable --profile-directory="Profile 9" --app=https://twitter.com/home &
    ;;
  whatsApp)
        exec google-chrome-stable --profile-directory="Default" --app=https://web.whatsapp.com/ &
    ;;
  soundCloud)
	exec google-chrome-stable --profile-directory="Default" --app=https://soundCloud.com/you/likes &
    ;;
  warMap)
	exec google-chrome-stable --profile-directory="Profile 9" --app=https://egypt.liveuamap.com/ar &
    ;;
  youTubeStudio)
        exec google-chrome-stable --profile-directory="Default" --app=https://studio.youtube.com/channel/UCwVrRFtadPEZeP1KvdvyaVQ &
    ;;
  tweetDeck)
	exec google-chrome-stable --profile-directory="Default" --app=https://x.com/i/tweetdeck &
    ;;
  brainLab)
	exec google-chrome-stable --profile-directory="Profile 3" --app=file:////home/mr124/Documents/Projects/BrainLab/old/BrainLab/templates/mainPage.html &
    ;;
  spotify)
	exec google-chrome-stable --profile-directory="Default" --app=https://open.spotify.com/ &
    ;;
  slack)
        exec google-chrome-stable --profile-directory="Default" --app=https://app.slack.com/client/T07NVCKSQG1/C07N25XVCNB &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

