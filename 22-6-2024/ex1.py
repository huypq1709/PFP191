"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
"""
def count_letters(string):
    counts = dict()
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1
    return counts
if __name__ == "__main__":
    string = 'w3resource'
    print(count_letters(string))