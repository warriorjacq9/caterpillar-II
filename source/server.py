#!/usr/bin/env python3
"""A program to start a network server."""

import socket
import _thread
import pack
import unpack
from player import Player
from leaf import Leaf

server = "192.168.0.21"

port = 65000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Waiting for connection")

objs = [Player(200, 200, 60, 20, (255, 0, 0)),
        Player(200, 100, 60, 20, (255, 0, 0)),
        Leaf()]


def threaded_client(conn, obj):
    """Connect to client."""
    conn.send(pack.pack(objs[obj]))
    reply = ""
    while True:
        try:
            data = unpack.unpack(conn)
            objs[obj] = data

            if not data:
                print('Disconnected.')
                break
            else:
                reply=objs[obj]
                print('Recieved: ', data)
                print('Sending: ', reply)

            conn.send(pack.pack(reply))
        except Exception as e:
            print(e)
            break

    print("Lost connection.")
    conn.close()


currentObj = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    _thread.start_new_thread(threaded_client, (conn, currentObj))
    if type(objs[currentObj])==type(Player):
        objs[currentObj] = Player(200, 200, 60, 20, (255, 0, 0))
    currentObj += 1
    if currentObj == len(objs):
        currentObj = 0
