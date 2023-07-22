# Lesson 13 Airthmatic Operators
# + | - | * | / | //

# floor division // | round off value with minimum number
""" 
x = 10/3
print(x)
print(type(x))

y = 10//4
print(y)
print(type(y))
 """

# Lesson 14 Assignment Operators
""" 
x = 10
print(x)
x += 1
print(x)
x = x + 1
print(x)
 """

# Lesson 15 Comparision Operators | (== | != | > | >= | < | <=)
""" 
x = 10
y = 15
print("x is equal to y", x == y)
print("x is not equal to y", x != y)
print("x is greater than y", x > y)
print("x is greater than or equal to y", x >= y)
print("x is less than y", x < y)
print("x is less than or equal to y", x <= y)
 """

# Lesson 16 Logical Operators | (and | or)
""" 
a = True
b = True
c = False
d = False
print(a and b)  # True
print(a or b)  # True
print(a or c)  # True
print(a and d)  # False
print(a and b or c)  # True
print(a or b and c)  # True
# Same condition but different priority set by using round brackets
print((a or b) and c)  # False
print(a or (b and c))  # True
 """

# Lesson 17 | If Statement
# Syntax
""" 
if expression:
    # Command
elif expression:
    #Command
else:
    #command 
"""

# Ex. 1
""" 
x = 10
condition = x == 10

if condition == True:
    print("x is 10")
else:
    print("x is not 10")
 """

# Ex. 2
""" 
x = 10
# x = -50
if x > 0:
    print("x is positive number")
else:
    print("x is negative number")

 """

# Ex. 3 | Write a program to check a person us eligible to vote or not
""" 
age = 15
if age > 18:
    print("Your are eligible for vote")
else:
    print("Your are not eligible for vote")
"""

# Ex. 4 | Write a program to check alphabet is a vowel or not
# Way 1
""" 
alphabet = "g"
if alphabet == "a":
    print("Alpabet A is vowel")
elif alphabet == "e":
    print("Alpabet E is vowel")
elif alphabet == "i":
    print("Alpabet I is vowel")
elif alphabet == "o":
    print("Alpabet O is vowel")
elif alphabet == "u":
    print("Alpabet U is vowel")
else:
    print(f"Alpabet {alphabet} is not vowel")
 """

# Way 2
""" 
alphabet = "a"
if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
    print(f"Alpabet {alphabet} is vowel")
else:
    print(f"Alpabet {alphabet} is not vowel")
 """

# Task 1 | Write a program to check if the nummber is postive or not
""" 
number = -11
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"Number is negative")
else:
    print(f"Number is not integer")
"""

# Task 2 | Write a program to check if the number is even or odd
""" 
if number % 2 == 0:
    print("NUmber is belongs to Even Family")
elif number % 2 == 1:
    print(f"Number is belongs to Odd Family")
else:
    print(f"Number is not integer")
 """

# Task 3 | Write a program to display the grade of the user in subject "English",
# ask user marks obtained, output should be Grade A, Grade B, Grade C
""" 
totalMarks = 100
obtainedMarks = int(input("Type your Obtained Marks\n"))
percentage = (obtainedMarks * 100) // totalMarks
if percentage < 50:
    print("Sorry You are failed")
elif percentage >= 80 and percentage <= 100:
    print("Grade A+")
elif percentage >= 70 and percentage < 80:
    print("Grade A")
elif percentage >= 60 and percentage < 70:
    print("Grade B")
elif percentage >= 50 and percentage < 60:
    print("Grade C")
 """    

# Chapeter List - - - - -  - - - - -
# Lesson 18 | Add data in list
list_1 = ["Apple", 23, True, "Orange", -254, False]
list_1.append("Super Bike") # Add item on last index
list_1.insert(2,"Aeroplane") # Insert new item with index position
print(list_1)

# Lesson 19 | Access data in list using index
print(list_1[0]) #print first item of list_1
print(list_1[1]) #print second item of list_1
print(list_1[2]) #print third item of list_1

# Lesson 20 | Find length of list using len()
length = len(list_1)
print(length) #print length
print(list_1[length - 1]) #print last element of list_1
print(list_1[-1]) #print last element of list_1

# Lesson 21 | Update List
list_1[1] = 45
print(list_1)

# Lesson 22 | Remove Item form list
list_1.pop() # remove last item from list_1 if you didn't pass any index
print("Using pop with no index", list_1)
list_1.pop(2) # remove given index postion item 
print("Using pop with given index", list_1)
list_1.remove("Orange") # remove give index postion item 
print("Remove item using remove function", list_1)

# Lesson 23 | Clear the list or empty the list
list_1 = []
print("Clear list using assign empty list", list_1)
# list_1.clear()
# print("Clear list using using clear function", list_1)

# - - - - -  - - - - - Chapeter List
