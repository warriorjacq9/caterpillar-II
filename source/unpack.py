#!/usr/bin/env python3
"""A file containing the unpack function."""
import pickle
import struct

def unpack(socket):
    """Unpack a package recieved from socket, and packed with pack.pack()."""
    buf = b''
    while len(buf) < 4:
        buf += socket.recv(4 - len(buf))

    length = struct.unpack('!I', buf)[0]
    return pickle.loads(socket.recv(length))
