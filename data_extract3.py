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
term = 'thebeatles'
#url = 'https://itunes.apple.com/search?term=michaeljackson&entity=musicVideo'
url = urlopen('https://itunes.apple.com/search?term={0}&entity=musicVideo'.format(term))

resp = json.loads(url.read().decode('utf-8'))
pprint(resp)


class JSONObject:
    def __init__(selfself,d):
        self.__dict__ = d

data = json.loads(resp,object_hook=JSONObject)
print(data.trackName)

#pprint(resp('collectionName'))