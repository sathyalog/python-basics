first = 'I'
second = 'love'
third = 'Python'
# {} works as params and format method is used to pass it
print('{} {} {}.'.format(first,second, third))
# 0 as first param and 1 as second param with min chars allotted of 8 length
print('{0:8} | {1:8}'.format('Fruit','Quantity'))
# < - left alignment
print('{0:8} | {1:<8}'.format('Apple',3))
# ^ - center alignment
print('{0:8} | {1:^8}'.format('Apple',3))
# > - right alignment 
print('{0:8} | {1:>8}'.format('Apple',3))
# .2f is the decimal place
print('{0:8} | {1:<8.2f}'.format('oranges',2.3333))

print('{0:8} | {1:<8.2f}'.format('bananas',10))

# {0} - first param which is love and {1} is second params i.e., Python
print('I {0} {1}. {1} {0}s me'.format('love','Python'))
