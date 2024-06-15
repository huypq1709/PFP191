# write file
file = open('demo.txt','w')
file.write('Hello World\n')
file.write('This is my new text file to test \n')
file.close()

# print file
file = open('demo.txt','r')
for line in file:
    print(line)
file.close()
# Add Hello World

# file = open('demo.txt','a')
file.write('Hello World\n')
# file.close()

# print file again
file = open('demo.txt', 'r')
for line in file:
    print(line)
file.close()

