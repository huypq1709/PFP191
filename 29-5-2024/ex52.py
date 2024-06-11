"""
52.	 Write a program to separate odd and even integers in separate list.
"""


def separate_Even(nums):
    lst = []
    lst.extend(map(int, nums.split()))
    even = []
    for x in lst:
        i = 0
        if x % 2 == 0:
            even.insert(i, x)
            i += 1
    return even


def separate_Odd(nums):
    lst = []
    lst.extend(map(int, nums.split()))
    odd = []
    for x in lst:
        i = 0
        if x % 2 != 0:
            odd.insert(i, x)
            i += 1
    return odd


n = input("Enter a list of the positive integers: ")
odd_list = separate_Odd(n)
even_list = separate_Even(n)
print(f"Odd List: {odd_list}")
print(f"Even List: {even_list}")
