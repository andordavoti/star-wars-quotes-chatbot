# import socket library
from socket import *

# import sys library
import sys

try:
    # create a client socket using TCP/IP protocol
    c = socket(AF_INET, SOCK_STREAM)

    # get ip and port number from cli args
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # cli help option
    if(ip == '--help' or ip == '- h'):
        print('usage: python3 client.py <ip> <port>')
        sys.exit()

    # connect to server with host and port number
    c.connect((ip, port))
    print("\nwelcome to the chat room!")

    try:
        while True:
            # read message from user
            message = input("\nme: ")

            # send message to server with UTF-8 encoding
            c.send(bytes(message, 'utf-8'))

            # receive message from server with UTF-8 encoding
            msg = c.recv(2048).decode('utf-8')

            # display message from server
            print(msg)

            if(message == 'exit'):
                c.close()
                break

    except BrokenPipeError:
        print("\nserver is down!")
    except KeyboardInterrupt:
        print("\ngoodbye!")

    # close client socket
    c.close()

except (IndexError, ValueError):
    print("usage: python3 client.py <ip> <port>")
