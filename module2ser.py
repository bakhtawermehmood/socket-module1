'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port

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
s.listen(10)
print 'Socket now listening'
k=0
t=[]
p=0
j=0
n=0
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server.') #send only takes string
    conn.send('enter user name')
    n1=conn.recv(1024)
    arr3.append(str(n1))
    for k in range(i-1):
        conn.sendall("connections connected to network are : " + (arr3[k]) + " \n")
    for j in range(i-1):
        arr[j].sendall('new connections  connected to network are: ')
        arr[j].sendall(str(n1))
    conn.sendall("Which client do you want to connect to? enter his address\n")
    address = conn.recv(1024)
    t.append(conn)
    n=0
    for n in range(i):
         if (address == arr3[n]):
            arr3[n]=arr[n]
            t.append(arr3[n])
            #infinite loop so that function do not terminate and thread do not end.
    while True:

            data=conn.recv(1024)


            if conn == t[0]:
                conn = t[1]
                conn.sendall(data)
                conn = t[0]
            elif conn == t[1]:
                conn = t[0]
                conn.sendall(data)
                conn = t[1]
            if not data:
                break




    #came out of loop
    conn.close()
arr =[] # this is to keep track of users
newv=0
arr2=[]
arr3=[]
i=0
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    arr.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    arr2.append(str(addr[1]))
    newv=addr[1]

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

    i += 1

s.close()

