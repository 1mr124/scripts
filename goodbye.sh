#!/usr/bin/env zsh

# all the  pachages needed in the script
packgeNeeded=("dmenu" "i3" "i3lock" "espeak")


# check if all used packages are installed
# dpkg -s $1 &> /dev/null [ $? -eq 0 ]  0 > installed , 1 > not installed

function installAllPackages(){
    read -p "Do you want to install missing Packages [y]: " answer
    if [[ $answer =~ [yY] ]];then sudo apt-get install -y ${packgeNeeded[@]}  ;else echo You must install all packges && exit ;fi
    
}


# Check for all needed packges first  - if one is missing > install all
#dpkg -s ${packgeNeeded[@]} > /dev/null 2>&1 || installAllPackages 


choice=$(echo -e "Hibernate\nSleep\nLock\nShutdown\nReboot\nQuit" | dmenu -i -p "Chosse")

case $choice in
	Shutdown)
			/home/mr124/scripts/sayit.py 'system is going to shutdown' || espeak 'system is going to shutdown' && shutdown now
			;;
	Hibernate)
			/home/mr124/scripts/sayit.py 'system is going to hibernate' || espeak 'system is going to hibernate' && systemctl hibernate
			;;
	Sleep)
			i3lock -c "#000033" && systemctl suspend
			;;
	Lock)
			/home/mr124/scripts/sayit.py 'screen locked' || espeak 'screen locked' && i3lock -c "#000033"
			;;
	
	Reboot)
			reboot
			;;
	Quit)
			i3-msg exit
			;;
	*)
			/home/mr124/scripts/sayit.py 'error' || espeak 'error'
			;;
esac
