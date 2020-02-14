def round_the_float(num):
     num = round(num, 2)
     return num

#result=round_the_float(3.1456)
#print(result)




a = 2.71828
a = round_the_float(a)
b = a

print(b)
#What is b's value when this line is reached?

# ###########################################################################
def absolute_reciprocal(an_int):
     abs(an_int)
     an_int = 1 / an_int
     return an_int



new_int = -5
print(absolute_reciprocal(new_int))
#What is new_int's value when this line is reached?

# ##########################################################################



def add_a_capitol(a_dict, a_state, a_city):
    a_dict = {a_state: a_city}

my_capitols = {"Georgia": "Atlanta", "Idaho": "Boise", "Maine": "Augusta"}
add_a_capitol(my_capitols, "Texas", "Austin")

print(my_capitols)
#What is the value of my_capitols when this line is reached?



