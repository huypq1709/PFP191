# Open file
file = open('test.txt','r')

# print file
for i in file:
    print(i)
file.seek(0)

# count the number of lines in file
inp = file.read()
print(len(inp))
file.seek(0)

#find the line that starts with 'Subject:'
for line in file:
    if line.startswith('Subject:'):
        print(line)
file.seek(0)
#Skipping with continue
for line in file:
    line = line.rstrip()
    if line.startswith('From'):
        continue
    print(line)
#Using in to Select Lines
file.seek(0)
for line in file:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
file.close()


