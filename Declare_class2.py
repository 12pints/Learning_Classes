class Name:
    #create new instance
    def __init__(self):
        #persons default values
        self.firstname ="[no first name]"
        self.lastname = "[no last name]"

myNameDict= {"firstname": "David", "lastname": "Dusjofnie"}

myNameInst = Name()
myNameInst.firstname="David"
myNameInst.lastname="Dusjofnie"

print("Dictionary:" + myNameDict["firstname"])
print("Instance:" + myNameInst.firstname)