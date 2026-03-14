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

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# formated_string = (f"I am {first_name} {last_name}. I teach {language}") My version
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

#New style formatting