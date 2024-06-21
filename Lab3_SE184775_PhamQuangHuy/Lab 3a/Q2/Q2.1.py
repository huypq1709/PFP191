"""
1.	Display numbers from a list using loop
•	The number must be divisible by five
•	If the number is greater than 150, then skip it and move to the next number
•	If the number is greater than 500, then stop the loop
"""


def display_numbers(lst):
    for i in lst:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)


if __name__ == '__main__':
    aList = []
    #E.g: Enter a list of numbers separated by spaces: 154 75 150 102 145
    aList.extend(map(int, input("Enter a list number separated by spaces: ").split()))
    # Output: 75 150 145
    display_numbers(aList)
