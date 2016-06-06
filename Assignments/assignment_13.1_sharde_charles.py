import urllib
from BeatifulSoup import *

tags = BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read())("span")

lst = []

for tag in tags:
	lst.append(int(tag.contents[0]))

print sum(lst)