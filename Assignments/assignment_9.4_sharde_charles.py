fname = raw_input("File Name> ")
if fname < 1:
	fname = "mailbox-short.txt"

try:
	fhand = open(fname, "r")
except:
	"Could not find file"

emailDict = {}
emaillist = []

for line in fhand:
	if not line.startswith("From"):continue 

	words = line.split()
	email = emailList.append(words[1])

for email in emailList:
	emailDict[email] = emailDict.get(email, 0) + 1

print emailDict 

list_kv = emailDict.items()
print list_kv

swap_list = []
for k,v in list_kv:
	swap_list.append((v,k))

print swap_list