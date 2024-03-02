#!/usr/bin/env python3

import requests
from lxml import html
from sys import argv

shareXpath = '//*[@id="wrapper"]/div/div[3]/div/main/div[1]/div[1]/div[2]'


def findShareDivElement(responseContent):
    try:
        tree = html.fromstring(responseContent.content)
        result = tree.xpath(shareXpath)
        return result[0]
    except:
        print("can't find share div")


def findSharePrice(ShareName):
    try:
        url = f'https://www.mubasher.info/markets/EGX/stocks/{ShareName}'
        response = requests.get(url)
        SharePrice = findShareDivElement(response)
        return SharePrice.text
    except:
        print('Error Getting the request')


def storePricToFile(sharePrice, FilePath):
    try:
        with open(FilePath, 'a') as file:
            file.write(sharePrice+'\n')
    except:
        print(f'error in opening the file {FilePath}')


x = findSharePrice(argv[1])
print(x)
storePricToFile(x,'/home/mr124/SharePric.log')