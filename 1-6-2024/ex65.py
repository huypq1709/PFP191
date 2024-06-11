"""
65. Write a program to find strings with a length greater than 2 and with the first and last characters being the same in a list
Sample List : ["abc", "xyz", "aba", "12321", "apple", "banana"]
Expected Result: ['aba', '12321']
"""
def check(aList):
    for x in aList:
        if str(x).startswith('1') == str(x).endswith('1'):
            print(x)

lst = ["abc", "xyz", "aba", "12321", "apple", "banana"]
check(lst)

