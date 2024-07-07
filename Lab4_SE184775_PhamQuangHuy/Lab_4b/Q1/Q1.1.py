def read_and_display_poem(filename="poem.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.rstrip("\n"))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_and_display_poem()
