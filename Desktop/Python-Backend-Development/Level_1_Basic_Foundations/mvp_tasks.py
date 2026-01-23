
# # MVP 1: User Profile Generator

# # Concepts used:
# # Variables, input/output, type conversion, strings

# user_name = input("Enter your name :")
# user_age = int(input("Enter your age :"))
# user_height = input("Enter your Height :")

# print ("------USER PROFILE-----")
# profile = f"Name: {user_name} \n Age: {user_age} \n Height: {user_height}"
# print(profile)

# # Simple Calculator v1

# # Concepts used:
# # Arithmetic operators, input, type casting
# # Simple Calculator v1

# num_1 = float(input("Enter First Number: "))
# operation = input("Enter Operation (+, -, *, /): ")
# num_2 = float(input("Enter Second Number: "))

# if operation == "+":
#     print("Addition:", num_1 + num_2)

# elif operation == "-":
#     print("Subtraction:", num_1 - num_2)

# elif operation == "*":
#     print("Multiplication:", num_1 * num_2)

# elif operation == "/":
#     if num_2 == 0:
#         print("❌ Division by zero is not allowed")
#     else:
#         print("Division:", num_1 / num_2)

# else:
#     print("❌ Invalid operation")


# # Username Validator
# # Strings, string methods, membership operator

# if user_name.strip() and len(user_name) >= 5:
#     print("Valid")
# else:
#     print("Invalid")


# String Analyzer Tool
# String indexing, slicing, methods

# Str  = "yasir afzal soomro"

# print(Str[0])
# print(Str[-1:])
# print(Str[::-1])
# print(len(Str))
# print(Str.upper())

# # USER ACCESS DECISION SYSTEM
# login_input = input("Are you logged in? (yes/no): ").strip().lower()
# age = int(input("Enter your age: "))
# role = input("Enter your role (Admin/User/Guest): ").strip().lower()

# if login_input not in ["yes", "y"]:
#     print("Access Denied. Please log in first.")
# else:
#     # Only reach here if logged in
#     if age < 18:
#         print("Access Denied. You must be 18 or older.")
#     else:
#         # Logged in + adult
#         if role == "admin":
#             print("Full Admin Access Granted")
#         elif role == "user":
#             print("Standard User Access Granted")
#         elif role == "guest":
#             print("Read-Only Guest Access Granted")
#         else:
#             print("Invalid role. Access Denied.")




# User Registration & Access System

# FEATURES
# User Registration
# Input Validation Rules
# Access Decision Logic

# 1 User Registration

Full_Name = input("Enter Your Full Name : ")
User_Name = input("Enter User Name :")
User_Age = int(input("Enter Your Age : ")) 
User_Role = input("Enter your role (Admin/User/Guest): ").strip().lower()
Login_Input = input("Are you logged in? (yes/no): ").strip().lower()

# 2 Input Validation Rules

# ------ USER SUMMARY ------
if  Full_Name == "" :
    print("Name Must not be empty")
elif  Full_Name == int :
    print("Name Must not be numeric")
else :
    print("Invalid Name")
    if not User_Name == "" and not len(User_Name) >=5 :
        print("Must be at least 5 characters")
    elif not User_Name.strip():
        print("Must not contain spaces")
        if User_Age <= 18 :
            print("Access Denied. You must be 18 or older.")
            # Logged in + adult
        if User_Role == "admin":
            print("Full Admin Access Granted")
        elif User_Role == "user":
            print("Standard User Access Granted")
        elif User_Role == "guest":
            print("Read-Only Guest Access Granted")
        else:
            print("Invalid role. Access Denied.")
            if Login_Input not in ["yes", "y"]:
                print("Access Denied. Please log in first.")
            
#    -----------------------------

    
# User Registration & Access System (Level-1 version)
# Only basic Python features allowed

# 1. Get all inputs
full_name = input("Enter Your Full Name : ")
username = input("Enter User Name : ")
age_str = input("Enter Your Age : ")
role = input("Enter your role (Admin/User/Guest) : ").lower()
login_answer = input("Are you logged in? (yes/no) : ").lower()

# 2. Try to convert age to number
age_ok = True
age = 0
if age_str.isdigit():
    age = int(age_str)
else:
    age_ok = False

# 3. Prepare cleaned values
name_stripped = full_name.strip()
username_stripped = username.strip()
role_clean = role.strip()

# 4. Start checking everything with nested ifs
print("--- Registration Check ---")

if name_stripped == "":
    print("Error: Full Name cannot be empty")
else:
    if username_stripped == "":
        print("Error: Username cannot be empty")
    else:
        if len(username_stripped) < 5:
            print("Error: Username must be at least 5 characters")
        else:
            if " " in username_stripped:
                print("Error: Username cannot contain spaces")
            else:
                if age_ok == False:
                    print("Error: Age must be a valid number")
                else:
                    if age < 18:
                        print("Error: You must be 18 or older")
                    else:
                        if role_clean != "admin" and role_clean != "user" and role_clean != "guest":
                            print("Error: Invalid role (only Admin, User, Guest allowed)")
                        else:
                            if login_answer != "yes" and login_answer != "y":
                                print("Error: You must login first (answer yes or y)")
                            else:
                                # All checks passed → show welcome + access
                                print("")
                                print("Registration SUCCESSFUL!")
                                print("Welcome,", full_name)
                                print("Username:", username)
                                print("Age:", age)
                                print("Role:", role_clean.capitalize())
                                
                                if role_clean == "admin":
                                    print("→ Full Admin Access Granted")
                                elif role_clean == "user":
                                    print("→ Standard User Access Granted")
                                else:  # must be guest
                                    print("→ Read-Only Guest Access Granted")