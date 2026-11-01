# ============================================================
#                    PYTHON OPERATORS
# ============================================================
#
# Operators are special symbols used to perform operations
# on variables and values.
#
# Types of Operators in Python:
#
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Membership Operators
# 6. Identity Operators
# 7. Bitwise Operators
#
# ============================================================


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
#
# Arithmetic operators are used to perform mathematical
# calculations.
#
# Operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# **  Exponentiation
# %   Modulus (Remainder)
#
# ============================================================

print("\n========== ARITHMETIC OPERATORS ==========")

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)
print("Modulus:", a % b)


# More arithmetic practice

num1 = 15
num2 = 4

print("\nMore Arithmetic Examples:")

print("15 + 4 =", num1 + num2)
print("15 - 4 =", num1 - num2)
print("15 * 4 =", num1 * num2)
print("15 / 4 =", num1 / num2)
print("15 // 4 =", num1 // num2)
print("15 % 4 =", num1 % num2)
print("2 ** 4 =", 2 ** 4)


# Practical Example: Calculate total price

price = 250
quantity = 3

total_price = price * quantity

print("\nTotal Price:", total_price)


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================
#
# Assignment operators are used to assign values to variables
# and update their existing values.
#
# Operators:
# =    Assign
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# //=  Floor divide and assign
# **=  Power and assign
# %=   Modulus and assign
#
# ============================================================

print("\n========== ASSIGNMENT OPERATORS ==========")

# Simple assignment (=)

x = 10
print("Initial value:", x)


# Addition assignment (+=)

x = 10
x += 5
print("After += 5:", x)


# Subtraction assignment (-=)

x = 10
x -= 3
print("After -= 3:", x)


# Multiplication assignment (*=)

x = 10
x *= 2
print("After *= 2:", x)


# Division assignment (/=)

x = 10
x /= 2
print("After /= 2:", x)


# Floor division assignment (//=)

x = 10
x //= 3
print("After //= 3:", x)


# Exponentiation assignment (**=)

x = 2
x **= 3
print("After **= 3:", x)


# Modulus assignment (%=)

x = 10
x %= 3
print("After %= 3:", x)


# Practical Example: Update shopping balance

balance = 1000

balance += 500
print("\nAfter adding money:", balance)

balance -= 200
print("After spending money:", balance)


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================
#
# Comparison operators compare two values.
# They always return either True or False.
#
# Operators:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
#
# ============================================================

print("\n========== COMPARISON OPERATORS ==========")

a = 15
b = 10

print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)


# More comparison examples

age = 20
marks = 75

print("\nMore Comparison Examples:")

print("Age is 18:", age == 18)
print("Age is not 18:", age != 18)
print("Age is greater than 18:", age > 18)
print("Marks are above 40:", marks >= 40)
print("Marks are below 100:", marks <= 100)


# Practical Example: Check pass or fail

student_marks = 65

if student_marks >= 40:
    print("\nStudent is Pass")
else:
    print("\nStudent is Fail")


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================
#
# Logical operators are used to combine multiple conditions.
#
# Operators:
# and  Returns True if both conditions are True.
# or   Returns True if at least one condition is True.
# not  Reverses the result.
#
# ============================================================

print("\n========== LOGICAL OPERATORS ==========")

age = 20
has_id = True

# AND operator

print("AND:", age >= 18 and has_id)


# OR operator

age = 17
has_permission = True

print("OR:", age >= 18 or has_permission)


# NOT operator

is_raining = False

print("NOT:", not is_raining)


# More logical examples

a = 10
b = 20
c = 30

print("\nMore Logical Examples:")

print(a < b and b < c)
print(a > b or b < c)
print(not (a > b))


# Practical Example: Login system

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("\nLogin Successful")
else:
    print("\nInvalid Username or Password")


# ============================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================
#
# Membership operators check whether an element exists
# inside a sequence or collection.
#
# Operators:
# in      Checks whether an element is present.
# not in  Checks whether an element is absent.
#
# ============================================================

print("\n========== MEMBERSHIP OPERATORS ==========")

fruits = ["Apple", "Banana", "Mango", "Orange"]

# IN operator

print("Apple in fruits:", "Apple" in fruits)
print("Grapes in fruits:", "Grapes" in fruits)


# NOT IN operator

print("Grapes not in fruits:", "Grapes" not in fruits)
print("Mango not in fruits:", "Mango" not in fruits)


# Membership with strings

language = "Python Programming"

print("\nMore Membership Examples:")

print("Python" in language)
print("Java" in language)
print("Java" not in language)
print("python" in language)


# Practical Example: Check student name

students = ["Ali", "Hamza", "Ahmed", "Sara"]

student_name = "Hamza"

if student_name in students:
    print("\nStudent Found")
else:
    print("\nStudent Not Found")


# ============================================================
# 6. IDENTITY OPERATORS
# ============================================================
#
# Identity operators check whether two variables refer
# to the same object in memory.
#
# Operators:
# is      Returns True if both refer to the same object.
# is not  Returns True if they refer to different objects.
#
# Important:
# == checks values.
# is checks object identity.
#
# ============================================================

print("\n========== IDENTITY OPERATORS ==========")

# Example 1: Same object

list1 = [10, 20, 30]
list2 = list1

print("list1 is list2:", list1 is list2)


# Example 2: Different objects with same values

list3 = [10, 20, 30]
list4 = [10, 20, 30]

print("list3 == list4:", list3 == list4)
print("list3 is list4:", list3 is list4)


# Example 3: IS NOT operator

print("list3 is not list4:", list3 is not list4)


# Example 4: Changing a shared list

numbers1 = [1, 2, 3]
numbers2 = numbers1

numbers2.append(4)

print("\nNumbers 1:", numbers1)
print("Numbers 2:", numbers2)

print("Same object:", numbers1 is numbers2)


# Example 5: Comparing with None

value = None

if value is None:
    print("Value is None")
else:
    print("Value is not None")


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================
#
# Bitwise operators perform operations on binary numbers.
#
# Operators:
# &   Bitwise AND
# |   Bitwise OR
# ^   Bitwise XOR
# ~   Bitwise NOT
# <<  Left Shift
# >>  Right Shift
#
# ============================================================

print("\n========== BITWISE OPERATORS ==========")

a = 5
b = 3

# Binary representation:
# 5 = 0101
# 3 = 0011


# Bitwise AND (&)

print("Bitwise AND:", a & b)


# Bitwise OR (|)

print("Bitwise OR:", a | b)


# Bitwise XOR (^)

print("Bitwise XOR:", a ^ b)


# Bitwise NOT (~)

print("Bitwise NOT:", ~a)


# Left Shift (<<)

print("Left Shift:", a << 1)


# Right Shift (>>)

print("Right Shift:", a >> 1)


# Bitwise Assignment Operators

x = 5
x &= 3
print("AND Assignment:", x)

x = 5
x |= 3
print("OR Assignment:", x)

x = 5
x ^= 3
print("XOR Assignment:", x)

x = 5
x <<= 1
print("Left Shift Assignment:", x)

x = 10
x >>= 1
print("Right Shift Assignment:", x)


# Practical Example: Check Even or Odd using Bitwise AND

number = 15

if number & 1:
    print("\nNumber is Odd")
else:
    print("\nNumber is Even")













