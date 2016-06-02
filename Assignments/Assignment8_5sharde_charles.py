fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh:
	if line.startswith("From: "):
		count += 1 
		linelst = line.split()
		print linelst[1]

print "There were", count, "lines starting with From!"