"""
49.	Write a program to input a list of integers and display it in reverse order.
"""


def reverse_list():
    lst = []
    n = input("Enter a list of integers: ")
    lst.extend(map(int, n.split()))
    lst.reverse()
    return lst

print(reverse_list())
