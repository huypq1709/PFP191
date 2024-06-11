word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

if word == 'banana':
    print("All right, banana")

fruit = 'banana'
pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o','x')
print(nstr)