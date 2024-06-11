"""
Write a program to input two or more numbers from user and find maximum and minimum of the given numbers using functions.
"""


def isPrime(num):
    demus = 0
    for i in range(1, num + 1):
        if num % i == 0:
            demus = demus + 1
    if demus == 2:
        return True
    else:
        return False


num = int(input("Input n: "))
result = isPrime(num)
if result:
    print("Yes")
else:
    print("No")
