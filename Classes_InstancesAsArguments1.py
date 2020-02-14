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

def capitalizeName(name):
    name.firstname=name.firstname.upper()
    name.lastname=name.lastname.upper()
# Create a person, and a

myPerson=Person(Name("Pietje","Retief"),"brown", 30)

capitalizeName(myPerson.name)
print(myPerson.name.firstname)
print(myPerson.name.lastname)