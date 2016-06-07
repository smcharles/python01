import re

fh = open('regex_sum_242232.txt')
nums = list()

for line in fh:
	num = re.findall('[0-9]+', line)
	if len(num) >= 1:
		for _int in num:
			nums.append(_int)

_sum = None

for num in nums:
	num = int(num)
	if _sum == None:
		_sum = num
	else:
		_sum = _sum + num

print 'Sum is:' , _sum