"""
2.	Aditi has used text editing software to type some text. After saving the article as WORDS.TXT, she realized that she had wrongly typed alphabet J in place of the alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
Example:
If Aditi has stored the following content in the file WORDS.TXT:
WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE
The function JTOI() should display the following content:
WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE.
"""
def JTOI(filename="WORDS.TXT"):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.replace("J", "I"), end="")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

JTOI()
