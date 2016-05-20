import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('span')
count = 0
sum = 0
for tag in tags:
    sum =  sum + int(tag.contents[0])
    count = count + 1

print 'Count', count
print 'Sum', sum 
