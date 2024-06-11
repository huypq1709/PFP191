"""
Q3  (2.5 marks). Write a  program that performs the following tasks:
1.	Input an integer number  n (check input validation), then
2.	Display n  in binary number format.
3.	Re-input n (not check input validation). Calculate the sum of all digits of n.
4.	Find the number m, which is the reverse of n.

"""
def get_integer():
    while True:
        try:
            n = int(input("Enter an integer number: "))
            return n
        except ValueError:
            print("Invalid input. Please enter an integer number again")

def sumOfDigits(a):
    s=0
    for i in range(1,len(str(a))+1,1):
        s += a % 10
        a = a // 10
    return s

def reverseNumber(b):
   return ''.join(reversed(b))

if __name__ == "__main__":
    num = get_integer()
    print(f"Binary number format: {bin(num)[2:]}")
    res = sumOfDigits(num)
    print(f"The sum of all digits of n: {res}")
    rev = reverseNumber(str(num))
    print(f"The reverse of n: {rev} ")

