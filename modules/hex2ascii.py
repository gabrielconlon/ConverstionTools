#!/usr/bin/env python3
from resources import colors, menus

def convert():
    while True:
        userInput = input(menus.hex2asciiPrompt)
        # if "-o" in args[1]:
        #     f = open(args[2], "r")
        #
        #     hexstring = f.readlines()
        #
        #     for line in hexstring:
        #         bytes_object = bytes.fromhex(line)
        #         # TODO: clean up to allow spaces, :, and all together
        #         ascii_string = bytes_object.decode('ASCII')
        #         print(ascii_string)
        # elif "-o" in args[2]:
        if userInput in ["file", "open"]:
            try:
                file = input(f"{colors.yellow}Filename: {colors.end}")
                f = open(file, "r")
            except FileNotFoundError:
                print(f"{colors.red}{colors.bad} Invalid filename or path.{colors.end}")

            hexstring = f.readlines()

            for line in hexstring:
                bytes_object = bytes.fromhex(line)
                # TODO: clean up to allow spaces, :, and all together
                ascii_string = bytes_object.decode('ASCII')
                print(ascii_string)

        else:
            try:
                if userInput.lower() not in ["exit", "quit", "q", "help"]:
                    hexstring = userInput.replace(":", " ")

                    bytes_object = bytes.fromhex(hexstring)
                    #TODO: clean up to allow spaces, :, and all together
                    ascii_string = bytes_object.decode('ASCII')
                    print(ascii_string)
                elif userInput.lower() == "help":
                    print(f"Help Menu")
                else:
                    break
            except ValueError:
                 print(f"""{colors.red}{colors.bad} Invalid entry.
                 Valid formats are ' ' or ':' separated
                 Try 'help'.{colors.end}""")
