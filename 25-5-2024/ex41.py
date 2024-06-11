"""
41.	Write a function in programming to find prime numbers between two intervals using function.
"""
def printPrime(num1, num2):
    demus = 0
    for num1 in range(num1,num2+1,1):
        for i in range(1,num1+1,):
            if num1 %i == 0:
                demus = demus +1
        if demus ==2 :
            return True
        else:
            return False

a = int(input("Enter a: "))
b = int(input("Enter b: "))
prime = printPrime(a, b)




