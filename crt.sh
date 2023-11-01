#!/bin/bash

# Check if the domains file exists

if [ ! -f $1 ]; then
  echo "File $1 not found. Please create the file and add domain names to it."
  exit 1
fi

# Loop through each line in the domains file
while IFS= read -r domain; do
  if [ -n "$domain" ]; then
	echo Downloading $domain
	wget -q https://crt.sh/?q=$domain -O $domain.html
	grep -Eo '\b[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' $domain.html > $domain.txt
	sort $domain.txt | uniq > $domain.crt
  fi
done < $1
echo "cleaning up" && rm *.html *.txt
