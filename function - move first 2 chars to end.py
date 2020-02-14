# Given a string, return a "rotated left 2"
# version where the first 2 chars are moved to the end. The string length will be at least 2.


# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
    output=str[2:]+str[:2]
    return output


str=input('Enter your input string here: ')
print(left2(str))


    
