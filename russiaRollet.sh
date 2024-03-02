#!/bin/bash


while [ True ]; do

randomNumber=$(ps aux | grep -v -i -E 'scripts/russiaRollet.sh|xorg' | awk '{print $2}' | grep -v -E 'PID|69974|69995|70067|70095|70289' | shuf -n 1)
echo 'killing this process ' $(ps -p $randomNumber -o comm=)
sudo kill -9 $randomNumber 
sleep .5

done

