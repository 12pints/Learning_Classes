class Person:
    #create new instance
    def __init__(self, name, eyecolor, age):
        #persons default values
        self.name = name
        self.eyecolor = eyecolor
        self.age= age

class Name:
    #create new instance
    def __init__(self, firstname, lastname):
        #Name default values
        self.firstname = firstname
        self.lastname = lastname

# Create a person, and a

myPerson1=Person(Name("Pietje","Retief"),"brown", 30)

#now is we wanted to create a newPerson2, with same set of vaariables, but a seperate instcnce:

myPerson2=Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor="purple"


#so as you can see, we have created two separate instances; myperson1 and 2
print(myPerson1.eyecolor)
print(myPerson2.eyecolor)


myPerson2.name.firstname="Andre Joubert"
#anow lets print to see if we have copies

print(myPerson1.name.firstname)
print(myPerson2.name.firstname)