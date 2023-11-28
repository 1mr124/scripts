#!/bin/zsh

setxkbmap -option ctrl:nocaps
xmodmap -e "keycode  66 = Tab ISO_Left_Tab Tab ISO_Left_Tab"
xmodmap -e "keycode 67  = Escape "
