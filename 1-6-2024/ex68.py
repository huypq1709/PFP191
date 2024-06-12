"""
67. Write a program to find the string with the minimum length in a list of strings.
Sample List : ["apple", "banana", "kiwi", "grape", "orange"]
Expected Result : kiwi
"""
def find_min_length_strings(lst):
    min_length = min(len(s) for s in lst)
    result = [s for s in lst if len(s) == min_length]
    return result

sample_list = ["apple", "banana", "kiwi", "grape", "orange"]
print(find_min_length_strings(sample_list))