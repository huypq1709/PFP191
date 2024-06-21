"""1.	Removal all characters from a string except integers"""
def remove_all_except_integers(s):
    return ''.join([char for char in s if char.isdigit()])
if __name__ == '__main__':
    str1 = input("Enter a string: ")
    print(f"Output: {remove_all_except_integers(str1)}")