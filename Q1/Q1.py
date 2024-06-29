import  math
#----------------------------------------------------------------
def isPrime(number):
    #Begin your statements here
    #......
    demus = 0
    for i in range(1, number+1):
        if number % i == 0:
            demus += 1
    if demus == 2:
        return True
    pass
    #End your statements
#end isPrime
#----------------------------------------------------------------
def average(x):
    # Begin your statements here
    #.....
    count = 0
    s = 0
    i = 1
    while count < x:
        if isPrime(i):
            s += i
            count += 1
        i += 1
    return s / x
    pass
    #End your statements
#end average
#=============DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("\nTEST Q1 (2 marks):")
    x = int(input("Enter x = "))
    r = average(x)
    print("OUTPUT:")
    print("{:.2f}".format(r))
#end main
if __name__ == "__main__":
   main()

#====================================================================================
