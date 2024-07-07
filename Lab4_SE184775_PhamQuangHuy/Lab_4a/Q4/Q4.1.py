import os

old_name = r"E:\demos\files\reports\details.txt"
new_name = r"E:\demos\files\reports\new_details.txt"

if os.path.isfile(new_name):
    print("File name already exists. Cannot rename")
else:
    os.rename(old_name, new_name)