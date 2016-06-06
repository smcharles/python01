import urllib
from BeautifulSoup import *


url = "http://python-data.dr-chuck.net/known_by_Ross.html"

count = 7

while count > 0:
	html = urllib.urlopen(url).read()
	parsed_html = BeautifulSoup(html)

	tags = parsed_html('a')

	links = []

	for tag in tags:
		link = tag.get('href', None)
		links.append(link)

	url = links[17]


	count -= 1

print url