"""
47.	Write a program to input a positive integer n. Print all “perfect numbers” less than n.
"""


def is_perfectNumber(n):
    s =0
    for i in range(1,n,1):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False

n = int(input("Enter a positive integer n: "))
for i in range(1,n+1,1):
    if is_perfectNumber(i):
        print(i,end=" ")

