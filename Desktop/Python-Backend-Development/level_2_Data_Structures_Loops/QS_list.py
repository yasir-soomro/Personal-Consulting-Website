
tasks = []

tasks = list("a") # this expression is write
print(tasks)

name = "afzal"

name = "A" + name[1:]
print(name)

tasks = list(["Hello"])
print(type(tasks) ,tasks)

# 7 
nums = [1,2,3,4,5,6]
print(nums[1:4]) # 2 3 4

# 8
nums[:3] # 3 2 1
nums[3:] # 4 5 6
print(nums)

# 9
nums[::-1] # reverse 

# 10 
data1 = [10, 20, 30, 40]# []
data1[1::-3] # [20]

print(data1[1:-3])


# Shopping Cart

cart = []

cart.append("Mouse")
cart.extend(["Pen", "T-Shirt" , "Shoes" , "Cap"])

cart.remove("Pen")
cart.insert(2, "Laptop")
cart.sort()
print(cart[::-1])

# Marks Processing System

marks = [21,83,40,76,32,59]
marks[2] = 89
marks.remove(21)
marks.sort()

print(marks[1::3])



list_data = [1,2,3,4,5]

tup = tuple(list_data)

print(type(tup),tup)

x = list(tup)
x.append(7)
print(type(x),x)

# features
# username take a input
# store 3 movies name



# movies = []

# mov1 = input("Enter your first mov : ")
# mov2 = input("Enter your sec mov : ")
# mov3 = input("Enter your third mov : ")

# movies.extend([mov1,mov2,mov3])
# for m in movies:
#     print("Fav Mov : ", m)




user_list = [1,2,3,1,2]

new_List = user_list.copy()
new_List.reverse()

if user_list == new_List :
    print("plindrome")
else:
    print("plindrome")

#  practice questions in dictionary and set 

# Store Following word meaning in a python Dic

Dict = {
    "table" :[ "a peiece of fur" ,"list of facts" ],
    "cat" : "a small animal"
}

print(Dict)


Subj = {"py","ja","c++","py","js","ja","py","ja","c++","c",}

print(f"Total Class Rooms of Sub : {len(Subj)} and Here is Total Sub : {Subj}")

stu_user = {}

stu_s = {"Eng" : 81}
stu_ss = {"Sind" : 85}
stu_sss = {"chm" : 93}

stu_user.update(stu_ss,)
stu_user.update(stu_s,)
stu_user.update(stu_sss,)
print(stu_user)

values = {9,9.2 ,8, "8"}
print(values)

