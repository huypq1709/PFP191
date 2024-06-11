"""
Q2 (2.5 marks). Write a program to accept  2  integer numbers  m and n, then:
1.	Display all common prime dividers of them.
2.	Find the greatest common divider (GCD) of them.
3.	Find the least common multiple (LCM) of them.
"""

from math import *
def isPrime(k):
    demus = 0
    for i in range(1, k + 1):
        if k % i == 0:
            demus += 1
    if demus == 2:
        return True
    else:
        return False
def printCommon(a, b):
    for i in range(1, min(a, b) + 1, 1):
        if a % i == 0 and b % i == 0:
            if isPrime(i):
                print(i,end=" ")


if __name__ == "__main__":
    m = int(input("Enter a number m: "))
    n = int(input("Enter a number n: "))
    print("All common prime dividers of them: ",end="")
    printCommon(m, n)
    print(f"\nGCD({m},{n}) = {gcd(m,n)}")
    print(f"LCM({m},{n}) = {lcm(m,n)}")
