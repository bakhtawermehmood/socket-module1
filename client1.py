import socket

s= socket.socket()
host = socket.gethostname()
port =5190
s.connect((host,port))
while true:
	data=raw_input("enter...")
	try: 
		s.sendall(data)
	except socket.error:
		print 'send failed'
		sys.exit()
	print 'message send successfully'
	print s.recv(1024)
	if data=='bye' or s.recv(1024)=='bye':
		print 'exiting'
		break
s.close()

