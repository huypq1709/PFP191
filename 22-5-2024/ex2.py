"""Kiểm tra số nguyên tố"""
n = int(input("Enter a number: "))
for i in range(2,n,1):
    if n % i == 0 :
        print("n is not the prime number")
        break

else:
    print("n is the prime number")