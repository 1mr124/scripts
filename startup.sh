#!/bin/bash

#exec > /tmp/startup.log 2>&1

# Your script commands follow below
echo 'hello Mr12' >> /home/mr124/startup.txt

setxkbmap -option ctrl:nocaps
echo 'hello Mr12' >> /home/mr124/startup.txt

xmodmap -e "keycode  66 = Tab ISO_Left_Tab Tab ISO_Left_Tab"
echo 'hello Mr12' >> /home/mr124/startup.txt

xmodmap -e "keycode 67  = Escape "
echo 'hello Mr12' >> /home/mr124/startup.txt

xset +dpms dpms 600 600 600 && echo 'Done Mr12' >> ~/startup.txt
