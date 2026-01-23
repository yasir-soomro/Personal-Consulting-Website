

# List & Tuple in Python

# A list is a mutable, ordered collection of elements used to store multiple values in a single variable.


# Basic Creation

numbers = [1, 2, 3, 4]
names = ["Ali", "Sara", "Ahmed"]
# Mixed Data Types
user = ["Ali", 25, True, 5.9]

tasks = []

# Using list() constructor

chars = list("hello")   # ['h','e','l','l','o']

marks = [85, 90, 78, 92, 88]
marks[0] = 47
print("Marks List:",marks)

#  Slicing (Extracting Sub-Data)
nums = [1, 2, 3, 4, 5, 6]

print(nums[1:4])    # [2,3,4]
print(nums[:3])     # [1,2,3]
print(nums[3:])     # [4,5,6]
print(nums[::-1])   # reverse

nums.append(7)
print(nums)

list = [2,1,4,3,6,5]
list.sort()

print(list)

list.sort(reverse=True)
print(list)


# Indexing (Accessing Data)

# Index starts from 0

# Negative index starts from -1

data = [10, 20 ,30 ,40]

print(data[1:3]) # 20 , 30
print(data[:3]) # 10
print(data[1:-3]) # none
print(data[1::-3]) # 40 30 20 

nums = [0,1,2,3,4,5,6,7,8,9]



print(nums[::2]) # even
print(nums[1::2]) # odd
print(nums[::-1]) # reverse
print(nums[2::3]) # 


# List Methods (FULL & PRACTICAL)
# append() – Add one item

tasks.append("Laptop")
print(tasks)

# extend() – Add multiple items

tasks.extend(["Mouse" , "Keyboard"])
print(tasks)

# insert() – Add at index

tasks.insert(2 , "Monitor")

print(tasks)

# remove() – Remove by value

tasks.remove("Mouse")
print(tasks)

# pop() – Remove by index
tasks.pop()
print(tasks)

# clear() – Remove all
tasks.clear()
print(tasks)

# index() – Find position
items = ["pen", "book", "eraser"]
print(items.index("book"))  # 1

# count() – Count occurrences

votes = ["yes","no","yes"]
votes.count("yes")  # 2

# sort() – Sort list

scores = [90, 70, 85]
scores.sort()

list.clear()

# reverse() – Reverse list
scores.reverse()

#<------------ End of List data --------------->

# Tuple in Python

# A tuple is an ordered, immutable collection of elements used to store fixed data.

# in tuple we use parentheses ()

# Rule:

# Changing data → List
# Fixed data → Tuple
# Creating Tuples (ALL ways)
t = (1, 2, 3)
t = (5)      # int, not tuple
t = (5,)     # correct this is a tuple



list_data = [1,2,3,4,5]

tup = tuple(list_data)

print(type(tup),tup)

x = list(tup)
print(x)