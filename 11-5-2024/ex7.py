"""
7.	Write a program to input length and width of a rectangle and calculate perimeter and area of the rectangle.
"""
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
area = length * width
per = (length+width)*2

print(f"\nPerimeter: {per}\nArea: {area}")