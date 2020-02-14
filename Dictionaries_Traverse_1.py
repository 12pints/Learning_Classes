myDictionary={"BMW-M5":4,"AudiRS6":10,"CitroenSM":3,"Rolls Royce":19}

#sop let us iterate over the list and let it flag if  a certain car count gets low
for value in myDictionary.values():
    if value < 5:
        print("Your are about to run out of certain cars, only a few left:", value)

#this is not useful, as it does not provide which cars have a low count
#so let us iterate over the keys as well
print("now try something else..................")
for key in myDictionary.keys():
    value=myDictionary[key]
    if value < 5:
        print(key,"is less than 7, namely:",value)

