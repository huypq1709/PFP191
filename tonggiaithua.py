from math import *
n = int(input("Enter n: "))
s = 0
for i in range(1,n+1,1):
    s +=  factorial(i)
print(f"S = {s}")