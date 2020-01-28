# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(style, str):
    output='<'+style+'>'+str+'</'+style+'>' 
    return output
    
style=str(input('desired style e.g  b , cite, i:'))
str=str(input('what would you like to have HTML styled?:'))


print(make_tags(style,str))
    
    
