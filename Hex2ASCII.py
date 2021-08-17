userinput = input('Enter your Hexidecimal string: ')
hex_string = userinput[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode('ASCII')
print(ascii_string)