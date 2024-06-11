"""
Write a program to find the last prime number in a list. If the list has no prime numbers, print the last value of the list.
"""
def find_last_prime_number(aList):
    lst = []
    lst.extend(map(int, aList.split()))
    lst.reverse()
    for x in lst:
        count = 0
        for i in range(1, x+1):
            if x % i ==0:
              count += 1
        if count == 2:
            return x
    return lst[0]

n = input("Enter a list of numbers: ")
result = find_last_prime_number(n)
print(result)