"""
65.	Given 1 String as “5;7;8;-2;8;11;13;9;10”
- Output digits on separate lines
- How many even number?
- How many negative numbers?
- How many primes numbers?
- Calculate the average value.

"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

s = "5;7;8;-2;8;11;13;9;10"
numbers = list(map(int, s.split(';')))

even_count = 0
negative_count = 0
prime_count = 0
total = 0

for num in numbers:
    print(num)
    total += num
    if num % 2 == 0:
        even_count += 1
    if num < 0:
        negative_count += 1
    if is_prime(num):
        prime_count += 1

average = total / len(numbers)

print("Number of even numbers:", even_count)
print("Number of negative numbers:", negative_count)
print("Number of prime numbers:", prime_count)
print("Average value:", average)