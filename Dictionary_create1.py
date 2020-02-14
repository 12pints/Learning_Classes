#Let create an inventory of what we have in a garage
#the keys (BMW, AUDI etc are inmutable, the value of these key are mutable
myDictionary={"BMW-M5":3,"AudiRS6":10,"AMGTurbo":3,"Rolls Royce":19}
print(myDictionary)

#let modify the dictionary, say we added an audi RS to the garage

myDictionary["AudiRS6"] +=1

print(myDictionary)

#or we wanna see how many Rolls Royces we have

print("you have: ", myDictionary["Rolls Royce"], " Rolls Royces")

#lets say I sell, a couple rolls and i have 7 left:

myDictionary["Rolls Royce"] =7

print("you have: ", myDictionary["Rolls Royce"], " Rolls Royces")

#now I am adding 6 Maseratis to my collection

myDictionary["Maserati"] =6

print(myDictionary)

#I got fed up with the AMG;s cos they are not really that great

del myDictionary["AMGTurbo"]
print(myDictionary)