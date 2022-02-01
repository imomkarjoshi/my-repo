print("Hello World")
print("*"*10)

# Python Extension for VSCode Editor
# Python Enhancement Proposals (PEP)

x = 2
# Format on save!!

################## Variables #################
students_count = 1000  # type - int
ratings = 4.99  # type - float
is_published = False  # type - bool
course_name = "Python"  # type - string

x, y = 1, 2
# above line is equivlent to below
x = 1
y = 2
#################
x = y = 2
# above line is equivlent to below
x = 2
y = 2
##############

################## Dynamic Typing #################
x = 1
x = "Omkar"
# No error even if the data type is changed
# Type is defined at run time

################## Type Annotations #################
age: int = 20
age = "Python"


################## Mutable and Immutable Types #################
x = 1
print(id(x))  # address of x
# Address of immutable items wont change with updates to the variable
# i.e.,
x += 1
print(id(x))
# The above line will print another address

_list = [1]
print(id(_list))

_list.append(4)
print(id(_list))
# The address of both the prints will give the same results as lists are mutable

################## Strings #################
course = "Python Programming"

print(course[0])  # "P" 0th index
print(course[-1])  # "g" last index
print(course[0:3])  # "Pyt" 0 1 2 index not the end index
# "Pyt" 0 1 2 index not the end index start index is defaulted to 0
print(course[:3])
# "Python Programming" end index is defaulted to length of the string
print(course[0:])
# "Python Programming" start = 0 end index is defaulted to length of the string
print(course[:])

# Strings are immutable so if we access a character or group of chars in  string
# they are copied to a location and then are accessed
# i.e.,
print(id(course))
print(id(course[0]))
print(id(course[-1]))
# All the above will give different addresses

################## Escape Sequences #################

message = "Python \"Programming"  # \ to add " inside a string

# i.e., we can escape the abiguity created after the "sf"gf" => "sf\"gf"
# and makes the string readable to the interpreter

# if the statements are too confusing we can use the """ """ to use it as we use `` in js

message = """ """

################## Formatted Strings #################
first = "Omkar"
last = "Joshi"
full = first + " "+last  # concatenation
# formatted strings
full = f"{first} {last}"
# this will be more readable using the formatted strings or f-strings

################## String Methods #################
course = "Python Programming"
# .upper()
# .lower()
# .title()
# .strip() remove whitespaces
# .find("") find the "" inside the string
# .replace("","f")
# bool_val = "Pro" in course => true
# bool_val = "Pro" not in course => false

################## Numbers #################
x = 10  # integer
x = 0b10  # binary bin()
x = 0x10  # hexadecimal hex()

x = 2 + 7j  # Complex number

################## Arithmatic Operators #################
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3      # float
x = 10 // 3     # integer division
x = 10 % 3
x = 10 ** 3

PI = 3.14
# round(PI)
# abs(PI)
# print(round(PI//1))

################## Type Conversion #################
# x = int(input("X:"))
# Expilicitly typed as python doesn't perform type conversions for us
print(x+1)

# int()
# float()
# bool()
# bool() will return according to Truthy/ Falsy values
# "", 0, [], None
# str()


################## Conditional Statements #################
age = 22

if age > 18:
    print("Adult")
elif(age >= 13):
    print("Teen")
else:
    print("Child")

print("All done!")

################## Logical Operators #################
# and
# or
# not

age = 22

# if age >= 18 and age < 65:
# Above is same as
if 18 <= age < 65:
    print("Eligible")

################## Ternary Operator #################

message = "Eligible" if 18 <= age < 65 else "Not Eligible"

################## For Loops #################

# for x in "Omkar":
#     print(x)

# for x in ["a", "b", "c"]:
#     print(x)

# for x in range(5):
#     print(x)


################## For Else Loops #################

names = ["John", "Marry"]

# for name in names:
#     if(name.startswith("J")):
#         print("Found")
#         break
# else:
#     print("Not Found")

################## While Loops #################

guess = 0
answer = 5

while answer != guess:
    # guess = int(input("Guess: "))
    pass

else:
    pass

################# Function #################


# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number+by)


# print(increment(2, by=3))
# print(increment(2))

################# Arguments #################


# def multiple(*list):
#     total = 1
#     for x in list:
#         total *= x
#     return total


print("start")
# print(multiple(1, 2, 3, 4, 6))
print("end")


# def save_user(**user):
#     print(user)


# save_user(id=1, name="omkar")

################ Scope #################


message = "a"


# def greet():
#     if True:
#         message = "a"
#     print(message)


################## Lists #################
_list = [1, 2, 3, [1, 2]]
five_zeros = [0]*5
combine = _list + five_zeros  # concatenation of arrays

numbers = list(range(5))  # [0,1,2,3,4]
chars = list("Omkar")  # [O,m,k,a,r]
# len(chars) #length

