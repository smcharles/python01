fname = raw_input('Enter file name: ')

try:
	open(fname)
except:
	print 'File does not exist'

fh = open(fname)
lst_hours = []

for line in fh:
	if line.startswith('From '):
		line = line.split()
		print line
		for word in line:
			if ':' in word:
				time = word.split(':')
				lst_hours.append(time[0])

hours = dict()

for hour in lst_hours:
	hours[hour] = hours.get(hour, 0) + 1

hours_tup = hours.items()
lst_sorted_hours = list()

for hour, count in hours_tup:
	lst_sorted_hours.append((count, hour))

lst_sorted_hours.sort(reverse=True)

print lst_sorted_hours