#!/usr/bin/env bash

selectedAi=$(echo -e "Twitter\nTweetDeck\nbrainLab\nspotify\nwhatsApp\nSoundCloud\nyouTubeStudio\nwarMap" | dmenu -p "Select an App:")

'''
2-Temp
3-No
4-rewind
6-pubg
7-black
Default - gleedbeso
'''
case $selectedAi in
  Twitter)
	exec google-chrome-stable --profile-directory="Profile 4" --app=https://twitter.com/home &
    ;;
  whatsApp)
        exec google-chrome-stable --profile-directory="Profile 3" --app=https://web.whatsapp.com/ &
    ;;
  SoundCloud)
	exec google-chrome-stable --profile-directory="Default" --app=https://soundcloud.com/you/likes &
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
  brainLab)
	exec google-chrome-stable --profile-directory="Profile 3" --app=file:////home/mr124/Documents/Projects/BrainLab/old/BrainLab/templates/mainPage.html &
    ;;
  spotify)
	exec google-chrome-stable --profile-directory="Profile 3" --app=https://open.spotify.com/ &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

