"""
3.	Print list in reverse order using a loop
"""
def reverse_list(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i], end=" ")

if __name__ == '__main__':
    aList = []
    #E.g: Enter a list of numbers separated by spaces: 1 2 3 4 5
    aList.extend(map(int, input("Enter a list number separated by spaces: ").split()))
    # Output: 5 4 3 2 1
    reverse_list(aList)