
# 📝 Python Level 1 – 10 Questions  

# Question 1 – Hello User

# Write a program to print your full name and age in one line using print().

name = "Afzal Soomro"
age = 21
print ("Name:", name, "Age:", age)
print(f"My name is {name} and I am {age} years old.")

# Question 2 – Variables & Data Types

# Create 3 variables:
# name → string

# age → integer
# 
# height → float

# Then print all variables and their data types using type().

name = "Afzal Soomro"
age = 21
height = 6.2
print(name, type(name))
print(age, type(age))
print(height, type(height))


# Question 3 – User Input
# Ask the user to enter their favorite color and print:

color = input("Enter your favorite color")

print("your favorite color is",color)

# Question 4 – Convert Input

# Ask the user to enter a number, then multiply it by 2 and print the result.
# (Hint: convert input to int)

user = int(input("enter a number"))
print(f"here is multiply by {user} * 2 =",user * 2)


# Question 5 – Arithmetic Operators

# Create 2 variables x = 15 and y = 4
# Print:

# Sum  +

# Difference  -

# Product   *

# Division   /

# Floor division  //
  
# Modulus   %

# Exponentiation   **

x = 15
y = 8

print("sum of numbers" , x + y)
print("difference of numbers" , x - y)
print("product of numbers" , x * y)
print("division of numbers" , x / y)
print("floor division of numbers" , x // y)
print("Module of numbers" , x % y)
print("Exponentiation of numbers" , x ** y)


# Question 6 – Assignment Operators

# Start with num = 10
# Then:

# Add 5 using +=

# Multiply by 2 using *=

# Subtract 4 using -=
# Print final value

num = 10 
num += 5
num *= 2
num -= 4
print("final value is :", num)

# Question 7 – Comparison Operators

# Create 2 variables a = 25 and b = 30
# Print whether:

# a equals b

# a not equals b

# a greater than b

# a less than or equal to b

a = 25
b = 30
print( a == b )  # False
print( a != b ) #  True
print( a > b )# False
print( a <= b )  # True


# Question 8 – Logical Operators

# Create variables x = 7, y = 12
# Print results of:

# x > 5 and y < 15

# x < 5 or y > 10

# not(x > 5)

x = 7
y = 12

print(x > 5 and y < 15)
print(x > 5 or y < 10)
print(not (x > 5))

# Question 9 – Identity & Membership 

# Create list1 = [1,2,3] and list2 = list1

# Create list3 = [1,2,3]

# Then print:

# list1 is list2

# list1 is list3

# Check if 2 is in list3

# Check if 5 not in list3

list1  = [1,2,3]
list2 = list1
list3 = [1,2,3]
print(2 in list3)
print (5 not in list3)

print(list3)
print(list2)
print(list1)


# Level 1 MVP – Hints
# Goal: Build a small program that interacts with the user and performs calculations.


# Step 1 – Get User Info

# Ask for name → store as string

# Ask for age → convert to int

# Ask for favorite number → convert to int

# Hint: Use input() and int()


name = input("Enter your Name : ")
age  = int(input("Enter your age : "))
fav_num = int(input("Enter your fav number : "))

# Step 2 – Display Info

# Print the user’s name, age, favorite number

# Hint: Use print() or f-strings for clean formatting
print(f"your Name is :{name}, your age is : {age} and your fav number is : {fav_num }")

# Step 3 – Arithmetic Operations

# Add, subtract, multiply, divide the favorite number with some constants 

# Also do floor division, modulus, and exponentiation

# Hint: Use +, -, *, /, //, %, **

constants = int (input("Enter constants number"))
add = constants + fav_num
sub =constants - fav_num
mul = constants * fav_num
div = constants / fav_num
f_d  =constants // fav_num
mod = constants % fav_num
exp = constants ** fav_num
print(add,sub,mul,div,f_d,mod,exp)

# Project Name

# Daily Expense Analyzer (Basic Version)

# Create a program that:

# Takes user input

# Uses variables & data types

# Performs arithmetic operations

# Shows clear output

# Uses only Level 1 concepts

# Step 1 – User Input

# Ask the user to enter:

# Their name

# Money they have (integer)

# Daily expense (integer)

# 💡 Hint: input() + int()

user_name = input("Enter a Name : ")
day_1 = int(input("Enter Money for day 1 __"))
day_5 = int(input("Enter Money for day 5 __"))
day_10 = int(input("Enter Money for day 10 __"))

# write a program to input 2 numbers & print thier sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

# WAP to input 2 floating point numbers & print their average.


float1 = float(input("Enter first floating point number: "))
float2 = float(input("Enter second floating point number: "))
average = (float1 + float2) / 2
print("The average of", float1, "and", float2, "is:", average)

