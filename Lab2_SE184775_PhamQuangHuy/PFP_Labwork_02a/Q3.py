"""
Q3  (2.5 marks). Write a  program that performs the following tasks:
1.	Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
A recursive function is a function that calls itself, again and again.
2.	Assign a different name to function and call it through the new name
"""

def addition(n):
    s=0
    for i in range(0,n+1,1):
        s += i
    return s
res = addition(10)
print(res)

def display_student(name,age):
    print(name, age)

display_student("Emma",26)

show_student = display_student
show_student("Emma",26)