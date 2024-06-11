"""
62.	Write a program to find the average of all prime numbers of the list.
"""
def findAveragePrime(aList):
    lst = []
    lst.extend(map(int, aList.split()))
    s = 0
    count = 0
    for x in lst:
        demus = 0
        for i in range(1,x+1):
            if x % i == 0:
                demus +=1
        if demus == 2:
            s += x
            count += 1
    return s/count

n = input("Enter a list of numbers: ")
result = findAveragePrime(n)
print(result)
