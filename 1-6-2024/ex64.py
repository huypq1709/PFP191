"""
64. Write a Python program to count the number of strings from a given list of strings and numbers.
Sample List : ['abc', 'xyz', 'aba', 1221]
Expected Result : 3
"""
def countString(aList):
    count = 0
    for x in aList:
        if str(x).isdigit() is False:
            count += 1
    return count

n = ['abc', 'xyz', 'aba', 1221]
result = countString(n)
print(result)