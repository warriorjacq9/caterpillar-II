#!/usr/bin/env python3
"""A file containing the pack function."""
import struct
import pickle

def pack(foo):
	"""Packs an object into bytes with buffer."""
	packet = pickle.dumps(foo)
	length = struct.pack('!I', len(packet))
	packet = length + packet
	return packet
