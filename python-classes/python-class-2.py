# # Chapter String Start - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# #Lesson 8 | Concatenation | Merge two string into 1 string
# firstName = "Muhammad"
# lastName = "Hamza"
# print("Lesson 8 | Concatenation")
# print(firstName+" "+lastName) # Way 1 | Output "Muhammad Hamza"
# # print("Muhammad"+"Hamza") # Way 2 | Output "MuhammadHamza"

# #If we merge numbers
# itemOnePrice = 540
# itemTwoPrice = 230
# print(itemOnePrice + itemTwoPrice) # Way 1 | Output 770 
# # print(540+230) # Way 2 | Output 770

# # If we merge two number string
# itemOnePriceString = "540"
# itemTwoPriceString = "230"
# print(itemOnePriceString + itemTwoPriceString) # Way 1 | Output "540230" becuase python knows every value in quotation it would be string 
# # print("540"+"230") # Way 2 | Output "540230" 


# #Lesson 9 | String Interpolation | add any veriable or dynamic values in string
# # There are three ways 
# # 1. F String  2. format() 3. %s
# fullName = "Muhammad Hamza"
# age = 26

# # with F String
# print("Lesson 9 | String Interpolation | f String")
# print(f"I am {fullName}, My age is {age}") # Output | "I am Muhammad Hamza, My age is 26"
# # with format()
# print("Lesson 9 | String Interpolation | format")
# print("I am {}, My age is {}".format(fullName, age)) # Output | "I am Muhammad Hamza, My age is 26"
# # with %s()
# print(f"Lesson 9 | String Interpolation | %s")
# print("I am %s, My age is %s "%(fullName, age)) # Output | "I am Muhammad Hamza, My age is 26"

# # Lesson 10 | Escape Characters | "\n" "\t" \

# bio = "My name is Hamza"
# jobTitle = "Frontend Developer"

# # \n | Use For break line
# print(bio,"\n", jobTitle)

# # \t | Use For Tab and Tab equals to 4 spaces
# print(bio,"\t", jobTitle)

# # \n | Use For Special Characters
# print('I\'m hamza')
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Chapter String End

# # Chpater Input - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# # Lesson 11 | input | Use for get input from user

# iptName = input("Whats your name")
# iptAge = input("Whats your age")

# print(iptName)
# print(iptAge)

# Exercise
# Write a program to ask user his name. The name should be asked in new line
# ex1 = input("Your Name \n")

# Hi USER_INPUT, Welcome back
# ex2 = input("Your Name")
# print("Hi, {} Welcome Back".format(ex2))

# Ex3 | Get input two numbers and print their sum
# sum1 = input("Input Number 1 \t")
# sum2 = input("Input Number 2 \t")
# print(int(sum1)+int(sum2))

# Ex4 | Get input a number and print square of a number
# ex4 = int(input("Type number for find Square \t"))
# print(ex4*ex4)

# Ex5 | Wtire a program to ask user 3 subjects scores and display
# Math: SCORE
# English: SCORE
# Physics: SCORE

# mathSub = int(input("Type your Math Score"))
# englishSub = int(input("Type your English Score"))
# physicsSub = int(input("Type your Physics Score"))
# print(f"Math: {mathSub}\nEnglish: {englishSub}\nPhysics: {physicsSub}")

# Ex6 | Ask user two numbers and display SUM, MULTIPLY< DIVISION, SUBTRACTION
# SUM: SCORE
# MULTIPLY: SCORE
# DIVIDE: SCORE
# SUBTRACT: SCORE

# iptNumber1 = int(input("Type Number 1"))
# iptNumber2 = int(input("Type Number 2"))
# print(f"SUM: {iptNumber1+iptNumber2}")
# print(f"SUBTRACT: {iptNumber1-iptNumber2}")
# print(f"MULTIPLY: {iptNumber1*iptNumber2}")
# print(f"DIVIDE: {iptNumber1/iptNumber2}")

# Input function Exercise
x = 1
y = 2
z = 0
print(f"x is, {x}")
print(f"y is, {y}")

# x,y = y,x
z = x
x = y
y = z

print(f"x is, {x}")
print(f"y is, {y}")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Chapter Input

# String Methods
# string = "My name is Hamza"
# print(string.format())
# print(string.lower())
# print(string.upper())
# print(string.capitalize())

# Buitin FUnction for Strings
# print(len(string))
# print(type(string))
# print(round(2.5454545))
# print(isinstance(string, str))
# print(isinstance(string, int))


# Airthmatic Operators
# + | - | * | /
















