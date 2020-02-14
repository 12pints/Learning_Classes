
list = ['a', 2, 'c']
#print(str(l))
print(str(list)[1:-1])
#print(str(list).replace(''',''))



def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')
