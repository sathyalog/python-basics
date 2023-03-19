def say_hi():
    print('Hello Hi')

def say_hello(name):
    print('Hello {}!'.format(name))
#default param example
def say_hello_everyone(name='everyone'):
    print('Hello {}!'.format(name))

def say_fullname(fname, lname):
    print('Hello {} {}!'.format(fname, lname))

def say_fullname_citizen(fname, lname, citizen='india'):
    print('I am {} {}!. I am from {}'.format(fname, lname, citizen))

say_hi()
say_hello('Sathya')
say_hello_everyone()
say_hello_everyone('Sathya')
say_fullname('Sathya','Vakacharla')
say_fullname_citizen('Sathya','Vakacharla')
say_fullname_citizen('Sathya','Vakacharla', 'UK')

"""By convention first statement of a function can be a documentation string.
To create a documentation string, simply add the keywords to explain
function using triple quote and get this documentation using built in help function like help(function_name)"""

def hello_python():
    """ This is a welcome python function."""
    print('Hello! Welcome to Python world')

help(hello_python)

#using return keyword
def get_name():
    name = input('what is your name? ')
    return name

def say_name(name):
    print('your name is {}!'.format(name))

def get_and_say_name():
    """ Get and say name"""
    name = get_name()
    say_name(name)

get_and_say_name()
