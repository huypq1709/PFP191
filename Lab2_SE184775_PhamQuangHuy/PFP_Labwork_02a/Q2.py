"""
Q2 (2.5 marks). Write a program to accept  2  integer numbers  m and n, then:
1.	Create a function with default argument
2.	Create an inner function to calculate the addition in the following way
•	Create an outer function that will accept two parameters, a and b
•	Create an inner function inside an outer function that will calculate the addition of a and b
•	At last, an outer function will add 5 into addition and return it
"""
def showEmployee(name, salary = 9000):
    print(f"Name: {name} salary: {salary}")
showEmployee("Ben",12000)
showEmployee("Jessa")

def outer_fun(a,b):
    def addition(a,b):
        return a + b

    add = addition(a,b)

    return add + 5

result = outer_fun(5,10)
print(result)