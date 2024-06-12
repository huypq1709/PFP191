"""
66. Write a program to count number strings with a length greater than 2 and with the first and last characters being the same in a list.

Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

"""
def count_strings(lst):
    count = 0
    for s in lst:
        if len(s) > 2 and s[0] == s[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyz', 'aba', '1221']
print(count_strings(sample_list))