# import socket library
from socket import *

# import shared constants
from constants import *

# create a server socket using TCP/IP protocol
s = socket(AF_INET, SOCK_STREAM)

# bind the socketwith host and port number
s.bind((host, port))

# allow maximum 1 connection to the socket
s.listen(1)

# endless loop to receive messages from client
while True:
    # wait till a client accepts the connection
    c, addr = s.accept()

    # display client address
    print("Connection from: ", str(addr))

    # read message from client, decode it
    message = c.recv(bufsize).decode()

    # display message from client
    print("Message from client: ", message)

    # send modified message to client, encode it with UTF-8
    c.send(bytes('Your message was: ' + message, 'utf-8'))

    # close client socket
    c.close()
