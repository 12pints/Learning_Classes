#defione class Person

class Person:
    #create new instance
    def __init__(self):
        #persons default values
        self.firstname ="[no first name]"
        self.lastname = "[no last name]"
        self.eyecolor = "[no eye color]"
        self.age= -1

myPerson = Person()
#print myPerson's values
print(myPerson.firstname)
print(myPerson.lastname)
print(myPerson.eyecolor)
print(myPerson.age)


#now ifd the firstname is actually set:
myPerson.firstname="jimmy_James_RyanFrom Iowa"

print(myPerson.firstname)


myPerson1=Person()
myPerson2=Person()

myPerson1.firstname="Jimmy"
myPerson2.firstname="Porky"

print("myPerson1: " +  myPerson1.firstname)
print("myPerson2: " +  myPerson2.firstname)