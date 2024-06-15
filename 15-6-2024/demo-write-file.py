fhand = open("write.txt", "w")
file = open('demo.txt','r')
for line in file:
    fhand.write(line)
file.close()
fhand.close()

fhand = open("write.txt", "r")
for line in fhand:
    print(line)
fhand.close()