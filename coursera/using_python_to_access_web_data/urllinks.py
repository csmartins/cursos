import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
pos = raw_input('Enter position: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
cnt = 0

print url
while cnt < count:
    tags = soup('a')
    url =  tags[int(pos) - 1].get('href', None)
    soup = BeautifulSoup(urllib.urlopen(url).read())
    print url
    cnt = cnt + 1
