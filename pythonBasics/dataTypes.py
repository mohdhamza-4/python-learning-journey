# PRIMITIVE

# name="Hamza"     # string
# Fan=True         # boolean
# x=10             # Integer
# c=40.5           # Float

# NON-PRIMITIVE

# # List
# # list is a collection of diferent types of data 

# fruits=["apple","mango","grapes"]
# print(fruits)
# print(fruits[0])

# OPERATIONS:-

# nums=[10,20,30,40,50,60,70]

# # SLICING:-
# print(nums[1:5])   #output :-[20, 30, 40, 50]
# print(nums[:4])    #output :-[10, 20, 30, 40]
# print(nums[2:])    #output :-[30, 40, 50, 60, 70]
# print(nums[::2])   #output :-[10, 30, 50, 70]
# print(nums[::-1])  #output :-[70, 60, 50, 40, 30, 20, 10] Reverse list

# UPDATING LIST :- Append,Insert,extend

# # Append:- Element will be added in the last.
# fruits=["Apple","Mango","Orange"]
# fruits.append("Banana")
# print(fruits)

# # Insert:- Element will be added according to given index.
# fruits=["Apple","Mango","Orange"]
# fruits.insert(0,"Grapes")
# print(fruits)

# # Extend:- Multiple element will be added at a time.
# fruits=["Apple","Mango","Orange"]
# fruits.extend(["Grapes","Banana"])
# print(fruits)

# REMOVING ELEMENTS FROM THE LIST :-

# remove:-Removes a particular value.
# fruits = ["apple", "banana", "mango"]
# fruits.remove("banana")
# print(fruits)

# # Pop :- Removes an element using its index and returns that element and If you don't provide an index, pop() removes the last element.
# fruits = ["apple", "banana", "mango"]
# fruits.pop(1)
# print(fruits)

# # Del:-Deletes an element or a portion of the list.

# numbers = [10, 20, 30, 40]
# del numbers[1]
# print(numbers)


# # Clear:- Removes all elements.

# numbers = [10, 20, 30]
# numbers.clear()
# print(numbers)

# =================================================================================================
# # All important List methods
# # ==========================================================
# #   Method	                       Purpose
# # ==========================================================
# #   append()	                     Add one element
# #   extend()	                     Add multiple elements
# #   insert()	                     Insert at an index
# #   remove()	                     Remove a particular value
# #   pop()	                         Remove and return an element
# #   clear()	                       Remove all elements
# #   index()	                       Find the index of a value
# #   count()	                       Count occurrences
# #   sort()	                       Sort the list
# #   reverse()	                     Reverse the list
# #   copy()	                       Create a shallow copy

# Examples:-

# numbers = [10, 20, 30, 20, 40]

# # Find index
# print(numbers.index(20))  

# # Count occurrences
# print(numbers.count(20))

# # Sort ascending
# numbers.sort()

# # Sort descending
# numbers.sort(reverse=True)

# # Reverse
# numbers.reverse()

# # Copy
# new_numbers = numbers.copy()



# Built-in functions used with Lists:-
# These are Python functions, not list methods.

# ==========================================================
#       Function	                  Purpose
# ============================================================
#       len()	                      Number of elements
#       max()	                      Maximum value
#       min()	                      Minimum value
#       sum()	                      Sum of numeric elements
#       sorted()	                  Returns a new sorted list
#       any()	                      True if at least one element is truthy
#       all()	                      True if every element is truthy
#       list()	                    Creates a list
#       enumerate()	                Gives index and value
#       reversed()	                Returns a reverse iterator
'''
practice questions

Your next coding task: Create a list of 5 numbers and write Python code to:
1. Print the total of all numbers.
2. Find the largest number.
3. Find the smallest number.
4. Sort the list in descending order.
5. Remove the last element.
'''

# nums=[40,20,30,50,60]

# # Anwer:1
# print(max(nums[1:4]))

# # Anwer:2
# print(min(nums))

# # Anwer:3
# print(sorted(nums,reverse=True))

# # Anwer:4
# print(nums.pop())

# # Anwer:5
# print(nums)


# # LIST COMPREHENSION:- List comprehension is a shorter way to create a list using existing iterble.

# # List comprehension with for loop :-

# # normal Approach:-
# squares=[]
# for i in range(1,5):
#   squares.append(i**2)
# print(squares)

# # using List comprehension:-
# even=[i**2 for i in range(1,6)]
# print(even)

# # List comprehension with condition:-
# even=[]
# for i in range(100):
#   if i%2==0:
#     even.append(i)
# print(even)

# # using List comprehension:-
# even=[i for i in range(100) if i%2==0]
# print(even)

'''
practice questions:-
1. Create a nested list containing 3 students and their marks.
2. Print the marks of the second student.
3. Create a list of squares from 1 to 10 using list comprehension.
4. Create a list of only odd numbers from 1 to 20 using list comprehension.
'''
# ANSWERS
student=[
  [50,30,40],[90,50,0],[58,11,45]
]
print(student[1])

squares=[i**2 for i in range(1,10)]
print(squares)

odd=[i for i in range(1,20) if i%2!=0]
print(odd)