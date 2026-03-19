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
# fruits = ['banana', 'orange', 'mango', 'lemon']
# # orange_and_mango = fruits[1:3]
# # print(orange_and_mango)
# # banana_and_mango = fruits[::2]# take every second item
# # print(banana_and_mango) # ['banana', 'mango']

# #negative indexing 
# all_fruits = fruits[-4:]
# orange_mango_lemon = fruits[-3:]
# reverse_fruits = fruits[::-1]


##modifying a list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits[0] = 'avocado'
# print(fruits) #['avocado', 'orange', 'mango', 'lemon']
# last_index = len(fruits) - 1
# fruits[last_index] = 'lime'
# print(fruits) #['avocado', 'orange', 'mango', 'lime']


##Checking Items in a List
# does_exist = 'banana' in fruits
# print(does_exist)  # True


##Adding Items to a List
# fruits.append('apple')
# print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple']


##Inserting Items into a List
# fruits.insert(2, 'apple')
# print(fruits) #['banana', 'orange', 'apple', 'mango', 'lemon']


##Removing Items from a List
# fruits.remove('orange')
# print(fruits) #['banana', 'apple', 'mango', 'lemon']


##Removing Items Using Pop
#The pop() method removes the specified index, or the last item if index isn't specified
# fruits.pop()
# print(fruits) #['banana', 'apple', 'mango']
# fruits.pop(1)
# print(fruits)#['banana', 'mango']


##Removing Items Using Del
#The del keyword removes the specified index and can also be used to delete items within index ranges or delete the list completely
# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits) #['orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits [1:3]
# print(fruits) #['orange', 'kiwi', 'lime']


##Clearing List Items
# The clear() method empties lists
# fruits.clear()
# print(fruits) #[]


##Copying a List
#use the copy() method
# fruits_2 = fruits.copy()
# print(fruits_2) #['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']


##Joining Lists
#lists can be joined using + or extend()
# list_1 = ['gravity','is','a','harness']
# list_2 = ['what','is','that','melody']
# list_3 = ['      ']

# final_list = list_1 + list_2
# print(final_list)#['gravity', 'is', 'a', 'harness', 'what', 'is', 'that', 'melody']

# list_1.extend(list_2)
# print(list_1) #['gravity', 'is', 'a', 'harness', 'what', 'is', 'that', 'melody']

# list_1.extend(list_3)
# list_1.extend(list_2)
# print(list_1)
#['gravity', 'is', 'a', 'harness', 'what', 'is', 'that', 'melody', '      ', 'what', 'is', 'that', 'melody']


##Counting Items in a List
#use count() method to return the number of times an item appears in a list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('banana'))


##Finding Index of an Item
#index() method returns the index of the first occurence of an item:
# print(fruits.index('mango')) #2


##Reversing a List
#reverse(), reverse the order of a list
# fruits.reverse()
# print(fruits)#['lemon', 'mango', 'orange', 'banana']


##Sorting List Items
#sort() method reorders the list in ascending order. It modifies the original list . if an argument of sort() = true, it will arrange the list in descending order
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.sort()
# print(fruits)#['banana', 'lemon', 'mango', 'orange']

# fruits.sort(reverse=True)
# print(fruits)#['orange', 'mango', 'lemon', 'banana']


#sorted()returns the ordered list without changing the original list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits)) #['banana', 'lemon', 'mango', 'orange']

fruits = sorted(fruits, reverse=True)
print(fruits) #['orange', 'mango', 'lemon', 'banana']

