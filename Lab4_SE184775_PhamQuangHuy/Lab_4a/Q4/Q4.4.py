import os
from datetime import datetime

current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r"E:\demos\files\reports\sales.txt"
new_name = r"E:\demos\files\reports\sales" + current_timestamp + ".txt"
os.rename(old_name, new_name)