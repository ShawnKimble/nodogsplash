
#!/usr/bin/python

import sys
from bitcoinrpc.authproxy import AuthServiceProxy
h = AuthServiceProxy("http://user:password@localhost:8332")
rate = 0.0001 # / 6 blocks ~ per hr

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

Current_Block =  h.getinfo()['blocks']
for entry in h.listunspent():
	print int(entry['confirmations'])
	print int(float(entry['amount'])/rate)
	if int(entry['confirmations']) < int(float(entry['amount'])/rate):
		print entry['address'], " is valid for another ", int(float(entry['amount'])/rate)-entry['confirmations'], " blocks"
		print "Or about ", (int(float(entry['amount'])/rate)-entry['confirmations'])/6*10, " minutes"		
		print "Or about ", (int(float(entry['amount'])/rate)-entry['confirmations'])/6*10*60, " seconds"		
	else:
		print entry['address'], " credits have expired"
