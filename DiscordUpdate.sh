cd /home/mr124/void-packages
git pull
./xbps-src clean discord
cd srcpkgs/discord
../../xbps-src pkg discord
sudo xbps-install --repository=/home/mr124/void-packages/hostdir/binpkgs/nonfree discord
