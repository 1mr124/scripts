#!/usr/bin/env bash

selectedAi=$(echo -e "ChatGpt\nBard" | dmenu -p "Select an Ai:")


case $selectedAi in
  ChatGpt)
	exec google-chrome-stable --app=https://chat.openai.com/ &
    ;;
  Bard)
	exec google-chrome-stable --app=https://bard.google.com/chat &
    ;;
  *)
        espeak "Error"
    ;;
esac

