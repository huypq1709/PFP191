person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
fp = open("write_demo.txt", "w")
fp.writelines(person_data)
fp.close()

fp = open("write_demo.txt", "r")
print(fp.read())
fp.close()