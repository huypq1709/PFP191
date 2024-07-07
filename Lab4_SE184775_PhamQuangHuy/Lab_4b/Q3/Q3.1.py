"""
1.	Write a function in Python to count uppercase characters in a text file.
"""
def count_uppercase_characters(filename="story.txt"):
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return count

# Example usage
print(f"Total number of uppercase characters: {count_uppercase_characters()}")