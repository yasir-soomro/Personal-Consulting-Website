

# WAP to input user's first name & print its length'

first_name = str (input("Enter your name :"))

print("length of your name is : ",len(first_name))

# WAP to find the occurrence of "a"in the string

a   = first_name.find("a")
print("the occurrence of a in the string is index at : ",a)

a = first_name.count("a")
print("the count of a in the string is : ",a)

# WAP to check if a number entered by the user is odd or even

num = int(input("Enter a Number :"))

if (num % 2 == 0 ):
    print("The number is Even")
else:
    print("The Number is Odd")

