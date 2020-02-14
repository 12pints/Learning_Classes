myList=[]  #declare empty list


#open input file read only
inputFile=open("inputFileVoetbal.txt", "r")

#for each line in the input file, Python does this automagically, when opening the file
#i.e. it automatically iterates over each line in the input file, stripping white space
for line in inputFile:
    myList.append(line.strip())

print(myList)

inputFile.close()