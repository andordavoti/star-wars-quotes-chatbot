# star-wars-chatbot

## Usage

Start first the server with localhost as the IP and a port that's not in use on your system. Then start the client with the same CLI args as the server.

Enter your username.

Mention any of the names of the following characters to get a response from them.

If no name is mentioned, a random quote from a random character will be returned.

**Bots:**

- anakin
- padme
- leia
- luke
- rey

**Implemented features:**

- Greetings:
  - If you send a greeting, you will get one back
  - If a bots name is mentioned it will be from them, otherwise from a random bot
- Farewells:
  - If you send a farewell, you will get one back
  - If a bots name is mentioned it will be from them, otherwise from a random bot
- Other messages:
  - There is a list of "good" and "bad" words. If the message contains a bad word, a "bad" quote will be returned, if a "good" word is mentioned, a "good" quote will be returned. Otherwise, a random quote will be returned.
  - If a bots name is mentioned it will be from them, otherwise from a random bot
- Inactivity timeout:
  - If you don't send any messages for 30 seconds, you will be kicked from the server

## Client

**Run client:**

```sh
python3 client.py <ip> <port>
```

**Exit client:**

To exit the client, the message needs to contain `bye` or `goodbye` (or you can use `ctrl+c`)

## Server

**Run server:**

```sh
python3 server.py <ip> <port>
```

**Exit server:**

To exit the server, use `ctrl+c`
