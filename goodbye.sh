#!/usr/bin/env bash


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


choice=$(echo -e "Shutdown\nLock\nHibernate\nSleep\nReboot\nQuit" | dmenu -i -p "Chosse")

case $choice in
  Shutdown)
		sayit.py 'system is going to shutdown' || espeak 'system is going to shutdown' && shutdown now
    	;;
  Lock)
		sayit.py 'screen locked' || espeak 'screen locked' && i3lock -c "#000033"
		;;
  Hibernate)
  		sayit.py 'system is going to hibernate' || espeak 'system is going to hibernate' && systemctl hibernate
                ;;
  Sleep)
		i3lock -c "#000033" && systemctl suspend
   		;;
  Reboot)
		reboot
  		;;
  Quit)
		i3-msg exit
		;;
  *)
		sayit.py 'error' || espeak 'error'
    	;;
esac
