#Taking teh CV technical test and extracting the data

import os
import json
import shutil
import webbrowser
import requests
path = os.getcwd() # get current directory
data_dict ={}
term = 'michaeljackson'
#term = 'thebeatles'
#url = 'https://itunes.apple.com/search?term=michaeljackson&entity=musicVideo'
url = 'https://itunes.apple.com/search?term={0}&entity=musicVideo'.format(term)
#webbrowser.open_new(url)


r = requests.get(url,allow_redirects=True)
open('itunes_data.json','wb').write(r.content)
#get_json = json.load('itunes_data.json')


with open('itunes_data.txt','r') as f:
    loaded_json = json.load(f)
    #print(loaded_json)
    print(json.dumps(loaded_json))
    print(loaded_json['results'])
    print(loaded_json['resultCount'])
    print(loaded_json[['results'],["kind"]])
''''
need to find the following
    artistName =
    collectionName=
    collectionPrice = 
    trackName =
    artworkUrl100 = 
'''
#insert.data_dict(key)

