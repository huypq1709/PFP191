"""
1.	Print the following pattern
Write a program to print the following number pattern using a loop.
"""
def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
if __name__ == '__main__':
    num = int(input("Enter the number: "))
    pattern(num)
