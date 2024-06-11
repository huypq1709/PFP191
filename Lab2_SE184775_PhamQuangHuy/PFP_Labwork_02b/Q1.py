"""
Q1  (2.5 marks). Write a  program that performs the following tasks:
1.	Input an integer number  n, where  n > 5 (If  n≤ 5 then prompt a user to re-enter). Then calculate
2.	S1 = 1 + 2 + 3 + ... + n.
3.	S2 = n!
4.	S3 = 1+ 1/2 + 1/3 +...+ 1/n .
5.	Re-input n. Check whether n is a prime number or not.

"""
from math import *

n = 0
while n <= 5:
    n = int(input("Enter an integer number: "))

def calculate(num):
    s1 = 0
    s3 = 0
    for i in range(1, num + 1, 1):
        s1 += i
        s3 += 1/i
    print(f"S1 = 1 + 2 + 3 + ... + n = {s1}")
    print(f"S2 = n! = {factorial(n)}")
    print(f"S3 = 1+ 1/2 + 1/3 +...+ 1/n = {s3}")

if __name__ == "__main__":
    calculate(n)



