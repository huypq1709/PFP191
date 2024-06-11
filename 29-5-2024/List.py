"""
list rỗng: lst = []
list có giá trị: lst = [1,2,-3,0]
list có 10 phần tử với giá trị mặc định là 0: lst = [0]*10
list có 10 phần tử với giá trị mặc định là 0.5: lst = [0.5]*10
================================================================
Duyệt List
lst = [5,7,2,9,6,3,10,17,16]
for x in lst:
   print(x, end="\t")

lst = [5,7,2,9,6,3,10,17,16]
for i in range(len(lst)) :
    x = lst[i]
    print(x, end="\t")

lst = [5,7,2,9,6,3,10,17,16]
for i in range(len(lst)-1,-1,-1) :
    x = lst[i]
    print(x, end="\t")


"""
lst = [5,7,2,9,5,6,3,10,17,16]
lst.remove(5)
print(lst, end="\t")

