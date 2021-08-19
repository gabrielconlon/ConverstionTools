from resources import colors

def readwriteFile(option):
    if option == "r":
        try:
            file = input(f"{colors.yellow}Filename: {colors.end}")
            f = open(file, option)
            return f.readlines()
        except FileNotFoundError:
            print(f"{colors.red}{colors.bad} Invalid filename or path.{colors.end}")
            return []
