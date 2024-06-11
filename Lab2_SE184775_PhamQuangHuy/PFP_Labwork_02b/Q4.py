"""
Q4 (2.5 marks). Write a program to accept  2  integer numbers  m and n, where m < n then
Display all palindrome numbers in the interval [m.n].
(A palindromic number or numeral palindrome is a number that remains the same when its digits are reversed, e.g. 16461)
"""


def check_palindrome(num):
    if num % 10 == num // (10 ** (len(str(num)) - 1)):
        return True
    else:
        return False

def print_palindrome(a, b):
    for i in range(a, b + 1, 1):
        if check_palindrome(i):
            print(i, end=" ")


if __name__ == "__main__":
    while True:
        try:
            m = int(input("Enter m: "))
            n = int(input("Enter n: "))
            if m < n:
                break
            else:
                print("m must be less than n. Please enter again.")
        except ValueError:
            print("Invalid input. Please enter integers for m and n")

    print_palindrome(m,n)




