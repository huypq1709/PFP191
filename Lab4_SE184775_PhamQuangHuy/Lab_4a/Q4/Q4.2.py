import os

folder = r'E:\demos\files\reports\\'
count = 1
for file_name in os.listdir(folder):
    source = folder + file_name

    destination = folder + "sales_" + str(count) + ".txt"

    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
res = os.listdir(folder)
print(res)