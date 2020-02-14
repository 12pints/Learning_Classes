#let write some script that goes over some text and counts all words to see how often the indivudually occur

myString="Schonis heeft tijdens een debat over ’duurzaam vervoer’ staatssecretaris Van Veldhoven, gevraagd om te gaan praten met de branche. Hij ziet graag dat de populaire bestelwebsites als Bol.com en Zalando aan klanten laten zien hoeveel CO2-uitstoot er gepaard gaat met een rit."

#first thing we will need to do is remove the text from any garbage, so we can turn it into a dictionary
#each work is a dictionary key, with a value: its occurence
myString=myString.replace(".","")  #remove periods
myString=myString.replace(",","")  #remove commas
myString=myString.replace("'","")  #remove capostrophies
myString=myString.lower()  #turn into lower case

mySplitString=myString.split()  #split by spaces
#so now you actually have a list containing all the words
# print(mySplitString)    <----can be used to test a preliminary result

#now lets create a dictionary

wordDictionary={}   #create emoty dictionary
for word in mySplitString:    #For each word in splitString, iterate over it
    if word in wordDictionary:     #if the word is already in the dictionary, add 1 to the value, cos its found again
        wordDictionary[word] +=1
    else:
        wordDictionary[word]=1     #if the works is not YET in the dictionary, make count 1, cos its new

print(wordDictionary)

