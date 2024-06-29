#-----------------------------------------------------------------------------
def sum(n,x):
    #Begin your statements
    #....
    s = 0
    for i in range(1, n+1):
        s += x * i
    return s
    pass
    #End your statements
#end sum

#==========DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("\nTEST Q2 (3 marks):")
    n = int(input("Enter n = "))
    x = int(input("Enter x = "))
    r = sum(n, x)
    print("OUTPUT:")
    print(r)
#end main
if __name__ == "__main__":
    main()
#==============================================================================
