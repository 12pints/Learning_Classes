# this code takes a dictionary and writes to file in columns delimited by TAB
# working Feb 20 2020
# Dennis Mink

import pandas as pd

order=['mix', 'meow']
#D = {'foo':{'meow':1.23,'mix':2.34}, 'bar':{'meow':4.56, 'mix':None}, 'baz':{'meow':None,'mix':None}} # working with this dict
D = {'Johnny':{1}, 'Jimmy':{1}, 'James': {1}, 'Keith': {2}}         #not working with this dict
df = pd.DataFrame(D).T.reindex(columns=order)

df.to_csv('./Dictionaries_7_example_output.txt', sep='\t', na_rep="none")