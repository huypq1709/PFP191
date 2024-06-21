"""2.	Remove special symbols / punctuation from a string"""
import string
def remove_special(s):
    s = "/*Jon is @developer & musician"
    new_str = s.translate(str.maketrans('', '', string.punctuation))
    return new_str
if __name__ == "__main__":
    str1 = input("Enter a string: ")
    print(f"Output: {remove_special(str1)}")
