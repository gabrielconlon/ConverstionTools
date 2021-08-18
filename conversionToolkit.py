#!/usr/bin/env python3

from modules import hex2dec
from modules import hex2ascii
from resources import colors

def switchCase(*args):

    switcher = {
        "help": print("Help Menu"), # lambda: menus.helpMenu("mainhelp"),
        "hex2ascii": lambda: hex2ascii.convert(),
        "hex2dec": lambda: hex2dec.convert()
    }

    try:
        func = switcher.get(args[0], lambda: print(f"{colors.red}{colors.bad}Invalid Input."))
        # func()
    except IndexError:
        print(f"""{colors.red}{colors.bad}Invalid number of arguments.
        Try 'help'""")

def main():
    command = input(f"{colors.yellow}ConversionTools >> {colors.end}")
    commandOptions = command.split(" ")
    if len(commandOptions) > 1:
        commandBase = commandOptions[0]
        del commandOptions[0]
        commandArgs = commandOptions[-1]
        del commandOptions[-1]
        switchCase(commandBase, commandOptions, commandArgs)
    else:
        commandBase = commandOptions[0]
        switchCase(commandBase)

if __name__ == "__main__":
    while True:
        main()

