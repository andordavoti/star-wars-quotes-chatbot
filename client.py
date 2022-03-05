# import socket library
from socket import *

# import shared constants
from constants import *


# create a client socket using TCP/IP protocol
c = socket(AF_INET, SOCK_STREAM)

# connect to server with host and port number
c.connect((host, port))

# read message from user
message = input("Enter your message: ")

# send message to server with UTF-8 encoding
c.send(bytes(message, 'utf-8'))

# receive message from server with UTF-8 encoding
msg = c.recv(bufsize).decode()

# display message from server
print(msg)

# close client socket
c.close()
