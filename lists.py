#Lists are arrays in javascript

animals = ['man','cat','dog']

print(animals[0])
print(animals[1])
print(animals[2])
print(len(animals))
# reverse order
print('Printing in reverse order using negatives')
print(animals[-1])
print(animals[-2])
print(animals[-3])
#add an item to end of list using append
animals.append('lion')
print(animals[-1])
print(len(animals))
# add multiple items in list using extend
more_animals = ['pig','cow','duck']
animals.extend(more_animals)
print(animals)
#add an item in any point(position) of list using insert
animals.insert(3,'horse')
print(animals)
#concat can also be used to join 2 lists
new_list = ['monkey','tiger']
all_animals = animals + new_list
print(all_animals)

