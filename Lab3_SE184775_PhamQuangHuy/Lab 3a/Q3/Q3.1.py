"""
1.	Create a string made of the middle four characters.
"""
def middle_four_characters(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 2: len(s) // 2 + 2]
    else:
        return s[len(s) // 2 - 1: len(s) // 2 + 3]

if __name__ == '__main__':
    s = input("Enter a string: ")
    print(f"Middle four characters are: {middle_four_characters(s)}")