#Tuple - A tuple is an immutable list, meaning once it is defined the values contained in the tuple cannot be changed

#Example days of a week cannot be changed

days_of_the_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

for day in days_of_the_week:
    print(day)

#The following will raise an exception, just try uncommenting and execute it

#days_of_the_week[0] = 'New Monday'

print(days_of_the_week)

# delete a tuple using del command - del days_of_the_week

# You can use tuples to assign values
weekend_days = ('Saturday', 'Sunday')
(sat,sun) = weekend_days
print(sat)
print(sun)

contact_info = ['555-0123','abc@xyz.com']

(phone,email) = contact_info
print(phone)
print(email)

contacts = [('Sathya','555-0123'),('Vakacharla','555-1234')]

for (name,phone) in contacts:
    print("{}'s phone number is {}.".format(name, phone))

#Tuples can be converted to lists using list() built in function
#Lists can be converted to tuples using tuple() built-in function