nums = [1, 2, 4, 3, 5]
nums[0] = 8
# [8, 2, 4, 3, 5]
nums = list(range(20))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(nums)
print(nums[:3])  # [0, 1, 2]
print(nums[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Unpacking
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)  # 1 2 3


numbers = [1, 2, 34, 5, 5, 6, 6, 6]

first, *others = numbers
print(first)  # 1
print(others)  # [2, 34, 5, 5, 6, 6, 6]
# when we seperate the elements of array in different variables we call it unpacking
# when we combine many variables to form a different array we call it packing

# Loop over lists
letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):
    print(index, letter)

# Add/ Remove

letters = ['a', 'b', 'c']
# Add
letters.append('z')  # ['a', 'b', 'c','z']
letters.insert(0, '-')  # ['-','a', 'b', 'c','z']

# Remove
letters.pop()  # ['-','a', 'b', 'c']
letters.pop(0)  # ['a', 'b', 'c']
letters.append('b')  # ['a', 'b', 'c','b']
letters.append('b')  # ['a', 'b', 'c','b','b']
letters.append('b')  # ['a', 'b', 'c','b','b','b']

letters.remove('b')  # ['a', 'c','b','b','b']


del letters[0:3]  # ['b','b']
print(letters)

letters.clear()  # []

# Finding Items
letters = ['a', 'b', 'c']

if 'd' in letters:
    letters.index('d')

# Sorting
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)

new_numbers = sorted(numbers, reverse=True)
# .sort() modifies the original list
#  sorted() returns a sorted list and can be stored in a new array/list

items = [
    ("Product1", 10)
    ("Product2", 9)
    ("Product3", 12)
]

# items.sort()
#  [
#     ("Product1", 10)
#     ("Product2", 9)
#     ("Product3", 12)
# ]


def sort_item(item):
    return item[1]


# Lambda Functions
# items.sort(key=lambda item: item[1])
#  [
#     ("Product2", 9),
#     ("Product1", 10),
#     ("Product3", 12)
# ]

# Lambda function will eliminate the definition of a new function and we can create an
# annonymous function for the same

# MapFunction
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])
# prices = [10, 9, 12]
# But above way is a bit ugly

prices = list(map(lambda items: item[1], items))
# prices = [10, 9, 12]

# Filter Function
filtered = list(filter(lambda item: item[1] >= 10, items))
print(prices)
print(filtered)

# List Comprehensions
# map and filter functions can be alternated to using for in expression/ comprehension

prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]
print(prices)
print(filtered)

# Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

zipper = list(zip(list1, list2))  # [(1,10),(2,20),(3,30)]

# Stacks
_stack = []
# push
_stack.append(1)
# pop
_stack.pop()


# Queues
# Enqueue/ Add
# Dequeue/ Remove

# Tuples
# -Read Only List

tup_point = (1, 2)  # class 'tuple'
list_to_tuple = list([1, 2, 3])  # (1,2,3)


# Thumb Rule- if we dont want to change the list by any chance we should use tuple

# Swapping Variables
x = 10
y = 12

print(x, y)
z = x
x = y
y = z
print(x, y)

x, y = y, x
# This will give the same result

# Arrays
# number = array('i', [1, 2, 3])

# Sets - List without any duplicates

first = set([1, 1, 2, 2, 4, 3])
second = {1, 5}

_union = first | second         # {1,2,3,4,5}
_intersection = first & second  # {1}
_difference = first - second    # {2,3,4}
_sematic_difference = first ^ second
# {2,3,4,5} (In first or second but not in both)

# Sets cannot be accessed like set[0] as they are unordered

# Dictionary
# - Key: Value pair

point = {"x": 1, "y": 2}
# Dictionary can be declared as follows too
point = dict(x=1, y=2)

print(point["x"])  # 1
point["x"] = 10
print(point)  # {"x": 10, "y": 2}

# we can also use get()/ set() methods of dictionaries

point.get('x')  # this returns 10
point.get('a')  # this returns None as a is not in point
point.get('a', 0)  # this returns 0 as a is not in point

del point['x']
print(point)  # {"y": 2}

for key in point:
    print(key, point[key])

for key, value in point.items:
    print(key, value)

# Comprehension in sets/ dictionary
# Like we generate list by comprehension of [expression for item in items] we can generate
# sets/dictionaries but for tuples we get some runtime errors

# Generator Expression
values = (x*2 for x in range(5))
print(values)
# generator object tht is iterable but not stored
# in memory but is generated when we need it so memory is saved

# Unpacking Operator
nums = [1, 2, 3]
print(*nums)  # 1 2 3
# We can unpack any iterable using * operator

# Unpacking Dictionary
first = {'x': 1}
second = {'x': 10, 'y': 2}
combine = {**first, **second, "z": 1}
# Combine = {x:10,y:2,z:1}
# #x was in both it'll take the last value for the same key


################# Exceptions #################
numbers = [1, 2]
print(numbers[3])

try:
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Error")
else:
    print("No Error")
print("Continue")
# Implementing Exceptions take almost 4x time as compared to if: else block
# so try to use If-else in cases
