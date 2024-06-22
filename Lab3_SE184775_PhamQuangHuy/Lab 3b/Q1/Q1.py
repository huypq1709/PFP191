"""
1.	An anagram is a word or a phrase made by transposing the letters of another word or phrase; for example, "parliament" is an anagram of "partial men," and "software" is an anagram of "swear oft." Write a program that figures out whether one string is an anagram of another string. The program should ignore white space and punctuation.
"""
def is_anagram(str1, str2):
    workingCopy1 = removeJunk(str1)
    workingCopy2 = removeJunk(str2)

    workingCopy1 = workingCopy1.lower()
    workingCopy2 = workingCopy2.lower()

    workingCopy1 = sorted(workingCopy1)
    workingCopy2 = sorted(workingCopy2)

    return workingCopy1 == workingCopy2
def removeJunk(s):
    return ''.join([char for char in s if char.isalpha()])
if __name__ == '__main__':
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    if is_anagram(s1, s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
