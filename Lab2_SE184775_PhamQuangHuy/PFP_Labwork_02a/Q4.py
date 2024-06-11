"""
Q4 (2.5 marks). Write a program that performs the following tasks:
1.	Check Palindrome Number
A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
2.	Find the largest item from a given list
"""
def check_palindrome(num):
    print("original number ",num)
    if num % 10 == num // (10**(len(str(num))-1)):
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


check_palindrome(1331)
check_palindrome(1245)

x = [4,6,8,24,12,2]
print(max(x))
