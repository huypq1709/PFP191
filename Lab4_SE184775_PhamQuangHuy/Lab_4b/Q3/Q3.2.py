"""
2.	Write a function in Python to count the words "this" and "these" present in a text file "article.txt". [Note that the words "this" and "these" are complete words]
"""
def count_words(filename="article.txt"):
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word.lower() == "this" or word.lower() == "these":
                        count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return count


print(f"Total number of words 'this' and 'these': {count_words()}")