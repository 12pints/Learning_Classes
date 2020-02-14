

inputFile = open("carList.txt", "r")
lines = inputFile.readlines()
new_list = []
for i in lines:
    print (i)
    new_list.append(i.strip())

inputFile.close()

print(new_list)