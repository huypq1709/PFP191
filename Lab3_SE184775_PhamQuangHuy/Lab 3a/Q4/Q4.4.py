"""4.	Split a string on hyphens"""
def split_string(str1):
    sub_strings = str1.split("-")
    print("Displaying each substring")
    for sub in sub_strings:
        print(sub)
if __name__ == '__main__':
    s = input("Enter a string: ")
    split_string(s)

