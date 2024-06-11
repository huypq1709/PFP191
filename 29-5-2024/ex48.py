"""
48.	Write a program to input and output a list of integers.
"""
def input_list():
    lst = []
    n = str(input("Enter a list of integers separated by spaces: "))
    # hàm map là hàm ánh xạ
    lst.extend(map(int, n.split()))
    return lst

print(input_list())
