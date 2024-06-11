"""
Write a program to find the first prime number in a list. If the list has no prime numbers, print the first value of the list.
"""
def find_prime_number(aList):
    lst = []
    lst.extend(map(int, aList.split()))

    for x in lst:
        count = 0
        for i in range(1, x+1):
            if x % i == 0:
                count += 1
        if count == 2:
            return x
    return lst[0]

n = input("Enter a list of integers: ")
result = find_prime_number(n)
print(result)




