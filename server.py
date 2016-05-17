import socket
import sys
from thread import *

conn=[]
HOST=''
PORT = 5190
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'socket created'

try:
	s.bind((HOST,PORT))
except socket.error as msg:
	print 'bind failed.Error code: ' + str(msg[0]) + 'message ' + msg[1]
	sys.exit()

print 'socket bind complete'

s.listen(2)
print 'socket now listening'


def clientthread(conn):
	if conn[0]:
	
		conn[0].send('welcome to the server\n')
		while True:
			data=conn[0].recv(1024)
			reply = data
			if not data:
				break
			conn[1].sendall(reply)
		conn.close()
	 
	if conn[1]:
		conn[1].send('welcome to the server\n')
		while true:
			data= conn[1].recv(1024)
			reply=data
			if not data:
				break
			conn[0].sendall(reply)
		conn.close()

for x in xrange(2):
	conn[x],addr=s.accept()
	if conn[0]!=NULL:
		start_new_thread(clientthread,(Conn))
	 
		print 'connected with ' + addr[0] +':' + str(addr[1])
	 if conn[1]!=NULL:
		start_new_thread(clientthread,(conn))
s.close()
