from socket import *
from bots import *
import random
import sys


def analyzeMessage(message: str, c: socket):
    words = message.lower().replace('?', '').replace('.', '').split()

    responded = False

    for word in words:
        if(word in bots.keys()):
            messageToClient = word + ': ' + random.choice(bots[word])

            # send message to client, encode it with UTF-8
            c.send(bytes(messageToClient, 'utf-8'))

            print(messageToClient)
            responded = True
            break

    # if the client didn't include a bot name in the message, send a quote from a random bot
    if not responded:
        randomBot = random.choice(list(bots.keys()))

        messageToClient = randomBot + ': ' + random.choice(bots[randomBot])

        c.send(bytes(messageToClient, 'utf-8'))


def handleMessage(message: str, c: socket):
    if(message == 'exit'):
        print('\nclient has left the chat room')

        # send goodbye message to client, encode it with UTF-8
        c.send(bytes('\ngoodbye!', 'utf-8'))

        # close client socket
        c.close()
        sys.exit()

    analyzeMessage(message, c)


try:
    # create a server socket using TCP/IP protocol
    s = socket(AF_INET, SOCK_STREAM)

    # get ip and port number from cli args
    ip = sys.argv[1]
    port = int(sys.argv[2])

    # cli help option
    if(ip == '--help' or ip == '-h'):
        print('usage: python3 server.py <ip> <port>')
        print('example: python3 server.py localhost 9999')
        sys.exit()

    # bind the socket with host and port number
    s.bind((ip, port))

    # allow maximum 1 connection to the socket
    s.listen(1)
    print('server is running!')
    print('waiting for a client to connect...')

    # wait till a client accepts the connection
    c, addr = s.accept()

    # display client address
    print("connected client: ", str(addr))

    try:
        # loop to receive messages from client
        while True:
            # read message from client, decode it in UTF-8
            message = c.recv(2048).decode('utf-8')
            handleMessage(message, c)

    # handle if the client disconnects
    except BrokenPipeError:
        print("\nclient has left the chat room!")
    except ConnectionResetError:
        print("\nclient has left the chat room!")

# handle wrong cli args
except (IndexError, ValueError):
    print("usage: python3 server.py <ip> <port>")
    print('example: python3 server.py localhost 9999')

# handle if the server disconnects
except KeyboardInterrupt:
    print("\ngoodbye!")
