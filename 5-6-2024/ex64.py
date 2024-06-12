"""
64.	Using loop, allows input of a string and check this string symmetric or not. Ask the user whether to continue the software. If continue, enter a new string, otherwise exit and thank you.

"""


def is_symmetric(s):
    return s == s[::-1]


while True:
    s = input("Enter a string: ")
    if is_symmetric(s):
        print("The string is symmetric.")
    else:
        print("The string is not symmetric.")

    continue_choice = input("Do you want to continue? (yes/no): ")
    if continue_choice.lower() != "yes":
        print("Thank you!")
        break