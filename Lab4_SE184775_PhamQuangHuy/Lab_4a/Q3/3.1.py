with open(r'E:\demos\files_demos\test.txt', "w+") as fp:
    # add content
    fp.write('My First Line\n')
    fp.write('My Second Line')
    fp.seek(0)
    # read file
    print(fp.read())
