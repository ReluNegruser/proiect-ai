import urllib.request
from urllib.parse import urlparse
from nltk.corpus import wordnet as wn

print(wn.all_lemma_names(lang="ro"))
'''file = open('urlData.txt', 'wb')
with urllib.request.urlopen('http://nlptools.info.uaic.ro/WebNpChunkerRo/') as response:
    html = response.read()
    file.write(html)

url = 'http://nlptools.info.uaic.ro/WebNpChunkerRo/'

o = urlparse(url)
print(o)
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   file.write(the_page)'''