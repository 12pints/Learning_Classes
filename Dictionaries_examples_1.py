# dictionaries, just a bit of playing around
# source:  https://www.youtube.com/watch?v=XCcpzWs-CI4
# let us create a dictionary

# in dictioanry below user_id, message, language, datetime and location are the KEYS
# 209, D5 E5 C5 C4 G4, Dutch, 20200212 and (44.590533, -104.715556) are the values
# btw, location is a tuple of floats
# so if you were to have a dictionary as a database, you could have different people in there with the same keys, but with different values
# for these keys


post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"Dutch","datetime":"20200212", "location":(44.590533, -104.715556)}

# if you run this in a python console, you would get:
# >>> type(post)
#  <class 'dict'>

print(post)

# let us create a partial dictionary, called post 2:

post2=dict(message="Quo Vadis", language ="German")
# now let us add separate keys and their respective values:

print(post2)

post2["user_id"]=208
post2["datetime"]="19771116T093001Z"


print(post2)

# now let us print only a subset oif keys and their values:

print('here is where I am printing a value for the msaage key from the dictionary post:')
print(post["message"])

# A1 print('here is where I am trying to print a value for a key location that is not in the post2 dictionary and creating an error:')
# A2 print(post2["location"])


# now I am going to add some exception handling:
# cos I have not yest added a key of location and value to my post2 dictonary
# if i was to print(post["message']) is would error out, test by uncommenting A1 and A2 lines above

print('error handling because location is not in my dictionary:')
if "location" in post2:
    print(post2["location"])

else:
    print('the post dict does not contain a location value')

try:
    print(post2['location'])

except KeyError:
    print("the post does not have a location")

print('*****Let us explore the get method:')
print(type(post2))

print('==this will print all the dictionary available methods:')
print('==note the get method and key method that we will use later')
print(dir(post2))

print('==this will print the output help on the get method:')
print(help(post.get))

# with the help you can see how to use the get method

print('==Here is where we start using the get method on our dictionary we made earlier:')

loc=post2.get('location, None')

print(loc)


print('=========Now let us iterate over the dictionary and return all the keys:')
for key in post.keys():
    value=post[key]
    print(key, "=", value)


print('======alternatively use the items method:')

for key, value in post.items():
    print(key, '=', value)

print('\n')
print('======now let us clear a key value, by using  the pop method:')

print(help(post.pop))

print('======now we know how to use the pop method, let us remove a key/value from our post dict and print the dict')
print('======you will see that the datetime key and value have been removed:')
print('\n')
pop_key=post.pop('datetime')

for key, value in post.items():
    print(key, '=', value)

