"""
53.	Write a program to print all perfect numbers in a list.
"""
lst = []
pfn = []
n = input("Enter a list of integers separated by spaces: ")
lst.extend(map(int, n.split()))
for x in lst:
    s = 0
    for i in range(1,x,1):
        if x % i ==0:
            s += i
    if s == x:
        pfn.append(x)
print(pfn)