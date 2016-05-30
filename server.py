

'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5133 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(5)
print 'Socket now listening'
conn = [0,0,0,0,0]
k=0
j=0
#addr = []
#Function for handling connections. This will be used to create threads
def clientthread(conn,i,att):
    #Sending message to connected client
    conn[i].send('welcome to the server')
    for k in range(i-1):
        conn[i].sendall("connections availble ar:" + (arrmsg[k]) +"\n")
    #for j in range(i-1):
    #    conn[j].sendall('new updated connection :')
     #   conn[j].sendall(str(new))
    conn[i].send('Enter Id of User You want to chat with\n')
    sel = conn[i].recv(1024)
    while int(sel) < 1 and int (sel) > len(conn) or int(sel)==i+1 or conn[int(sel)-1]==0:
        sel = conn[i].recv(1024)
    att[i] = int(sel)-1
        
    conn[i].send('Welcome to the server. Type something and hit enter\n') #send only takes string
    #infinite loop so that function do not terminate and thread do not end.
    while True:         
        #Receiving from client
	data = conn[i].recv(1024)
	
	data='client'+str(i+1)+':' +data

	conn[int(att[i])].sendall(data)

    conn[i].close()

#now keep talking with the client
x=0
i=0
arrmsg=[]
new=0
arr=[]
att=[0,0,0,0,0]
while 1:
    #wait to accept a connection - blocking call
    conn[i], addr = s.accept()
    msg = 'Connected Client ' + addr[0] + ':' + str(addr[1])
    print msg 
    arrmsg.append(str(msg))
    new=str(msg)
    for x in range(i):
            if x != i and att[x] == 0:
                conn[x].sendall(str(i)+'\t'+ msg) 
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,i,att))
    i=i+1


#conn[1].sendall(msg)
s.close()
