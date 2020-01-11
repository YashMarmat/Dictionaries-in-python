# Dictionaries-in-python

dictionary is defined as: d = {} or d = dict()
the "d" here is dictionary and the curley brackets {} contains key values. 
the keys in dictionary are basically srtings or numbers.
the following dictionary is empty because there is no key value.

d ={}  this is an empty dictionary

d['three'] = 3 its a non empty dictionary having key-value pair. 

Here, key is 'three' and value is '3'

where, 'd' means dicitonary.


# Note: Dictionary doesn't care about the order of reperesenting output, means it does not provide output in a sorted manner. But still sorting can be done in dictionary (shown in dictionary file at line number 84)



# Dictionary
Here "yash" is a key and its value is 10

d["yash"] = 10

A key’s value can be a number, a string, a list, or even another dictionary. 

Apple = {'color':'red', 'quantity':1}

print(Apple['color'])

print(Apple['quantity'])

# Accessing values in Dictionary
# Method 1:

alien_0 = {'color': 'green', 'points': 5}

print('you just earned ' + str(alien_0['points']) + ' points') # using str as integer values need to be converted in string.

output: ("You just earned " + alien_0['points']+" points!")

# Method 2:

new_points = str(alien_0['points'])

print("You just earned " + new_points +" points!")

# Starting with an Empty Dictionary

New_D = {}

New_D['PC'] = 'Laptop'

New_D['Company'] = 'Sony'

print(New_D)

output: {'PC': 'Laptop', 'Company': 'Sony'}

# Modifying Values in a Dictionary

taking 'Mango' dictionary: changing the price

print('Earlier Price of Mango\n' + str(Mango))

print('\n')

Mango['Price']=15

print('New Price of Mango\n' + str(Mango)) 

output:
Earlier Price of Mango
{'Color': 'yellow', 'Taste': 'sweet', 'Price': 10, 'Weight(g)': 200}

New Price of Mango
{'Color': 'yellow', 'Taste': 'sweet', 'Price': 15, 'Weight(g)': 200}

# Removing Key-Value Pairs 

print(Mango)

print('\n')

del Mango['Weight(g)']

print(Mango)

output:
{'Color': 'yellow', 'Taste': 'sweet', 'Price': 13, 'Weight(g)': 200}

{'Color': 'yellow', 'Taste': 'sweet', 'Price': 13}

# A Dictionary of Similar Objects: 
A dictionary containing large number of key-value pairs.
When you know you’ll need more than one line to define a dictionary, press enter after the opening brace,
Then indent the next line one level (four spaces), and write the first key-value pair, followed by a comma.

# format of defining:

favorite_languages = {  

    'jen': 'python',    
    'sarah': 'c',    
    'edward': 'ruby',    
    'phil': 'python',    
    }
    
 * see dictionary file for more :)
