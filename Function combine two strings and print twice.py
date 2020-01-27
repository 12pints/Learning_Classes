# Given two strings, a and b, return the result of putting them together in the order abba,
# e.g. "Hi" and "Bye" returns "HiByeByeHi".


# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(str1, str2):
    # output=((str1+str2),2)
    
    output=str((str1+str2)*2)
    return output
    
    
str1=input('enter 1st string here:')
str2=input('enter 2nd string here:')
print(make_abba(str1, str2))
#print(output)
