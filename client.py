from socket import *
from bots import *
import sys
import random


def main():
    try:
        # create a client socket using TCP/IP protocol
        client = socket(AF_INET, SOCK_STREAM)

        # get ip and port number from cli args
        ip = sys.argv[1]
        port = int(sys.argv[2])

        # connect to server with host and port number
        client.connect((ip, port))
        print("\nwelcome to the chat room!")

        # get user name
        name = input("\nwhat's your name? ")

        # display the bots the user can chat with
        botsNames = ', '.join(list(bots.keys()))
        print('\nbots in the chatroom: ' + botsNames)

        while True:
            # read message from user
            message = input("\n" + name + ": ")

            # send message to server with UTF-8 encoding
            client.send(bytes(message, 'utf-8'))

            # receive response from server with UTF-8 encoding
            response = client.recv(2048).decode('utf-8')

            # display response from server
            print(response)

            # check if the response is a farewell, if so, exit the script
            if(response.split(" ", 1)[1] in farewells):
                client.close()
                sys.exit()

    except BrokenPipeError:
        print("\nserver is down!")
    except ConnectionResetError:
        print("\nyou have been kicked out due to inactivity\n")
        print(random.choice(farewells))
    except ConnectionRefusedError:
        print("connection refused: is the server running on " +
              ip + ":" + str(port) + "?")
    except KeyboardInterrupt:
        print("\n" + random.choice(farewells))
    except IndexError:
        print("usage: python3 client.py <ip> <port>")
        print('example: python3 client.py localhost 9999')


if __name__ == "__main__":
    main()
