#!/usr/bin/env bash

selectedAi=$(echo -e "ChatGpt\nBard" | dmenu -p "Select an Ai:")


case $selectedAi in
  ChatGpt)
	exec google-chrome-stable --profile-directory="Profile 11" --app=https://chat.openai.com/ &
    ;;
  Bard)
	exec google-chrome-stable --profile-directory="Default" --app=https://bard.google.com/chat &
    ;;
  *)
        sayit.py 'error' || espeak 'error'
    ;;
esac

