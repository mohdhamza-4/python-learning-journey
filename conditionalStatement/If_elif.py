# Student Marks System
marks=int(input("Enter the number"))
if marks>=35 and marks<=100:
  print("pass")
elif marks<35 and marks>=0:
  print("fail")
else:
  print("invalid")

# Age Category Program.
# Rules:
# Age 0 se 12 → Child
# Age 13 se 19 → Teenager
# Age 20 se 59 → Adult
# Age 60 ya above → Senior Citizen
# Age negative ho → Invalid Age

age=int(input("Enter Your Age : "))
if age>=0 and age<=12:
  print("child")
elif age>=13 and age<=19:
  print("Teenager")
elif age>=20 and age<=59:
  print("Adult")
elif age>=60:
  print("Senior Citizen")
else:
  print("Invaid age")


# Problem: Find the largest of three numbers
a=int(input("Enter the first number"))
b=int(input("enter the second number :"))
c=int(input("enter the third number"))

if a>b and a>c:
  print(a," is greater")
elif b>a and b>c:
  print(b,"is greater")
else:
  print(c," is greater")