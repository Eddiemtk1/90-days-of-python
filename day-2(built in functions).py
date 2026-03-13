#python documentation: https://docs.python.org/3/library/functions.html
x = ('hello world')
print(len(x)) #use len() to find out the length of a variable including punctuation and spaces.

print(type(x))# use type() to find out which data type something is

a = str(10) #converts a integer to a string
print(a)
#print(type(a))

f = bool(4 + 4 == 9)
print(f)

#help(str)

#dir(str)

#What are objects, arguments 
print(min(20, 15, 0.17, 0.00002)) #gives the minimum value 
print(max(20, 15, 0.17, 0.00002)) #gives us the maximum value

print(min([20, 15, 0.17, 0.00002])) #takes the list as an argument then gives the minimum value
print(max([20, 15, 0.17, 0.00002])) #takes the list as an argument then gives the maximum value



#Variables
#variables can be stored on multiple lines
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }


# Printing the values stored in the variables
print('First name:', first_name), print('First name length:')
print(len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#variables can be stored on a single line: first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

#ctrl + / to make sections of code into comments
# my_age = input('enter your name: ')
# if my_age == '21':
#     print('You are the one')
# else:
#     print('You are not the one')

name = input('Whats your name: ')
print('your name is: ', name)