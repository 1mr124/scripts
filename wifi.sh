#!/usr/bin/bash


choice=$(echo -e "None\nEtisalt\nAi312\nQuit" | dmenu -i -p "Chosse")

case $choice in
        None)
		doas rm /run/wpa_supplicant/wlp3s0
		doas wpa_supplicant -B -i wlp3s0 -c /etc/wifi/None.conf && doas dhcpcd wlp3s0
		;;
	Etisalt)
		doas rm /run/wpa_supplicant/wlp3s0
		doas wpa_supplicant -B -i wlp3s0 -c /etc/wifi/Etisalt.conf && doas dhcpcd wlp3s0
		;;
	 Ai312)
                doas rm /run/wpa_supplicant/wlp3s0
                doas wpa_supplicant -B -i wlp3s0 -c /etc/wifi/Ai312 && doas dhcpcd wlp3s0
                ;;
	*)
		echo "Hope"
		;;
esac
