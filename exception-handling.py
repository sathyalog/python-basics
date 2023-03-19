# Exception handling

animals = ['cat','dog','cow']

try:
    goat_index = animals.index('goat')
except:
    goat_index = 'No goat found'

print(goat_index)
