nums = []
count = 0
total = 0

fname = raw_input('Enter File Name:')
fh = open(fname)
for line in fh:
	if line.startswith('X-DSPAM-Confidence'):
		pos = line.find('0')
		end_pos = line.find(' ', pos)
		num = float(line[pos : end_pos])
		nums.append(num)
		count = count + 1

for value in num_list:
	total = total + value

avg = total / count
print 'Number of lines:', count, 'Avg:', avg
