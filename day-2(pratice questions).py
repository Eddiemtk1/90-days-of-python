#Day 2: 30 Days of python programming

# first_name = 'Safron'
# last_name = 'Paula'
# full_name = first_name + ' ' + last_name
# country = 'United Kingdom'
# city = 'London'
# age = 21
# year = 2026
# is_married = False
# is_true = 'yes'
# is_light_on = False

# first_name1, last_name1, country1, city1, age1 = 'Faris', 'Myung', 'England', 'bradford', '22'

# print(type(first_name))
# print(type(last_name))
# print(type(full_name))
# print(type(age))
# print(type(is_married))

# print(len(first_name))
# print(len(last_name))

num_one = 5
num_two = 4
num_totals = num_one + num_two
print(num_totals)
num_diff = num_one - num_two
print(num_diff)
num_product = num_one * num_two
print(num_diff)
num_div = num_one / num_two
print(f'The division of {num_one} and {num_two} = {num_div}!')
num_remain = num_one % num_two
print(f'The modulous of {num_one} and {num_two} is {num_remain}!')
num_exp = num_one ** num_two
print(f'The expential of {num_one} and {num_two} = {num_exp}!!!')
num_floor_division = num_one // num_two
print(f'the floor division of {num_one} and {num_two} is {num_floor_division}')

radius_of_circle = 30
pi = 3.142
area_of_circle = pi * radius_of_circle ** 2
print(area_of_circle)
circumference_of_circle = pi * radius_of_circle * 2
print(f'circumference of the circle is {circumference_of_circle} ')

new_radius = input('enter radius: ')
int(new_radius)
new_area = pi * int(new_radius) ** 2
print(f'The new area of the circle is {new_area} ')

new_first_name = input('Enter first name: ')
new_last_name = input('Enter last name: ')
new_coutry = input('Enter your country: ')
new_age = input('Enter new age: ')
int(new_age)
new_person = new_first_name, new_last_name, new_coutry, new_age
print(f'The new persons information is {new_person}')  #The new persons information is ('King', 'Charles', 'England', '99')