# this code has a dictionary with keys and values and writes them to a file in culumns
# no working yet feb 19 2020
# Dennis Mink


dict={'Citroen': 1, 'Maserati': 1, 'Ferrari': 1, 'BMW': 2, 'RollsRoyce': 1, 'AMGr': 1, 'AstonMartin': 1, 'Audi': 4}

# next we print the dictionary
out_filename = 'Dictionaries_examples_5_formatting_output.txt'
f = open(out_filename, 'w')
print(dict, file=f)

# next we break it up an print each key value pair on a new line (\n),
# you can see by the (  )  that the key value pairs are now tuples:

for key, value in dict.items():
     print((key, value), end="\n", file=f)


# so how do we now change the into plain colums that we can actually present in like a csv?
# we will use the items attribute that we apply to a dictionary, using double indent \t\t or tab

for k , v in dict.items():
        print(k+"\t\t", v)

f.close()