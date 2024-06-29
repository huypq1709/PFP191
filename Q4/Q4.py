import math
# ----------------------------------------------------------------------
def isPrime(n):
    #Begin your statements here
    #...
    demus = 0
    for i in range(1, n + 1):
        if n % i == 0:
            demus += 1
    if demus == 2:
        return True
    pass
    #End your statements
# end isPrime
# ---------------------------------------------------------------------
def findMaxPrimeN2M(n, m):
    # Begin your statements here
    #...
    try:
        lst = []
        if n > m:
            for i in range(m, n+1):
                 if isPrime(i):
                    lst.append(i)
        else:
            for i in range(n, m+1):
                if isPrime(i):
                   lst.append(i)
        return max(lst)
    except:
        return 0

    #End your statements
# end findMaxPrimeN2M
# ===========DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("TEST Q4 (3 marks):")
    n = int(input("Enter n = "))
    m = int(input("Enter m = "))
    max_prime = findMaxPrimeN2M(n, m)
    print("\nOUTPUT:")
    print(max_prime)
# end main
if __name__ == "__main__":
    main()
# ================================================================================
