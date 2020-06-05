#dictionary is like a javascript object

#create dict

person={
    'first_name':'john',
    'last_name':'Doe',
    'age':30
}

print(person['first_name'])

person['phone']='555-555-5555'

print(person.keys())

print(person.items())

person2=person.copy()

person2['city']='boston'

# print(person2)

#remove item
del(person['age'])
person.pop('phone')

print(person.items())

#list of dictionaries

people=[
    {'name':'martha','age':30},
    {'name':'kevin','age':25}
]

print(people[1]['name'])