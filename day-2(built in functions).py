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


