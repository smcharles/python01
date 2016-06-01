fname = raw_input("Enter file name: ")
fhand = open(fname)
words = fhand.read()

print words.upper()
