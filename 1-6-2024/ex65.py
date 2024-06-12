"""
65. Write a program to find strings with a length greater than 2 and with the first and last characters being the same in a list
Sample List : ["abc", "xyz", "aba", "12321", "apple", "banana"]
Expected Result: ['aba', '12321']
"""
def find_strings(lst):
    result = []
    for s in lst:
        if len(s) > 2 and s[0] == s[-1]:
            result.append(s)
    return result

sample_list = ["abc", "xyz", "aba", "12321", "apple", "banana"]
print(find_strings(sample_list))

