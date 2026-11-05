# check whether a person is eligible to vote.
# Conditions:
# - Age must be 18 or above.
# - The person must have voter registration.

age=int(input("Eneter your age : "))
registered=True
if age>=18:
  if registered==True:
    print("you are eligible to vote")
  else:
    print("Registration reuired")
else:
  print("Not eligible")


# Student Result System
# Write a program that takes marks from the user.
# Rules:
# 1. If marks are 0–100, continue.
# 2. If marks are 40 or above, print Pass.
# 3. Otherwise, print Fail.
# 4. If marks are below 0 or above 100, print Invalid Marks.

marks=int(input("enter your marks"))
if marks>=0 and marks<=100:
  if marks>=40:
    print("pass")
  else:
    print("fail")
else:
  print("invalid number : ")


# Online banking login.
# Rules :
# user account exist ??
# If yes,password correct?
# if correct,print login successfully
account =True
password=True
if account==True:
  if password==True:
    print("Login Successfully")
  else:
    print("Incorrect Password")
else:
  print("account not found")



# Movie ticket booking program :
# Rules :
# User ki age 18 ya above honi chahiye.
# Agar age eligible hai, toh check karo ki ticket available hai ya nahi.
# Agar ticket available hai → Ticket Booked
# Agar ticket available nahi hai → Tickets Sold Out
# Agar age 18 se kam hai → Not Eligible


age=int(input("enter your age : "))
ticketAvailable=False
if age>=18:
  if ticketAvailable ==True:
    print("Ticket Booked")
  else:
    print("Tickets sold Out")
else:
  print("Not Eligible")