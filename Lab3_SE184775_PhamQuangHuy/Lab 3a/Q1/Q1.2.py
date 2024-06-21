"""2.Calculate the sum of all numbers from 1 to a given number"""
def sum_of_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
if __name__ == '__main__':
    num = int(input("Enter the number: "))
    sumOfAll = sum_of_numbers(num)
    print(f"Sum is {sumOfAll}")