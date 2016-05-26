import socket
from thread import *

s=socket.socket()
host =socket.gethostname()
port=5133

s.connect((host,port))
def clientthread(s):
	while 1:
	print s.recv(1024)

start_new_thread(clientthread, (s,))
while(1):
	data=raw_input('')
	s.sendall(dta)
	if str(data) =='exit':
		s.close

