age = 21
my_height = 175.0
complicated = 1 + 3j

# base = float(input('Enter base: '))
# height = float(input('Enter height: '))
# #You can't multiply a float and an integer,
# area = 0.5 * base * height
# print(f'The area of the triangle = {area}!')

#Question 5
# side_a = int(input('Enter side a: '))
# side_b = int(input('Enter side b: '))
# side_c = int(input('Enter side c: '))
# total_perimeter = side_a + side_b + side_c
# print(f'the total perimeter of the triangle is {total_perimeter}!!!')

#Question 6
# length = int(input('Enter the length: '))
# width = int(input('Enter the width: '))
# area = length * width
# print(f'area = {area}')
# perimeter = 2 * (length * width)
# print(f'Perimeter is {perimeter}')

#Question 7
# radius = int(input('Enter radius: '))
# pi = 3.142
# area_circle = pi * radius * radius
# print(f'The area is {area_circle}!!!')
# circumference_circle = 2 * pi * radius
# print(f'the circumference is as follows: {circumference_circle}')

#Question 8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
#For the x intercept, y=0 so x=1
#For the y intercept x=0 so y=-2

#Question 9
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# 6  - 2 =  4/8 = 2
# 10 - 2

#Question 10


#Question 11
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# y^2 + 6xy + 9y


#Question 12
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# python = len('python')
# dragon = len('dragon')
# print('python length is not equal to dragon:', python != dragon)


#Question 13
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
# print('on in python and dragon:','on' in 'python' and 'on' in 'dragon')
#Must repeat if theres more than one 

#Question 14
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# print('I hope this course is not full of jargon:', 'jargon' in 'I hope this course is not full of jargon')

# sentence = 'I hope this course is not full of jargon'
# print('I hope this course is not full of jargon:', 'jargon' in sentence)

#Question 15
#There is no 'on' in both dragon and python
# sentence = 'There is no on in both dragon and python'
# print(f'{sentence}:', 'on' not in 'dragon' and 'on' not in 'python')


#Question 16
#Find the length of the text python and convert the value to float and convert it to string
# text_length = len('python') #int
# text_length1 = float(text_length) #float
# text_length2 = str(text_length1)
# print(type(text_length2))

#Another way to do it, this is how people in industry do it: print(type(str(float(len('python')))))
#Read from the inside out

#Question 17
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# check_even = int(input('Enter your number: '))
# result = check_even % 2 == 0
# print(f' the number is even: {result}')

#Question 18
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# sentence = 'the floor division of 7 by 3 is equal to the int converted value of 2.7: '
# floor_division = 7 //3
# int_convert = int(2.7)
# print(f'{sentence} {floor_division == int_convert}')

#Question 19
#Check if type of '10' is equal to type of 10
# sentence = "The type of '10' is equal to type of 10:"
# print(f"{sentence} {type(10) == type('10')}")

#Question 20
#Check if int('9.8') is equal to 10
# first = int(9.8)
# sentence = "Check if int('9.8') is equal to 10:"
# print(f"{sentence} {int(9.8) == 10}")

#Question 21
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours_worked = float(input('Enter how many hours you worked: '))
# rate_per_hour = float(input('Enter your rate per hour: '))
# wage = hours_worked * rate_per_hour
# print(f"Your wages are:  {wage} for this week")

#Question 22
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# current_age = int(input('Enter your age: '))
# life_in_seconds = 60 * 60 * 24 * 365 * current_age
# print(f"{current_age} in seconds = {life_in_seconds}")

#Question 23
#Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

# print(1,1,1**1,1**2,1**3)
# print(2,1,2**1,2**2,2**3)
# print(3,1,3**1,3**2,3**3)
# print(4,1,4**1,4**2,4**3)
# print(5,1,5**1,5**2,5**3)

