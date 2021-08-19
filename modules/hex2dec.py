from resources import menus, colors, fileIO
"""
https://www.pythonpool.com/python-hexadecimal-to-decimal/
open and read file with hex chars
https://www.w3schools.com/python/python_file_write.asp
https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
"""

def decParser(string):
    return int(string.strip().replace(' ', '').replace(':', ''), 16)

# any filename can be input, either just the name or starting with a / to navigate a directory
def convert():
    while True:
        userInput = input(menus.hex2decPrompt)

        if userInput in ["file", "open"]:
            hexFile = fileIO.readwriteFile("r")

            # for each line, strip and convert to dec
            for line in hexFile:
                # print(int(line.strip().replace(' ', '').replace(':', '').replace('.', ''), 16))
                print("{:,}".format(decParser(line)))

        else:
            try:
                if userInput.lower() not in ["exit", "quit", "q", "help"]:
                    print("{:,}".format(decParser(userInput)))
                elif userInput.lower() == "help":
                    print(f"Help Menu")
                else:
                    break
            except ValueError:
                print(f"""{colors.red}{colors.bad} Invalid entry.
                 Try 'help'.{colors.end}""")

# content = [int(line.strip().replace(' ', '').replace(':', ''), 16) for line in open(input("Enter hex filename: "))]
# for decimal in content: print(decimal)
# if input("Write to file (y/n)? ") not in 'Yy': print('Goodbye'); exit();
# else:
#     with open(input('Save as: '), 'w') as f:
#         for x in content: f.write(str(x)+"\n")
