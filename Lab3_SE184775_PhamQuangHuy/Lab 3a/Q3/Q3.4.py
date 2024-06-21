"""
4.	Arrange string characters such that lowercase letters should come first
"""
def arrange_string(s):
    lower = []
    upper = []
    for char in s:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    sorted_str = ''.join(lower + upper)
    return sorted_str

if __name__ == '__main__':
    str1 = input("Enter a string: ")
    print(f"String after arranging: {arrange_string(str1)}")

