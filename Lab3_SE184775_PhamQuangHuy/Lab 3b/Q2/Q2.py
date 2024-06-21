"""2.	Write a program that reads a string from the user. If all the characters in the string are hexadecimal digits, print out the corresponding base-10 value. If not, print out an error message."""
def check_hexadecimal(string):
    if all(c in "0123456789ABCDEF" for c in string):
        print(f"Base-10 value: {int(string, 16)}")
    else:
        print("Error: Not all characters are hexadecimal digits")

if __name__ == "__main__":
    str1 = input("Enter a string: ")
    check_hexadecimal(str1)