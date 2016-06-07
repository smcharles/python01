import urllib
import json

url = raw_input('Enter URL: ')

uh = urllib.urlopen(url).read()

info = json.loads(uh)

lst = list()

for num in info['comments']:
	lst.append(int(num['count']))

total = sum(lst)

print 'Sum: ', total
