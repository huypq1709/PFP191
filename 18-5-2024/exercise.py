"""
Calculate: 	 n!   (n>0)

	Calculate:	S(n)=1+3+5+⋯.+(2×n+1),       n≥0

	Calculate:	P(n)=1.3.5…(2.n+1),       n≥0

	Calculate:	S(n)=1+1.2+1.2.3+⋯+1.2.3….n,        n>0)

"""

n = int(input("Enter n: "))
mul = 1
s = 0
p = 1
for i in range(1,n+1,1):
    mul =mul * i
print(f"n! = {mul}")

for i in range(1,n+1,2):
    s += i
    p *= i
print(f"s = {s}")
print(f"p = {p}")




