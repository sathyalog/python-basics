sum = 1 +2
difference = 100 - 1
product = 3 * 4
quotient = 8 / 2
power = 2 ** 4 # 2*2*2*2 (exponentiation)
remainder = 3 % 2 #module operator to get the reminder

print('Sum: {}'.format(sum))
print('Difference: {}'.format(difference))
print('Product: {}'.format(product))
print('Quotient: {}'.format(quotient))
print('Power: {}'.format(power))
print('Remainder: {}'.format(remainder))

#Handling integers with int method as python throws error when we pass string concatenation with numbers.
quantity_string = '3'
total = int(quantity_string) + 2
print(total)

#Handling float with float method
float_total = float(quantity_string) + 2
print(float_total)
