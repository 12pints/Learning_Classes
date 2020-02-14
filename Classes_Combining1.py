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

print(myPerson1.name.firstname)
print(myPerson1.name.lastname)
print(myPerson1.eyecolor)
print(myPerson1.age)

#somthing about mutability, so previsously the person;s eye color was brown

myPerson2=myPerson1
myPerson2.eyecolor='blue'
print("my Person1 's eyecolor: "+myPerson1.eyecolor)
print("my Person2 's eyecolor: "+myPerson2.eyecolor)

#as you can see myPerson2 has also changed myPerson1's eyecolor, as these instances are mutable