"""
Write a program to input two or more numbers from user and find maximum and minimum of the given numbers using functions
"""


def get_numbers():
    """
    Function to get a list of numbers from the user.
    """
    while True:
        try:
            numbers = list(map(float, input("Enter two or more numbers separated by spaces: ").split()))
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
            else:
                return numbers
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def find_maximum(numbers):
    """
    Function to find the maximum number in a list.
    """
    return max(numbers)


def find_minimum(numbers):
    """
    Function to find the minimum number in a list.
    """
    return min(numbers)


def main():
    """
    Main function to execute the program.
    """
    numbers = get_numbers()
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    print(f"The maximum number is: {maximum}")
    print(f"The minimum number is: {minimum}")


if __name__ == "__main__":
    main()
