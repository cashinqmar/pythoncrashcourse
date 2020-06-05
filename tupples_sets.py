#tuples dont change value and are not like lists
#a set is a collection which is unordered and unindexed

fruits=('apples','oranges','grapes')
fruits2=('apples',)

print(fruits)
print(fruits2)

del fruits2

print(len(fruits))

fruits_set={'Apples','Oranges','Mango'}

print('Apples' in fruits_set)

fruits_set.add('grape')

fruits_set.add('Apples')

print(fruits_set)

# fruits_set.clear()

# del(fruits_set)
# print(fruits_set)
