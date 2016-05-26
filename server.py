import socket
import sys
from thread import *
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

s.listen(10)
print 'socket now listening'
conn=[0,0,0,0,0,0,0,0,0,0]

def clientthread(conn):
	conn[i].send('welcome to the server. type something and hit enter\n')
	while True:
		data=conn[i].recv(1024)
                if i==0;
			data='client:' +data
			conn[1].sendall(data)
		else:
			data='client2:' +data
			conn[0].sendall(data)
		conn[i].close()
x=0
i=0
arr1=[]
while 1:
        #wait to accept a connection- blocking call
	conn[i],addr=s.accept()
	msg='connected client is ' + addr[0] + ':' +str(addr[1])
	print msg
	for x in xrange(i):
        	if x !=i:
			conn[x].sendall(msg)
	start_new_thread(clientthread, (conn,i))
	i=i+1
