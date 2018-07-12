#Taking teh CV technical test and extracting the data
from urllib.request import urlopen
from pprint import pprint
import os
import json
import shutil
import webbrowser
import requests
path = os.getcwd() # get current directory
data_dict ={}
term = 'michaeljackson'
country = 'GB'
#url = 'https://itunes.apple.com/search?term=michaeljackson&entity=musicVideo'
url = urlopen('https://itunes.apple.com/search?term={0}&country={1}&entity=musicVideo'.format(term,country))



resp = json.loads(url.read().decode('utf-8'))
pprint(resp)

#Track list returned
json_result_count = resp['resultCount']
i = 0
for i in range(1,json_result_count,1):
    json_trackCensorName = resp['results'][i]['trackCensoredName']
    json_artistName = resp['results'][i]['artistName']
    json_collectionName = resp['results'][i]['collectionCensoredName']
    json_collectionPrice =  resp['results'][i]['collectionPrice']
    json_trackName = resp['results'][i]['trackName']
    json_artworkUrl100 = resp['results'][i]['artworkUrl100']
    json_currency = resp['results'][i]['currency']
    json_trackViewUrl=resp['results'][i]['trackViewUrl']
    print(json_artistName,json_collectionName,json_collectionPrice,json_currency,'\n',json_trackName,json_artworkUrl100,json_trackViewUrl)


