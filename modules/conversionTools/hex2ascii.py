#!/usr/bin/env python3
from resources import colors, menus, fileIO


def hexToAscii(hexString):

    bytes_object = bytes.fromhex(hexString)
    return bytes_object.decode('ASCII')


def hexParser(string):
    return string.replace(":", " ")


def convert():
    while True:
        userInput = input(menus.hex2asciiPrompt)

        if userInput in ["file", "open"]:
            hexFile = fileIO.readwriteFile("r")
            for line in hexFile:
                print(hexToAscii(line))

        else:
            try:
                if userInput.lower() not in ["exit", "quit", "q", "help"]:
                    print(hexToAscii(userInput))
                elif userInput.lower() == "help":
                    print(f"Help Menu")
                else:
                    break
            except ValueError:
                print(f"""{colors.red}{colors.bad} Invalid entry.
                 Valid formats are ' ' or ':' separated
                 Try 'help'.{colors.end}""")
