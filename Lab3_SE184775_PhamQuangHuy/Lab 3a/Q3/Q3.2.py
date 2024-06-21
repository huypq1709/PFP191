"""2.Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""
def append_string(s1, s2):
    return s1[:len(s1) // 2] + s2 + s1[len(s1) // 2:]
if __name__ == '__main__':
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    print(f"New string is: {append_string(str1, str2)}")