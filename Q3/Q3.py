import string
#-----------------------------------------------------------------------------
def countConsonant(c1, c2):
    # Begin your statements
    #....
    count = 0
    c1 = ord(c1.lower())
    c2 = ord(c2.lower())
    if c1 < c2:
        for i in range(c1, c2+1):
            if chr(i).lower() in string.ascii_lowercase and chr(i).lower() not in "aeiou":
                count += 1
    else:
        for i in range(c2, c1+1):
            if chr(i).lower() in string.ascii_lowercase and chr(i).lower() not in "aeiou":
                count += 1
    return count
    pass
    #End your statements
#end countConsonant
#==========DO NOT ADD NEW OR CHANGE THE STATEMENTS IN THE MAIN FUNCTION========
def main():
    print("TEST Q3 (2 marks):")
    c1 = input("Enter c1 = ")
    c2 = input("Enter c2 = ")
    count = countConsonant(c1, c2)
    print("\nOUTPUT:")
    print(count)
#end main
if __name__ == "__main__":
    main()
#==============================================================================
