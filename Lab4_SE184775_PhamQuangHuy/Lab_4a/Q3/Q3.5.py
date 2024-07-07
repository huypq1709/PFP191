# open file for reading and writing  r+
with open(r'E:\demos\files_demos\test.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())

    # writing new content
    fp.write("\nDemonstrating tell")

    print('file handle at:', fp.tell())

    fp.seek(0)
    print('file handle at:', fp.tell())

    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    print('file handle at:', fp.tell())
