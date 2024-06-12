"""
66.	Write a program to string optimization:
A string is optimal when: Does not contain redundant spaces, words are separated by a space, first character of uppercase words.
Ex: 	Input: LE    tHi HonG       Nga
Output: Le Thi Hong Nga
"""
def optimize_string(s):
    words = s.split()
    optimized_words = [word.capitalize() for word in words]
    optimized_string = ' '.join(optimized_words)
    return optimized_string

input_string = "LE tHi HonG Nga"
print(optimize_string(input_string))