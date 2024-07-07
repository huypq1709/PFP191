with open(r'E:\demos\files_demos\test.txt', "rb") as fp:

    fp.seek(-40, 2)
    print(fp.read(11).decode("utf-8"))
