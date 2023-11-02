#!/usr/bin/python3

import requests
from sys import argv
import re  # Import the re module

domain = argv[1]

print ("Collecting ",domain)

url = f'https://crt.sh/?q=%.{domain}&output=json'

def writeToFile(subdomains):
	with open("{}.crtSh.txt".format(domain),"w") as file:
		for i in subdomains:
			file.write(i+"\n")
		file.close()

try:
	response = requests.get(url)
	if response.status_code == 200:
		data = response.text
		subdomains = set(re.findall(r'\b(?:[a-zA-Z0-9.-]+\.)*' + re.escape(domain) + r'\b', data))
		writeToFile(subdomains)
	else:
		print(f'Error: {response.status_code}')
except Exception as e:
	print(f'An error occurred: {str(e)}')
