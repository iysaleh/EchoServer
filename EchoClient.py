import socket

'''
EchoClient.py
    Provides a simple client for communicating with an EchoServer.
    Provides send() and recv() methods for sending and receiving messages.
    Author: Ibraheem Saleh'''

class EchoClient:
    """
    EchoClient Class
        Provides a simple client for communicating with an EchoServer.
        Provides send() and recv() methods for sending and receiving messages.
    """
    host = None
    port = None
    sock = None
    
    def __init__(self, host="localhost", port=7777):
        """EchoClient Constructor - Creates a new EchoClient object.
        :param host: (str) The host to connect to.
        :param port: (int) The port to connect to.
        :return: (EchoClient) The new EchoClient object."""
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, msg):
        """EchoClient send() Method - Sends a message to the server.
        :param msg: (str) The message to send.
        :return: (None)"""
        self.sock.send(msg.encode())

    def recv(self):
        """EchoClient recv() Method - Receives a message from the server.
        :return: (str) The message received from the server."""

        return self.sock.recv(1024).decode()

    def close(self):
        """EchoClient close() Method - Closes the connection to the server.
        :return: (None)"""

        self.sock.close()

#EchoClient CLI Args (OptionsParser)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-s",'--host', help='Host', type=str, default='localhost')
    parser.add_argument("-p",'--port', help='Port', type=int, default=7777)
    args = parser.parse_args()
    client = EchoClient(args.host, args.port)
    try:
        while True:
            print("Input: ", end="")
            client.send(input())
            print("Echo: ", client.recv())
    except KeyboardInterrupt:
        print("\nClosing Client - EchoServer Connection.")
        client.close()
    except ConnectionAbortedError:
        print("\nClosing Client - Connection Aborted (EchoServer Unavailable).")
        client.close()
    except EOFError:
        print("\nClosing Client - EOF (EchoServer Unavailable).")
        client.close()
    