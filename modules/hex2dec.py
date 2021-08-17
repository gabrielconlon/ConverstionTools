"""
https://www.pythonpool.com/python-hexadecimal-to-decimal/
open and read file with hex chars
https://www.w3schools.com/python/python_file_write.asp
https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
"""

# any filename can be input, either just the name or starting with a / to navigate a directory
# TODO: stanardize file-input through argvars
#  (split after command, i.e. hextodexc (split) -f filename OR give a hex value typed in)
def convert():
    filename = input('Enter hex filename (directory listing is valid): ')

    with open(filename) as f:
        content = f.readlines()

    f.close()

    # for each line, strip and convert to dec

    for line in content:
        print(int(line.strip().replace(' ', '').replace(':', '').replace('.', ''), 16))
        dec = int(line.strip().replace(' ', '').replace(':', ''), 16)

    # prompt user to save
    save = input('Write to file (y/n)? ')
    # check input
    if save in 'yY':
        saveasfilename = input('Enter filename (directory listing is valid)(will append to existing file): ')
        f = open(saveasfilename, "a")
        f.write(str(dec))
        f.close()
    else:
        print('Goodbye')
        exit()

# content = [int(line.strip().replace(' ', '').replace(':', ''), 16) for line in open(input("Enter hex filename: "))]
# for decimal in content: print(decimal)
# if input("Write to file (y/n)? ") not in 'Yy': print('Goodbye'); exit();
# else:
#     with open(input('Save as: '), 'w') as f:
#         for x in content: f.write(str(x)+"\n")
