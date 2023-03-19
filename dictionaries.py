#Dictionaries - Hold key value pairs called items. Like Object in JavaScript

contacts = {'Sathya':'555-0123','Vihaan':'555-0321'}

sathya_phone = contacts['Sathya']
vihaan_phone = contacts['Vihaan']

print('Dial {} to call Sathya.'.format(sathya_phone))
print('Dial {} to call Vihaan.'.format(vihaan_phone))

contacts['Vihaan'] = '555-0000'
vihaan_phone = contacts['Vihaan']
print('Dial {} to call Sathya.'.format(sathya_phone))
print('Dial {} to call Vihaan.'.format(vihaan_phone))

contacts['Lav']='555-0570'
print(contacts)
print(len(contacts))

del contacts['Lav']
print(contacts)
print(len(contacts))

new_contacts = {
    'Sathya':['555-012345','555-00000'],
    'Vihitha': '555-90909'
}

if 'Sathya' in new_contacts.keys():
    print(new_contacts['Sathya'][0])

#this will not execute as Vihaan is not in new_contacts lists
if 'Vihaan' in new_contacts.keys():
    print(new_contacts['Vihaan'][0])

#values can be used to determine values in the list. Return True or False
    print('555-90909' in new_contacts.values())
