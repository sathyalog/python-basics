#soring
animals = ['cow','cat','dog','horse','duck','bear']

animals.sort()

print(animals)

#range is built in function used to generate

for number in range(3):
    print(number)

for number in range(1,4):
    print(number)

#range can also accept step parameter i.e., it prints [1,3,5] if you provide range(1,6,2)

for number in range(1,6,2):
    print(number)
    
#use this step and range for animals list

newanimals = ['cow','cat','dog','horse','duck','bear']
for number in range(0,len(newanimals),2):
    print(newanimals[number])
