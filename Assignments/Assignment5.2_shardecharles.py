num_list = list()
while True:
	numbers = raw_input("Enter a number: ")
	if numbers == "done": break

	try:
		num_list.append(int(numbers))
	except:
		print "Please enter a number and not a word, Try again"

print "the largest number is ", max(num_list), "& the smallest number is ", min(num_list)