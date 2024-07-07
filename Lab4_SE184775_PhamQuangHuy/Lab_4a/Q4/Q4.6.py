import glob
import os

# Old and new folder locations
old_folder = r"E:\demos\files\reports\\"
new_folder = r"E:\demos\files\new_reports\\"

# Old and new file names
old_name = old_folder + "expense.txt"
new_name = new_folder + "expense.txt"

# Moving the file to the another location

os.rename(old_name, new_name)