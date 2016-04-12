hours = raw_input('Enter hours:')
pay = raw_input('Enter pay rate:')
hours = float(hours)
pay = float(pay)

if hours <= 40:
	total = hours * pay 
elif hours > 40:
# for the hours over 40 - 1.5 x pay 
# hours = 41 , 41 - 40 
	total = (40 * pay) +  (hours - 40) * (1.5 * pay)

print 'Hey I owe you', total