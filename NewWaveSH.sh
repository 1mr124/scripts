#!/usr/bin/env bash

# all the  pachages needed in the script
packgeNeeded=("dmenu" "graphicsmagick-imagemagick-compat" "imagemagick" "xclip" "espeak")


# check if all used packages are installed
# dpkg -s $1 &> /dev/null [ $? -eq 0 ]  0 > installed , 1 > not installed

function installAllPackages(){
    read -p "Do you want to install missing Packages [y]: " answer
    if [[ $answer =~ [yY] ]];then sudo apt-get install -y ${packgeNeeded[@]}  ;else echo You must install all packges && exit ;fi
    
}


# Check for all needed packges first  - if one is missing > install all
#dpkg -s ${packgeNeeded[@]} > /dev/null 2>&1 || installAllPackages 


choice=$(echo -e "Focused\nCopy\nFull" | dmenu -i -p "Chosse")

case $choice in
  Focused)
    scrot -u -q 100 - | tee '/home/mr124/Pictures/SS/SS-'$(date +"%Y-%m-%d_%H-%M-%S").png | xclip -selection clipboard -t image/png
    ;;
  Copy)
    scrot -s -q 100 - | tee '/home/mr124/Pictures/SS/SS-'$(date +"%Y-%m-%d_%H-%M-%S").png | xclip -selection clipboard -t image/png
    ;;
  Full)
    scrot -q 100 - | tee '/home/mr124/Pictures/SS/SS-'$(date +"%Y-%m-%d_%H-%M-%S").png | xclip -selection clipboard -t image/png
    ;;
  *)
	/home/mr124/scripts/sayit.py 'error' || espeak "Error"
    ;;
esac
