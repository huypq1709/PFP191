"""
55.	Write a program to sort elements of a list in descending order
"""
def sort_Descending_List(nums):
    lst = []
    lst.extend(map(int, nums.split()))
    lst.sort(reverse=True)
    return lst

n = input("Enter a list of integers separated by spaces: ")
result = sort_Descending_List(n)
print(f"List in descending order: {result}")