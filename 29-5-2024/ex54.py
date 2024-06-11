"""
54.	Write a program to sort elements of a list in ascending order
"""
def sort_Ascending_List(nums):
    lst = []
    lst.extend(map(int, nums.split()))
    lst.sort()
    return lst

n = input("Enter a list of integers separated by spaces: ")
result = sort_Ascending_List(n)
print(f"List in ascending order: {result}")