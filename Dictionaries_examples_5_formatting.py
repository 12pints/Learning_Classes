# this code has a dictionary with keys and values and writes them to a file in columns
# Code working 3/3/2020
# source:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
# Dennis Mink feb 2020

import pandas as pd

def header(msg):
    print('-'*75)
    print('['+msg+']')
    print('\n')

Cars_dict={'Citroen': [1,10], 'Maserati': [1,2], 'Ferrari': [1,2], 'BMW': [2,1], 'RollsRoyce': [1,3], 'AMG': [1,4], 'AstonMartin': [1,9], 'Audi': [4,1]}
print(type(dict))

# here is where we create a df thu panda, using the from_dict argument
# orient=index makes it print indexed in rows (default=column)
df=pd.DataFrame.from_dict(Cars_dict, orient='index')

# 1. next we print the dictionary, to screen and to file


header("1. Convert a library into a pandas dataframe and print to screen and file")

print(df)

out_filename = 'Dictionaries_examples_5_formatting_output.txt'
f = open(out_filename, 'w')

print(df, file=f)

f.close()

# 2. Adding column headers to the data frame, using pandas

header("2. Add a header name to existing df")

df.columns=['new Cars','old Cars']

f = open(out_filename, 'w')

print(df, file=f)

f.close()