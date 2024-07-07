"""
1.	A text file named "matter.txt" contains some text, which needs to be displayed such that a symbol "# separates every next character." Write a function definition for hash_display() in Python that would show the entire content of the file matter.txt in the desired format.
Example :
If the file matter.txt has the following content stored in it :
THE WORLD IS ROUND

The function hash_display() should display the following content :
T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

"""
def hash_display(filename="matter.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                for char in line:
                    print(char, end="#")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

hash_display()
