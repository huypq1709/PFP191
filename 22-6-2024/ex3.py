"""Write a Python program to sum all the items in a dictionary."""
def sum_dict(d):
    s = 0
    for i in d.values():
        s += i
    return s
if __name__ == '__main__':
    dict1 = {'a': 100, 'b': 200, 'c': 300}
    print(sum_dict(dict1))