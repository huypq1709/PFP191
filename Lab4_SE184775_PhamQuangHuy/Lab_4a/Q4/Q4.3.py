import os

files_to_rename = ['sales_1.txt', 'sales_4.txt']
folder = r"E:\demos\files\reports\\"

for file in os.listdir(folder):
    if file in files_to_rename:
        old_name = os.path.join(folder, file)
        only_name = os.path.splitext(file)[0]

        new_base = only_name + '_new' + '.txt'
        new_name = os.path.join(folder, new_base)

        os.rename(old_name, new_name)

res = os.listdir(folder)
print(res)
