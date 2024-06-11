"""
Write a program to input two numbers and perform all arithmetic operations: sum, difference, product, quotient and modulus.
"""
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
s = a+ b
sub = a-b
p = a*b
q = a/b
mod = a%b
print(f"\nSum: {s}")
print(f"Difference: {sub}")
print(f"Product: {p}")
print(f"Quotient: {q}")
print(f"Modulus: {mod}")