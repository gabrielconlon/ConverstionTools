#!/usr/bin/env python3

def convertIP_toBinary(user_binary):
    return '.'.join(bin(int(octet) + 256)[3:] for octet in user_binary.split('.'))
