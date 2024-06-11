from math import *
print("S(x,n)")
x = int(input("Enter x: "))
n = int(input("Enter n: "))
s=0
for i in range(1,n+1,1):
    s = s + ((x ** i) / (factorial(i)))
print(f"S(x,n) = {s}" )
