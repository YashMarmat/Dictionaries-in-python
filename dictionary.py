# key-value pairs in dictionary
# simple introducion

info = {'first_name':'yash','last_name':'marmat','age':22,'city':'delhi'}
print('Full Name: ' + info['first_name'] + ' ' + info['last_name'])

# lets say we want more key-value pairs in above dictionary

info['interest'] = 'coding'
print(info)

# empty dictionary

info2 = {}   # empty dictionary
info2['name'] = 'sam'      # adding new key-value pair in an empty dictionary
info2['location'] = 'paris'
print(info2)

# modifying values in ditionary

fruits = {'Yellow':'Banana'}
# lets replace banana with mango
print(fruits)
fruits['Yellow'] = 'mango'
print(fruits)

# removing key-value pairs

info3 = {'first_name':'yash','last_name':'marmat','age':22,'city':'delhi','interest':'coding'}
print(info3)

del info3['interest']
print('\ndeleting interest field...')
print(info3)

# taking a poll

languages = {
    'sam':'c++',
    'jason':'python',
    'edward':'java',
    'peter':'c#'
}

print("Sam's favourite language is " + languages['sam'])

avoiding errors if a key-value pair is not assigned --> by get() method

bio = {
    'name':'yash',
    'age':22,
    'location':'delhi'
}

print(bio['interest'])  <-- this will give keyerror, so use below code

data = bio.get('interest','no such key-value pair is present')
print(data)
'''
# Sorting in dictionary
# Also, Dictionary and list together

f = {
    'bob':'python',
    'harry':'ruby',
    'jack':'c',
    'stan':'java',
    }

list1 = ['jack','stan']
for each in f.keys():
    print(each.title())
    
    if each in list1:
        print('hi ' + each.title()+' you said your fav lang is ' +f[each].title()+ '!')

note: that in last line the 'each' will work for 'values' as well, just mention it with dictionary name.
You can also use the keys() method to find out if a particular person was polled. 
means if a person is not present in list we can send a message like,

if 'peter' not in f.keys():
    print('Peter please mention your fav language')

for every in sorted(f):                  # sorting in dictionary
    print('Thanks ' + every.title() + ' for taking the poll')  

output: 
Thanks Bob for taking the poll
Thanks Harry for taking the poll
Thanks Jack for taking the poll
Thanks Stan for taking the poll



# question 1: Introducion
'''
person = {
    'first':'yash',
    'last':'marmat',
    'age':22,
    'city':'delhi'
}

a = 'Full Name: ' + person['first'] + ' ' + person['last']
b = 'Age: ' + str(person['age'])
c = 'city: ' + person['city']

print(a.title())
print(b)
print(c.title())
'''

# question 2: Guessing numbers
'''
fav = {
    'sam':5,
    'peter':10,
    'jack':12,
    'sid':6
}

print("Sam's favourite number : " + str(fav['sam']))
print("Peter's favourite number : " + str(fav['peter']))
print("Jack's favourite number : " + str(fav['jack']))
print("Sid's favourite number : " + str(fav['sid']))
'''

# question 4: Printing keys and values only
'''
glossary = {
    'loops':'for looping',
    'append':'for adding alements',
    'del':'for deleting elements',
    'print':'to print something',
    'dictionary':'contains key-value pairs'
}

for k,v in glossary.items():
    print(k + ': ' + v) 
'''
# question 6: Favourite language poll
'''
fav_lang = {
    'sam':'python',
    'peter':'c#',
    'edward':'ruby',
    'jack':'java',
}

names = ['sam','jack','shon','hanna']

for each in names:
    print('Name: ' + each.title())
                
    if each not in fav_lang.keys():
        print(each.title() + ' take the poll')
    else:
        print(each.title() + ' thanks for participating')'''

# question 7: Introduction of multiple person (using nested dictionary) 
# Method 1
'''
people = []    # an empty list

person = {
    'first':'yash',
    'last':'marmat',
    'age':22,
    'city':'delhi',
}
people.append(person)

person = {
    'first':'edward',
    'last':'kenwey',
    'age':42,
    'city':'hawana',
    }
people.append(person)

person = {
    'first':'conor',
    'last':'kenwey',
    'age':32,
    'city':'boston',
    }
people.append(person)

for each in people:
    a1 = '\nName: ' + each['first'] +' ' + each['last']
    a2 = 'Age: ' + str(each['age'])
    a3 = 'City: ' + each['city']
    print(a1.title(),'\n' + a2,'\n' + a3.title()) '''

# question 7: Method 2(using nested dictionary, also without lists)
'''
people = {
    'person1': {
        'name':'yash',
        'age':22,
        'location':'delhi',
    },
    'person2':{
        'name':'edward',
        'age':46,
        'location':'hawana',
    },
}

for k,v in people.items():
    print(k.title() + ':')
    print('Name: ' + v['name'].title())
    print('Age: ' + str(v['age']))
    print('Location: ' + v['location'].title() + '\n') '''

# note: if you are extracting the information of a dictionary from a list, then you dont need key-value pairs while looping.
# note: if you are extracting the information from a dictionary by using key-value pairs, then you do not need to specify a list.

# question 8: Pet details
'''
pet_info = []

pet1 = {
    'pet type':'dog',
    'owner name':'edward',
}
pet_info.append(pet1)

pet2 = {
    'pet type':'cat',
    'owner name':'sam',
}
pet_info.append(pet2)

pet3 = {
    'pet type':'squirrel',
    'owner name':'jack',
}
pet_info.append(pet3)

for each in pet_info:
    print('Animal Type: ' + each['pet type'].title())
    print("Owner's Name: " + each['owner name'].title() + '\n') '''

# question 9: Favourite places poll
'''
favourite_places = {
    'edward':['INDIA', 'USA', 'CHINA'],
    'sam':['JAPAN', 'DUBAI', 'INDIA'],
    'peter':['UK', 'PARIS', 'JAPAN'],
}

for k,v in favourite_places.items():
    print('\n' + k.title() + ' likes to visit:')
    for each in v:
        print('-> ' + each)
'''
# question 10: Favourite numbers poll
'''
fav = {
    'sam':[5,8,10,15],
    'peter':[10,16,21,24],
    'jack':[1,12,18,22],
    'sid':[6,5,8],
}

print("Sam's favourite numbers are : " + str(fav['sam']))
print("Peter's favourite numbers are : " + str(fav['peter']))
print("Jack's favourite numbers are : " + str(fav['jack']))
print("Sid's favourite numbers are : " + str(fav['sid']))
'''
























