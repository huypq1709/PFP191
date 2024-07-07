"""
2.	Write a function in Python to count the number of lines from a text file "story.txt," which is not starting with an alphabet "T."
Example: If the file "story.txt" contains the following lines:
A boy is playing there.
There is a playground.
An airplane is in the sky.
The sky is pink.
Alphabets and numbers are allowed in the password.
Output: 2
"""
def count_lines_not_starting_with_t(filename="story.txt"):
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                if not line.lstrip().startswith("T"):
                    count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return count

# Example usage
print(f"No of lines not starting with 'T': {count_lines_not_starting_with_t()}")