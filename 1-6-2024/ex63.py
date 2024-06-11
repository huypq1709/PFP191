"""
63.	 Write a program to input an integer number x. Find the first index of x in the list. If list has not x, return -1.
"""

def findX(num, aList):
    lst = []
    lst.extend(map(int , aList.split()))
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return -1

n = int(input("Enter a integer number x: "))
nums = input("Enter a list of numbers: ")
result = findX(n,nums)
print(result)
