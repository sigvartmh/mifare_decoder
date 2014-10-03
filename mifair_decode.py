nuid="02c86146"

import argparse

parser = argparse.ArgumentParser(description='Process NUID[4] read from miFare card.')
parser.add_argument('-m', dest='mifare', metavar='M', type=str ,help='Selector for nuid string')

args = parser.parse_args()


if not  args:
	print "Provide an valid argument"

nuid = args.mifare

def reverse_bytes(uid):
	return ''.join(reversed([uid[i:i+2] for i in range(0, len(uid), 2)]))

string = reverse_bytes(nuid)

print string

try:
	print "Your mifair code: {0}".format(int(string,16))
except ValueError:
	print "What you entered is not a valid miFare NUID"


