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


choice=$(echo -e "Shutdown\nReboot\nHibernate\nSleep\nLock\nQuit" | dmenu -i -p "Chosse")

case $choice in
	Shutdown)
			doas shutdown -h now
			;;
	Hibernate)
			doas zzz -Z
			;;
	Sleep)
			doas zzz -z
			;;
	Lock)
			slock
			;;
	
	Reboot)
			doas reboot
			;;
	Quit)
			i3-msg exit
			;;
	*)
			/home/mr124/scripts/sayit.py 'error' || espeak 'error'
			;;
esac
