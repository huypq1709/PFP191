"""

66. Write a program to find the string with the maximum length in a list of strings.
Sample List : ["apple", "banana", "kiwi", "grape", "orange"]
Expected Result : banana, orange

"""
def find_max_length_strings(lst):
    max_length = max(len(s) for s in lst)
    result = [s for s in lst if len(s) == max_length]
    return result

sample_list = ["apple", "banana", "kiwi", "grape", "orange"]
print(find_max_length_strings(sample_list))