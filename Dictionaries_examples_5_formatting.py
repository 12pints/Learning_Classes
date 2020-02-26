# this code has a dictionary with keys and values and writes them to a file in columns
# partially working, need more args in the data frame creation, to make the car types columns
# source:  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.from_dict.html
# Dennis Mink feb 2020

import pandas as pd

def header(msg):
    print("-"*50)
    print("[+msg+]")
    print("\n")

Cars_dict={'Citroen': [1], 'Maserati': [1], 'Ferrari': [1], 'BMW': [2], 'RollsRoyce': [1], 'AMG': [1], 'AstonMartin': [1], 'Audi': [4]}
print(type(dict))

# here is where we create a df thu panda, using the from_dict argument
# orient=index makes it print indexed in rows (default=column)
df=pd.DataFrame.from_dict(Cars_dict, orient='index')

# next we print the dictionary, to screen and to file


header=("1. Convert a library into a pandas dataframe and print to screen and file")

print(df)

out_filename = 'Dictionaries_examples_5_formatting_output.txt'
f = open(out_filename, 'w')


print(df, file=f)

f.close()