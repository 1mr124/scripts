#!/usr/bin/python3
import argparse
import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/domain/report'


def getSubDomains(params):
	response = requests.get(url, params=params)
	try:
		data = response.json()
		return data["subdomains"]
	except:
		return False

def writeSubdomains(subdomains, fileName):
	if subdomains:
		with open("{}.OldVT".format(fileName),"w") as file:
			for i in subdomains:
				file.write(i+'\n')
			file.close()




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a Test',add_help=False)
	parser.add_argument('-d', '--domain', help='this will get domain')
	parser.add_argument('--help', '-h', action='help', help='-d domain')

	args = parser.parse_args()

	domain = args.domain
	
	API_KEY = open("/home/mr124/Documents/.virustotalApi","r").readline().strip()


	if domain:
		params = {'apikey':API_KEY,'domain':domain}
		print("Geting ",domain)
		domains = getSubDomains(params)
		writeSubdomains(domains,domain)
	