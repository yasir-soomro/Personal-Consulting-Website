
# Topics for cover in level_1_basic_foundations/part_1.py:
# - Variables and Data Types
# - Basic Input/Output
# - Operators



# print() is a function
# Text must be inside quotes " "
# Python runs line by line

# Your First Python Program
print("hello world")

# <-------------variables------------>

# Variables (Very Important)
# Variables store data.

name = "afzal soomro"
age  = 21
height = 6.2

height = "6.2"
print(name,age,height)


# <---------------------Data Types---------------------->
# Data Types (Level 1)
# Type	Example
# int	10, -5
# float	3.14, 5.6
# str	"Python"
# bool	True, False

print(type(name))   # str
print(type(age))    # int       
print(type(height)) # str

# <--------------------Basic Input/Output------------------>


# Taking Input from Username = input("Enter your name: ")
name = input("Enter your name: ")

# ⚠️ input() always returns a string

# Convert: input to int

age = int(input("Enter age: "))
print("your name is :", name, "Your age is:", age)


# <-------------------Basic Operators-------------------------->
#  1. Arithmetic Operators
#  2. Assignment Operators  
#  3. Comparison Operators
#  4. Logical Operators
#  5. Identity Operators
#  6. Membership Operators
#  7. Bitwise Operators
# 1. Arithmetic Operators
#  Used to perform mathematical operations like addition, subtraction, multiplication, etc.

# +   -   *   /   //   %   **

a = 10
b = 3
print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7  
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.3333
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000

# 2. Assignment Operators

# Used to assign values to variables.   
# =   +=   -=   *=   /=   //=   %=   **=
x = 5
x += 3  # x = x + 3  = 8
print("Value of x after += 3:", x)
x *= 2  # x = x * 2  = 16
print("Value of x after *= 2:", x)
x -= 4  # x = x - 4  = 12
print("Value of x after -= 4:", x)
x /= 3  # x = x / 3  = 4.0
print("Value of x after /= 3:", x)
x //= 2 # x = x // 2 = 2.0
print("Value of x after //= 2:", x)
x %= 2  # x = x % 2  = 0.0
print("Value of x after %= 2:", x)
x **= 3 # x = x ** 3 = 0.0
print("Value of x after **= 3:", x)


# 3. Comparison Operators
# Used to compare two values.
# ==   !=   >   <   >=   <=
p = 10
q = 20
print("p == q:", p == q)   # False
print("p != q:", p != q)   # True
print("p > q:", p > q)     # False
print("p < q:", p < q)     # True
print("p >= q:", p >= q)   # False
print("p <= q:", p <= q)   # True

# 4. Logical Operators
# Used to combine conditional statements.   
# and   or   not
x = 5
y = 10
print("x > 3 and y < 15:", x > 3 and y < 15) # True
print("x > 3 or y > 15:", x > 3 or y > 15)   # True
print("not(x > 3):", not(x > 3))               # False  

# 5. Identity Operators
# Used to compare the memory locations of two objects.
# is   is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]   
print("a is b:", a is b)         # True
print("a is c:", a is c)         # False
print("a is not c:", a is not c) # True

# 6. Membership Operators
# Used to test if a sequence contains a certain value.
# in   not in
fruits = ["apple", "banana", "cherry"]
print("banana in fruits:", "banana" in fruits)       # True
print("grape not in fruits:", "grape" not in fruits) # True
# 7. Bitwise Operators

# Used to perform bit-level operations on integers. 

# &   |   ^   ~   <<   >>
a = 5      # 0101 in binary
b = 3      # 0011 in binary
print("a & b:", a & b)   # 0001 = 1
print("a | b:", a | b)   # 0111 = 7
print("a ^ b:", a ^ b)   # 0110 = 6
print("~a:", ~a)         # -6 (two's complement)
print("a << 1:", a << 1) # 1010 = 10
print("a >> 1:", a >> 1) # 0010 = 2



# End of Level 1 Basic Foundations - Part 1

