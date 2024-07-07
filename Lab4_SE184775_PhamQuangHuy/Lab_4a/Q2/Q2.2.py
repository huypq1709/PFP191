file_path = r"E:\demos\files\write_demo.txt"
fp = open(file_path, 'r')
print(fp.read())
fp.close()

fp = open(file_path, 'w')
fp.write("This is overwritten content")
fp.close()

fp = open(file_path, 'r')
print("Opening file again..")
print(fp.read())
fp.close()