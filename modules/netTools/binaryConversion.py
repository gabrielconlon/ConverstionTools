#!/usr/bin/env python3

import argparse
from resources import menus, colors

parser = argparse.ArgumentParser()

parser.add_argument("-bin2dec", help="convert decimal to binary", type=str)

def convertIP_toBinary():
    while True:
        userInput = input(menus.dec2binPrompt)
        try:
            if userInput.lower() not in ["exit", "quit", "q", "help"]:
                print('.'.join(bin(int(octet) + 256)[3:] for octet in userInput.split('.')))
            elif userInput.lower() in "help":
                print(f"Help Menu")
            else:
                break
        except:
            print(f"{colors.red}{colors.bad}Invalid input.{colors.end}")

def convert_binary2decimal():
    while True:
        userInput = input(menus.bin2decPrompt)

        if userInput.lower() not in ["exit", "quit", "q", "help"]:
            try:
                if "." in userInput or " " in userInput:
                    ipOctets = userInput.split(".")
                    for idx, binary in enumerate(ipOctets):
                        decimal, count, n = 0, 0, 0
                        binary = int(binary)
                        while (binary != 0):
                            dec = binary % 10
                            decimal = decimal + dec * pow(2, count)
                            binary = binary // 10
                            count += 1
                        ipOctets[idx] = decimal
                    print(*ipOctets, sep=".")
                else:
                    binary = int(userInput)
                    decimal, count, n = 0, 0, 0
                    while (binary != 0):
                        dec = binary % 10
                        decimal = decimal + dec * pow(2, count)
                        binary = binary // 10
                        count += 1
                    print(decimal)
            except:
                print(f"{colors.red}{colors.bad}Invalid entry.{colors.end}")
        elif userInput.lower() in "help":
            print(f"Help Menu")
        else:
            break