"""
2.	Count the total number of digits in a number
"""
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count
if __name__ == '__main__':
    num = int(input("Enter the number: "))
    c = count_digits(num)
    print(f"Total number of digits are {c}")