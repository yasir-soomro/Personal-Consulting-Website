
# Dictionary & Set in Python

# Dictionary (dict) → “I want data WITH meaning (key → value)”
# A dictionary is a mutable mapping of unique keys to values.

# Keys must be unique

# Values can repeat

# Dictionary can be changed after creation

# Set (set) → “I only care about UNIQUE things”

# A dictionary stores data as:
# key : value

# Just like a real dictionary:
# Word : Meaning

user = {
    "id": 101,
    "name": "Afzal",
    "email": "afzal@gmail.com",
    "is_active": True
}

print(user["name"])

student = {
    "name": "yasir afzal",
    "sub" : {
        "eng" : 90,
        "sin" : 59,
        "urd" : 55,
    },
    "email" : "soomro@ss.com",
    "height" : 6.2,
    "lang" : ["sindhi" , "English","Urdu"],
    "isStud" : True,
}

# keys() → Get all keys
print(list(student.keys())) 

# values() → Get all values
print(list(student.values())) 

# get() → Safe way (BEST PRACTICE)
# print(student["name1"])  # error
print(student.get("name1"))  # no error none

# update() → Add / Modify data

student.update({"caste" : "Soomro"})
print(student)

# items() → Get key-value pairs

pairs = (list(student.items())) 

print(pairs[::-1])

# What is a Set?
# A set is a collection that stores:

#  Only unique values
#  No duplicates
#  No index
#  No key–value pair

# Think of a set as a duplicate remover + fast checker

# If a student writes their name twice → teacher counts once

students = {"Ali", "Bilal", "Ali", "Ahmed"}
print(students) 
# {'Ali', 'Bilal', 'Ahmed'}

# Duplicate automatically removed

# Problem:

# Users may register multiple times with same email.

emails = set()

emails.add("a@gmail.com")
emails.add("b@gmail.com")
emails.add("a@gmail.com")

print(emails)

# Permissions / Roles (Backend Use)
permissions = {"read", "write", "delete"}

if "delete" in permissions:
    print("Delete allowed")

# Why set?

# No duplicates

# Super fast checking (in)

#  From Python docs:

# Sets are optimized for membership testing.

# Tags / Categories (Frontend & Backend)
tags = {"python", "backend", "api", "python"}
print(tags)

# Removing Duplicates from List
# User uploads duplicate IDs

ids = [1, 2, 2, 3, 4, 4]
unique_ids = set(ids)
print(unique_ids)


# <-------------------- Set Methods ----------------

# add() → Add item

skills = {"Python", "Django"}
skills.add("FastAPI")

# remove() vs discard()

skills.remove("Django")   # ❌ error if not found
skills.discard("React")   # ✅ no error

# Use discard() when not sure element exists

# pop() → Remove random element

skills.pop() # Order is not fixed

# clear() → Remove everything

skills.clear()

# <------------Set Operations----------->

# Union (|) → Combine

a = {"Python", "JS"}
b = {"JS", "Go"}

print(a | b)

# Intersection (&) → Common items

print(a & b)

# Difference (-) → A but not B

print(a - b)

frontend = {"HTML", "CSS", "JS"}
backend = {"Python", "JS", "SQL"}

print(frontend & backend)

# Dictionary {}
Dict = {}# Curly braces with colon (:) = dictionary  {} means mapping container
# Python assumes key → value


# Tuple ()
Tup = ()
# Parentheses = tuple
# Immutable
# Fixed structure

# 2 List []

List = []
# Square brackets always mean list
# Ordered
# Mutable
# Index-based

# An empty set must be created using set(), not {}.
a = set()
Set = {1,2}


print(type(Dict))
print(type(Tup))
print(type(List))
print(type(Set))


# Has colon :  {"a": 1}  Dictionary
# No colon, only values  {1, 2, 3} Set

# Empty {} Dictionary (default)

# Mutable → can be changed after creation
# Immutable → cannot be changed after creation

u = {}

s = set(u)
s.add(1)
s.add(2)
s.add(3)
print(s)