cd /home/mr124/void-packages
git pull
./xbps-src clean google-chrome
../xbps-src pkg google-chrome
sudo xbps-install --repository=/home/mr124/void-packages/hostdir/binpkgs/nonfree google-chrome


