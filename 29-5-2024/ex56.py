"""
Write a program to find the first even number in a list. If the list has no even numbers, print the first value of the list.
"""
def find_even_number(aList):
    lst = []
    lst.extend(map(int, aList.split()))
    count = 1
    for x in lst:
        if x % 2 == 0:
            count += 1
            return x
    return lst[0]


n = input("Enter a list of integers: ")
result = find_even_number(n)
print(result)



