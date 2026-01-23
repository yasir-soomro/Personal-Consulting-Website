
# Conditional Statements Exercise

# Conditional Statements

# Conditional statements are used to make decisions in a program by executing different blocks of code based on whether a condition is true or false.

# Conditional statements control what happens and when.

# Conditional statements allow a program to execute specific code blocks based on logical conditions and decision-making rules.

# # Why Conditional Statements Are Important

# Control program flow

# Implement business logic

# Handle validations

# Decide API responses

# Manage permissions & roles

# Backend = conditions everywhere.

# <-----------------if Statement----------------->

# The if statement executes a block of code only when the condition is true.

age = 18 
if age >= 18:
    print("you are eligible to vote.")
# <-----------------if-else Statement----------------->
# The elif statement provides an alternative block of code to execute when the condition is false.
age = 16
if age >= 18:
    print("you are eligible to vote.")
elif age == 17:
    print("you will be eligible to vote next year.")
else:
    print("you are not eligible to vote yet.")

# if-elif-else Statement
# Used when multiple conditions need to be checked in sequence.

marks = 75

if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
else:
    print("Fail")


# Nested if Statement

# A nested if is an if statement inside another if statement, used for complex decision logic.

user = True
admin = True

if user:
    if admin:
        print("Admin access")


# match-case (Python 3.10+)

# match-case is used to compare a value against multiple patterns, similar to switch-case in other languages.

role = "admin"

match role:
    case "admin":
        print("Full access")
    case "user":
        print("Limited access")
    case _:
        print("No access")

# Conditional statements in Python enable dynamic decision-making by evaluating expressions and controlling execution flow, forming the foundation of backend business logic and application behavior.

