"""
Write a program to input two positive integers a and b. Find the greatest common divisor and least common multiple of a and b.
"""


# def UCLN(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
def UCLN(a,b):
    mod = a%b
    

def BCNN(a, b):
    mul = a * b
    uc = UCLN(a, b)
    bc = mul / uc
    return bc


if __name__ == "__main__":
   a = int(input("Enter a: "))
   b = int(input("Enter b: "))
   uc = UCLN(a, b)
   bc = BCNN(a,b)
   print(f"UCLN = {uc}\nBCNN = {bc}")