import urllib
import xml.etree.ElementTree as ET

while True:
	url = raw_input('Enter Url: ')
	if len(url) < 1: break

	html = urllib.urlopen(url).read()

	xml = ET.fromstring(html)

	comments = xml.findall('comments/comment')

	total = 0

	for comment in comments:
		number = int(comment.find('count').text)

		total += number

	print total