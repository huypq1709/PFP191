"""
63.	 Write a program that allows input of a string. Output request:
How many capital letters?
How many lowercase letters
How many letters are digits?
How many letters are special characters?
How many letters are spaces?
How many words are vowels?
How many letters are consonants?
"""


def check_capital(aString):
    count = 0
    for letter in aString:
        if letter.isupper():
            count += 1
    return count


def check_lowercase(aString):
    count = 0
    for letter in aString:
        if letter.isupper():
            count += 1
    return count


def check_digits(aString):
    count = 0
    for letter in aString:
        if letter.isupper():
            count += 1
    return count


def check_special(aString):
    count = 0
    for letter in aString:
        if letter.isalnum():
            count += 1
    return count


def check_space(aString):
    count = 0
    for letter in aString:
        if letter.isspace():
            count += 1
    return count

def check_vowels(aString):
    count = 0

    for letter in aString:
        if letter =='a' or letter =='u' or letter =='o' or letter =='i' or letter =='e' or letter =='A' or letter =='U' or letter =='O' or letter =='I' or letter =='E':
            count += 1

    return count
def check_consonants(aString):
    count = 0
    for letter in aString:
        if letter != 'a' or letter != 'u' or letter != 'o' or letter != 'i' or letter != 'e' or letter != 'A' or letter != 'U' or letter != 'O' or letter != 'I' or letter != 'E':
            count += 1

if __name__ == "__main__":
    str1 = str(input("Enter a string: "))
    result = check_space(str1)
    print(result)
