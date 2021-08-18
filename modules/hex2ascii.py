#!/usr/bin/env python3

def convert():
    userinput = input('Enter your Hexidecimal string: ')
    #BUG: chopping first letter of entered string
    # hex_string = userinput[2:]
    bytes_object = bytes.fromhex(userinput)
    #TODO: clean up to allow spaces, :, and all together
    ascii_string = bytes_object.decode('ASCII')
    print(ascii_string)
