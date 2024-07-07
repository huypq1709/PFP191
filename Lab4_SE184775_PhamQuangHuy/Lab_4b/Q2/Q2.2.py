"""
2.	Write a function display_words() in Python to read lines from a text file "story.txt" and display those words less than 4 characters.

"""
def display_words(filename="poem.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word, end=" ")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

display_words()