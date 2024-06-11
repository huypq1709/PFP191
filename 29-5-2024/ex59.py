"""
59.	Write a program to find the last odd number in a list. If the list has no even numbers, print the last value of the list.
"""
def find_last_odd_number(aList):
    lst = []
    lst.extend(map(int, aList.split()))
    lst.reverse()
    for x in lst:
        if x % 2 != 0:
            return x
    return lst[0]

n = input("Enter a list of numbers: ")
result = find_last_odd_number(n)
print(result)