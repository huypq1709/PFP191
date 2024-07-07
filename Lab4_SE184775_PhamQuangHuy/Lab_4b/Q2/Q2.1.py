"""
1.	Write a function in Python to count and display the total number of words in a text file.
"""
def count_words(filename="poem.txt"):
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                count += len(line.split())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return count

# Example usage
print(f"Total number of words: {count_words()}")