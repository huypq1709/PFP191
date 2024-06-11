s2=0
mul2 = 1
n = int(input())
for i in range(1,n+1,1):
   for j in range(1,i,1):
        mul2 = mul2 *j
s2 += mul2

print(f"s2 = {s2}")