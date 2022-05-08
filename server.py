from socket import *
from bots import *
import threading
import random
import sys

try:
    # handle message response
    def get_response(good_word_found: bool, bad_word_found: bool, bot_name: str):
        if(bad_word_found):
            return bot_name + ': ' + random.choice(bots[bot_name]['bad_quotes'])
        elif(good_word_found):
            return bot_name + ': ' + random.choice(bots[bot_name]['good_quotes'])
        else:
            return bot_name + ': ' + random.choice(bots[bot_name][random.choice(quote_types)])

    # handle greetings and farewells
    def get_salut(words: list[str], salut_words: list[str]):
        for word in words:
            if(word in salut_words):
                for botName in words:
                    if(botName in bots.keys()):
                        return botName + ': ' + \
                            random.choice(salut_words)

                return random.choice(list(bots.keys())) + ': ' + \
                    random.choice(salut_words)
        return None

    # handle messages from client
    def handle_message(message: str, client: socket):
        words = message.lower().translate(
            {ord(i): None for i in '!?.,:;-_*"&()/=+'}).split()

        greeting = get_salut(words, greetings)

        if greeting is not None:
            client.send(bytes(greeting, 'utf-8'))
            return

        farewell = get_salut(words, farewells)

        if farewell is not None:
            client.send(bytes(farewell, 'utf-8'))
            client.close()
            return

        # Check for messages to bots
        good_word_found = False
        bad_word_found = False

        for word in words:
            if(word in good_words):
                good_word_found = True
            elif(word in bad_words):
                bad_word_found = True

        responseBot = None

        for word in words:
            if(word in bots.keys()):
                responseBot = word

        # if the client message does not mention a bot, use a random bot
        if(responseBot is None):
            responseBot = random.choice(list(bots.keys()))

        # send response to client, encode it with UTF-8
        client.send(
            bytes(get_response(good_word_found, bad_word_found, responseBot), 'utf-8'))

    # handle client connection
    def handle_client(client: socket):
        while True:
            try:
                # receive message from client with UTF-8 encoding
                message = client.recv(2048).decode('utf-8')
                handle_message(message, client)

                # auto kick out clients that don't send a message in 30 seconds
                client.settimeout(30)
            except:
                client.close()
                break

    # main function to start the server and receive clients
    def main():
        try:
            # create a server socket using TCP/IP protocol
            server = socket(AF_INET, SOCK_STREAM)

            # get ip and port number from cli args
            ip = sys.argv[1]
            port = int(sys.argv[2])

            # bind the socket with host and port number
            server.bind((ip, port))

            server.listen()
            print('server is running!')
            print('waiting for a client to connect...')

            # accept client connections and spin up a thread handling that client
            while True:
                client, address = server.accept()
                print("client connected: ", str(address))
                threading.Thread(target=handle_client, args=(client,)).start()

        except IndexError:
            print("usage: python3 server.py <ip> <port>")
            print('example: python3 server.py localhost 9999')

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\n" + random.choice(farewells))
