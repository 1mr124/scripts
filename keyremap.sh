#!/usr/bin/bash

setxkbmap -option caps:escape
xmodmap -e "keycode 66  = Tab " && xmodmap -e "keycode 67  = Escape "
