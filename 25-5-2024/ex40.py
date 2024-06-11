"""
40.	Write a program to input a positive integer n. Find the sum of prime less than n.
"""


def isPrime(k):
    demus = 0
    for i in range(1, k + 1):
        if k % i == 0:
            demus += 1
    if demus == 2:
        return True
    else:
        return False


def Sum(n):
    s = 0
    for i in range(1, n):  # n=10 , 1 2 3 4 5 6 7 8 9
        if isPrime(i) is True:
            s = s + i
    return s


if __name__ == '__main__':
    n = int(input("Enter n: "))
    result = Sum(n)
    print(f"Sum = {result}")
