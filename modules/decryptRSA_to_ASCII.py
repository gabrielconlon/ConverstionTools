from resources import colors, menus

# Global Variables
decrypted_string = ''
c = 0
m = 0
d = 8743
n = 10403
e = 0

#config
def config():
    # TODO: write configuration script
    print("Configuration Menu Placeholder")
    # usr_n = int(input(f'\tEnter n (default 10403): ') or '10403')
    # usr_d = int(input('\tEnter d (default 8743): ') or '8743')

# Encryption
def encrypt():
    print(f'{colors.info}Encryption not yet supported.')

# Decryption
def decrypt():
    # TODO: check if n and d were given in the commandStream Tuple
    # TODO: check length of Tuple, consider what to do next based off that

    deryptString = []
    # parse args
    # if len(args) > 2:
    #     for commandSegment in args:
    #         commandStream.append(commandSegment)
    # else:
    #     commandStream = str(args)

    # decrypt options

    # write to file (-w | -write)
    # input from file (-f | -file)

    menus.helpMenu("decryptRSA")
    decryptedMessage = ""
    while True:
        command = input(f"{colors.yellow}NetTools >> decryptRSA >>{colors.end}")
        if command[0] in '1234567890':
            for c in command.split(','):
                m = pow(int(c), d, n)
                decryptedMessage = decryptedMessage + chr(m)
            print(f'ASCII: {decryptedMessage}')
        elif command.lower() in 'main':
            return
        elif command.lower() in 'quit':
            print('Goodbye')
            quit()
        elif command.lower() in 'help':
            menus.helpMenu("decryptRSA")
        elif command.lower() in 'clear':
            decryptedMessage = ''
            print(f'ASCII: {decryptedMessage}')
        elif command.lower() in 'delete':
            decryptedMessage = decryptedMessage[:-1]
            print(f'ASCII: {decryptedMessage}')
        elif command.lower() in 'config':
            config()

def menu_controller(user_choice):
    if len(user_choice) > 2:
        if user_choice in 'decrypt':
            decrypt()
        elif user_choice in 'encrypt':
            encrypt()
        elif user_choice in 'help':
            print(f"""
            {colors.run}{colors.yellow}Encrypt: {colors.end}open RSA Encryption Toolkit
            {colors.run}{colors.yellow}Decrypt: {colors.end}open RSA Decryption Toolkit
            """)