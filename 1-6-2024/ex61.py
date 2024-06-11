"""
61.	Write a program to count all even numbers in list.
"""
def countAllEven(nums):
    lst = []
    lst.extend(map(int,nums.split()))
    count = 0
    for x in lst:
        if x % 2 == 0:
            count +=1
    return count

n = input("Enter a list of numbers: ")
result = countAllEven(n)
print(f"Count all even numbers in list: {result}")