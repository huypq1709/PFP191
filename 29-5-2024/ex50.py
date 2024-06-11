"""
Write a program to find the sum of all values of a list.
"""


def sum_list(nums):
   lst = []
   lst.extend(map(int, nums.split()))
   s = 0
   for x in lst:
       s += x
   return s

n = input("Enter a list of integers separated by spaces: ")
result = sum_list(n)
print(f"Sum of all values: {result}")