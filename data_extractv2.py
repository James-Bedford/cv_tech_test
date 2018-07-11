#Taking teh CV technical test and extracting the data

import os
import json
import shutil
import webbrowser
import requests
path = os.getcwd() # get current directory
data_dict ={}
term = 'thebeatles'
#url = 'https://itunes.apple.com/search?term=michaeljackson&entity=musicVideo'
url = 'https://itunes.apple.com/search?term={0}&entity=musicVideo'.format(term)
#webbrowser.open_new(url)  - dont need this if used the website opens ans asks to save a file.


r = requests.get(url,allow_redirects=True)
open('requested_data.json','wb').write(r.content)  #- creates a file of the data
with open('requested_data.json','r') as f:
    search_json = json.load(f)
    print(search_json)
    dictionaryToJson = json.dumps(search_json)  #converts to json
 
