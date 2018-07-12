import urllib.parse
import requests

##url = 'https://itunes.apple.com/search?term=michaeljackson&entity=musicVideo'
#url = urlopen('https://itunes.apple.com/search?term={0}&entity=musicVideo'.format(term))
main_api = 'https://itunes.apple.com/search?'
artist = 'thebeatles'
url = main_api +urllib.parse.urljoin({'term':artist,'&entity=musicVideo'})
print(url)