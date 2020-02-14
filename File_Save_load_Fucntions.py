#Saves inList into a file, so write save and load functions, is more efficient

def save(filename, inList):
    outputFile=open(filename, "w")

    for item in inList:
        print(item, file=outputFile)

    outputFile.close()


def load(filename):
    inputFile=open(filename,"r")
    inList=[]

    for line in inputFile:
        inList.append(line.strip())
    inputFile.close()
    return inList

myList=["mercedes", "BMW","Volkswagen", "DAF", "Audi", "Rover", "Spkijker"]

save("carList.txt",myList)

newList=load("carList.txt")

print("you just saved the following list into a file and loaded that same file: \n")
print(newList)