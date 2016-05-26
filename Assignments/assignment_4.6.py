def computepay(h,r):
	if h > 40:
		regPay = 40 * r
		overtime = (h - 40) * (r * 1.5)
		total = regPay + overtime
		return total 
	else:
		total = h * r
		return total

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate")
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs,rate)
print "Pay",p

