nuid="02c86146"

def reverse_bytes(uid):
	#index = 0
	#new_uid=[]
	#while index < len(uid):
	#	new_uid.append(uid[index+2:index])
	#	index = index + 2
	return ''.join(reversed([uid[i:i+2] for i in range(0, len(uid), 2)]))
print nuid
string = reverse_bytes(nuid)
print string
print "Your mifair code: {0}".format(int(string,16))
