import random
def Input(lst):
    n=int(input("n="))
    for i in range(n):
        x=int(input("x="))
        lst.append(x)
#random
def InputRandom(lst):
    n=int(input("n="))
    for i in range(n):
        x=random.randint(-1000,1000)
        lst.append(x)
def isPerfect(n):
    s=0
    for i in range(1,n):
        if n%i == 0:
            s=s+i
    if s==n:
        return True
    else:
        return False


#in tat ca cac so hoan thien
def PrintPerfect(lst):
    flag=0
    for i in lst:
        if (isPerfect(i)) == True:
            flag=1
            print(i)
    if flag==0:
        print(lst[0])


if __name__ =="__main__":
    lst=[]
  #  InputRandom(lst)
    Input(lst)
    print(lst)
    PrintPerfect(lst)

