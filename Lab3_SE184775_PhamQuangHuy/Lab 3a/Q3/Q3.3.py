"""
3.	Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
"""
def new_string(s1, s2):
    return s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
if __name__ == '__main__':
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    print(f"New string is: {new_string(str1, str2)}")