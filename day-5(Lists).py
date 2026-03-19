#Theres 4 collection data types in python: list, dictionary, tuple, set
# List - A collection which is ordered and changeable, allows duplicate members
# Tuple - A collection which is ordered and unchangeable, allows duplicate members
# Set - A collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary - A collection which is unordered, changeable(modifiable) and indexed. No duplicate members.


##How to make a list
# list function: 1st = list()

# square brackets 1st = []


##Accessing list items using positive indexing
#We can access items in a list using their index, it starts at 0.

#fruits = ['banana', 'orange', 'mango', 'lemon']
#first_fruit = fruits[0]
#print(first_fruit)


##Accessing List Items Using Negative Indexing
#-1 is the last item, -2 is second to last item, etc

#last_fruit = fruits[-1]
#print(last_fruit)


##Unpacking list items
# lst = ['item1','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest_items = lst
# print(rest_items) #['item4', 'item5']
# print(second_item) #item2

##Slicing Items from a List
#positive indexing we can specific a range of positive indexes by stating the start and end (length - 1) overall layout is (0: 7)
fruits = ['banana', 'orange', 'mango', 'lemon']
# orange_and_mango = fruits[1:3]
# print(orange_and_mango)
# banana_and_mango = fruits[::2]# take every second item
# print(banana_and_mango) # ['banana', 'mango']

#negative indexing 
all_fruits = fruits[-4:]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]


##modifying a list