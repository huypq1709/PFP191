with open(r'E:\demos\files_demos\test.txt', "r+") as fp:
    fp.seek(0, 2)

    fp.write("\nThis content is added to the end of the file")

    fp.seek(0)
    print(fp.read())