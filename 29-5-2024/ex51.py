"""
51.	Write a program to calculate the sum of the maximum and minimum values in a list.
"""


def sum_maxMin(nums):
    lst = []
    lst.extend(map(int, nums.split()))
    s = max(lst) + min(lst)
    return s

n = input("Enter a list of integers separated by spaces: ")
result = sum_maxMin(n)
print(f"Sum of the maximum and minimum values in this list: {result}")
