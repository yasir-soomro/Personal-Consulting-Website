# 🟢 LEVEL 1 — PYTHON BASICS (FOUNDATION)

Welcome to **Level 1 of Python**.  
This level is designed to build **strong programming foundations** and **logical thinking**, not just syntax.

If you complete this level **properly**, you will:
- Think like a programmer
- Understand how code works
- Write clean beginner-level programs confidently
- Be fully ready for **Level 2 (Control Flow & Logic)**

---

## 🎯 Goal of Level 1

> Learn **how Python thinks**, how programs execute, and how to work with basic data.

This level focuses on:
- Core concepts
- Real understanding
- Practical examples
- Hands-on practice

---

## 👤 Who Should Study This Level?

- Absolute beginners
- Students starting programming
- Developers switching to Python
- Anyone weak in programming fundamentals

⚠️ **No prior coding knowledge required**

---

## 🧠 What You Will Master in Level 1

By the end of this level, you will confidently understand:

- What Python is and how it works
- Installing and setting up Python
- Writing and running Python programs
- Variables and data storage
- Core data types
- Input & output
- Operators and expressions
- Basic math & logic
- Comments & code readability

---

# 📘 COMPLETE LEVEL 1 SYLLABUS (WITH EXPLANATIONS & EXAMPLES)

---

## 1️⃣ What is Python?

Python is a **high-level, interpreted programming language** known for:
- Simple syntax
- Easy readability
- Beginner-friendly
- Widely used in backend, AI, automation, data science

Python executes code **line by line**, making it easy to understand and debug.

---



## 1️⃣ Writing and Running Python Programs

**Definition:** Writing Python programs means creating instructions for the computer to execute using Python syntax. Running a program means executing these instructions to get results.

**Example:**
```python
print("Hello, World!")  # This program prints text to the screen


## 2️⃣ Installing Python & Setup

1. Go to [python.org](https://www.python.org/downloads/)  
2. Download and install the latest version
3. Add Python to PATH during installation
4. Verify installation in terminal:
```bash
python --version


3️⃣ Variables and Data Storage

Definition: A variable is a named storage that holds data in memory. Variables can store numbers, text, or boolean values and can be updated dynamically.

Example:

age = 20       # integer
name = "Afzal" # string
price = 99.5   # float


Notes:

Variable names must be meaningful.

Cannot start with numbers or contain spaces.

Python automatically detects the data type.



4️⃣ Core Data Types

Definition: Data types classify the type of data a variable can hold.

Type	Description	Example
int	Whole numbers	10
float	Decimal numbers	3.14
str	Text	"Python"
bool	True / False	True

Example:

x = 10
y = 5.5
language = "Python"
is_active = True


5️⃣ Input & Output

Definition: Input is how a program receives data from the user. Output is how a program displays results to the user.

Example:

name = input("Enter your name: ")  # input
print("Hello", name)               # output


⚠ Input is always a string. Use type casting if needed:

age = int(input("Enter your age: "))

6️⃣ Operators and Expressions

Definition: Operators perform operations on data. Expressions combine values and operators to compute results.

Types of Operators:

Arithmetic: + - * / // % **

Comparison: == != > < >= <=

Logical: and or not

Example:

a = 10
b = 5
print(a + b)           # 15
print(a > b)           # True
print(a > 5 and b < 10) # True

7️⃣ Basic Math & Logic

Definition:

Basic math: arithmetic calculations like addition, subtraction, multiplication, division, modulo, exponentiation.

Logic: decision-making using comparisons and logical operators.

Example:

# Math
x = 7
y = 3
print(x ** y)  # 343

# Logic
age = 20
print(age >= 18) # True

8️⃣ Comments & Code Readability

Definition: Comments explain code and are ignored by Python. Code readability makes your program easier to understand.

Example:

# Single-line comment
"""
Multi-line comment
explaining the program
"""
print("Python is readable!") # Prints message


Practice Programs
Program 1: Simple Calculator
a = int(input("First number: "))
b = int(input("Second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

Program 2: Age Eligibility Checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")

