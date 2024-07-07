with open(r'E:\demos\files_demos\test.txt', "rb") as fp:

    fp.seek(3)
    print(fp.read(5).decode("utf-8"))

    fp.seek(10, 1)
    print(fp.read(6).decode("utf-8"))
