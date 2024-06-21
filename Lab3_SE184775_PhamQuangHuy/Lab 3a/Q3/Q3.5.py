"""
5.	Count all letters, digits, and special symbols from a given string
"""
def count_all(str):
    letters = 0
    digits = 0
    special = 0
    for char in str:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    return letters, digits, special
if __name__ == "__main__":
    str1 = input("Enter a string: ")
    l, d, s = count_all(str1)
    print(f"Letters: {l}\nDigits: {d}\nSpecial: {s}")