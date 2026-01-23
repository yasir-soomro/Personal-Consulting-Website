# LEVEL 1 Part 2 
# Strings & Methods
# Strings in Python are sequences of characters enclosed within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# They are used to represent text data. 

# <------------------Strings--------------------->
# Creating Strings
str1 = 'Hello, World!'          # Single quotes
str2 = "Hello, Python!"         # Double quotes
str3 = '''Hello,
Pythonistas!'''  # Triple quotes
str4 = """Hello,
Python Developers!"""  # Triple quotes
print(str1 , str2, str3, str4)

print(len(str1))  # Length of the string len() is built-in function to get length of string

# String Indexing
# Indexing starts from 0 

str = "Learn Python"
res = str[3] # "r" 
print(res)


# Negative Indexing
res = str[-1] # "n"
print(res)  # "n"
res = str[::-1] # "nohtyP nraeL"
print(res)

# String Slicing
# String slicing lets you cut a string into pieces.
# Why String Slicing Exists

# Strings are immutable (cannot be changed)

# Slicing creates a new string from the original one

# Used heavily in:

# data validation

# parsing input

# backend logic

# formatting responses

# string[start : end : step]

# Meaning:

# start → index where slicing begins (included)

# end → index where slicing stops (excluded)

# step → how many characters to skip


str = "Hello, Pythonistas!"
slice1 = str[0:5]    # "Hello"

slice2 = str[7:]     # "Pythonistas!"
slice3 = str[5:len(str)]     # "Hello"
slice4 = str[::-1]   # "!satsihoP ,olleH"
print(slice1, slice2, slice3, slice4)
# print(str3)

# <---------------------------------------------------String Functions-------------------------------------------------->
# string Functions

# String functions (also called string methods) are built-in functions provided by Python to perform operations on strings, such as modifying, searching, formatting, or analyzing string data.

# These functions do not change the original string because strings are immutable.
# They always return a new string or a value.

# len()

# Returns the total number of characters in a string
string = "Hello, World!"
print(len(string))  # 13

# lower()

# Converts all characters in a string to lowercase

string = "Hello, World!"
print(string.lower())  # "hello, world!"

# upper()

# Converts all characters in a string to uppercase

string = "Hello, World!"
print(string.upper())  # "HELLO, WORLD!"

# strip()

# Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
string = "   Hello, World!   "
print(string.strip())  # "Hello, World!"

# replace()

# Replaces a specified phrase with another specified phrase

string = "Hello, World!"
print(string.replace("World", "Python"))  # "Hello, Python!"

# split()

# Splits a string into a list where each word is a list item

string = "Hello, World!"
print(string.split(","))  # ['Hello', ' World!']

# join()

# Joins a list of strings into one string
string_list = ['Hello', 'World']
print(" ".join(string_list))  # "Hello World"

# find()

# Returns the index of first occurrence (or -1 if not found)
Find = "Hello Afzal Soomro"
print(Find.find("Afzal"))  # 6

# count()

# Counts occurrences of a substring
Count = "banana"
print(Count.count("a"))  # 3

# startswith() / endswith()

# Checks how a string begins or ends

role = "admin_user"
print(role.startswith("admin"))  # True
print(role.endswith("user"))    # True


# <------------------Conditional Statements--------------------->
