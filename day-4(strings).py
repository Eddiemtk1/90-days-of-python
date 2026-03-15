#Multiline strings can be created with 3 ''' or 2 """"
# sentence = '''My name is Edward
#             I am the goat 
#             NICE TO meet you'''
# print(sentence)

#Escape sequences in strings
#\n for new line
#\t is 4 character spaces
#\\ is back slash
#\' is single quote '
#\" is double quote ""

# print('Day 1\t5\t5')
# print('This is a backslash  symbol (\\)')
# print("In every programming language it starts with \'Hello, World!\'") # to write a double quote inside a single quote

#Old style string Formatting
# %s - string
# %d - integer
# %f - floating point numbers
# %.number of digitsf - Floating point numbers with fixed precision

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# # formated_string = (f"I am {first_name} {last_name}. I teach {language}") My version
# print(formated_string)

# Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

#New style formatting
# formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# print(formated_string)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print(f'{a} + {b} = {a+b}')
# print('{} / {} = {:.2f}'.format(a, b, a / b))

#String interpolation / f-string
# print(f'{a} + {b} = {a+b}') The new way

#unpacking characters
# language = 'pYthon'
# a,b,c,d,e,f = language
# print(a) #p
# print(b) #Y
# print(c) #t
# print(d) #h
# print(e) #o
# print(f) #n

#Accessing Characters in Strings by Index
#Counting starts from zero.
# language = 'python'
# # first_letter = language[0]
# # print(first_letter)
# # last_index=len(language) - 1
# # print(language[last_index])

# #if we want to start from the right we can use negative indexing. -1
# last_letter = language[-1]
# print(last_letter) #n
# second_last_letter = language[-2]
# print(second_last_letter)

#slicing python string
# language = 'python'
# first_three_letters = language[0:3]
# print(first_three_letters) #pyt
# last_3_letters = language[3:6]
# print(last_3_letters)#hon

#Another way is:
# last_three = language[-3:]
# print(last_three)
# last_3 = language[3:]
# print(last_3)


#Reversing a string
# welcome = 'helcome to Brum!'
# print(welcome[::-1]) #!murB ot emocleW

# print(welcome[::2]) #Skipps every second letter

#Skipping Characters While Slicing
# missing = welcome[0:6:2]
# print(missing) # hlo
#[0:6] basically states we are focusing on index 0 - 6 so 'helcome' then the [:2] means we focus on every second letter
#so we are left with h, l, o.

#string methods
#capitalize()
# challenge = 'thirty days of coding python'
# # # print(challenge.capitalize())

# # #count() returns the number of non-overlapping times a substring appears in a string, starting and ending indexes are optional
# # print(challenge.count('o')) #3
# # print(challenge.count('o',2,6)) #0 'how many 'o' between index 2 - 6

# #endswitch() checks if a string ends in a specific ending
# print(challenge.endswith('on'))#true
# print(challenge.endswith('days'))#false

#expandtabs() replaces tab character with spaces, default tab size is 8 but actually 4 characters.
# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())
# print(challenge.expandtabs(10))#thirty    days      of        python, Space 4,6,8

#find()returns the index of the first occurence of a substring, if not found returns -1
# print(challenge.find('t')) #0
# print(challenge.find('tz')) #-1

# #rfind() find the index of the last occurence of a substring, if not found returns -1
# print(challenge.rfind('t'))#17

#format() formats string into a nicer output
# formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# print(formated_string)

#index()returns the lowest index of a substring, additional arguments indicate starting and ending index. 
#if the substring isn't found it returns a valueError
challenge = 'thirty days of python'
sub_string = 'da'
# print(challenge.index(sub_string)) #7
# print(challenge.index(sub_string,9))#Error

#rindex() returns the highest index of a substring, additional arguments indicate starting and ending index.
print(challenge.rindex(sub_string)) #7
# print(challenge.rindex(sub_string, 9))
print(challenge.rindex('t',5))#19 #finds the highest index of 't' after index 5.