#!/usr/bin/env python3
"""A file with the Network class."""

import socket
import pack
import unpack


class Network:
    """A network class."""

    def __init__(self):
        """Init self."""
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.21"

        self.port = 65000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        """Get self's p."""
        return self.p

    def connect(self):
        """Connect to client."""
        try:
            self.client.connect(self.addr)
            print("Connected.")
            return unpack.unpack(self.client)
        except Exception as e:
            print(e)

    def send(self, data):
        """Send data to client."""
        self.client.sendall(pack.pack(data))
        return unpack.unpack(self.client)


if __name__ == '__main__':
    n = Network()
    print(n.send("hello"))
    print(n.send("working"))
