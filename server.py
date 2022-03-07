# import socket library
from socket import *

# import sys library
import sys

try:
    # create a server socket using TCP/IP protocol
    s = socket(AF_INET, SOCK_STREAM)

    # get ip and port number from cli args
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # cli help option
    if(ip == '--help' or ip == '- h'):
        print('usage: python3 server.py <ip> <port>')
        sys.exit()

    # bind the socketwith host and port number
    s.bind((ip, port))

    # allow maximum 1 connection to the socket
    s.listen(1)

    print('server is running...')

    # wait till a client accepts the connection
    c, addr = s.accept()

    # display client address
    print("connection from: ", str(addr))

    try:
        # loop to receive messages from client
        while True:
            # read message from client, decode it in UTF-8
            message = c.recv(2048).decode('utf-8')

            if(message == 'exit'):
                print('\nclient has left the chat room')

                # send goodbye message to client, encode it with UTF-8
                c.send(bytes('\ngoodbye!', 'utf-8'))

                # close client socket
                c.close()
                break

            # display message from client
            print("Message from client: ", message)

            # send modified message to client, encode it with UTF-8
            c.send(bytes('Your message was: ' + message, 'utf-8'))

    except BrokenPipeError:
        print("\nclient has left the chat room!")
    except ConnectionResetError:
        print("\nclient has left the chat room!")

except (IndexError, ValueError):
    print("usage: python3 client.py <ip> <port>")
except KeyboardInterrupt:
    print("\ngoodbye!")
