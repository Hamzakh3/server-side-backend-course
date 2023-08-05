# Exercise_1
# Write a program to check whether a person is eligible to vote or not?

""" 
voter_min_age = 18
voter_age = 19
if voter_age >= voter_min_age:
    print("You are eligible for vote")
else:
    print(f"Your age is {voter_age}, you are not eligible for vote") """

#----------------------------------------------------------------------------------------------------

# Exercise_2
# Write a program to check char is vowel or not.
""" 
vowel_ipt = "r"
if vowel_ipt == "a" or vowel_ipt == "e" or vowel_ipt == "i" or vowel_ipt == "o" or vowel_ipt == "u":
    print(f"{vowel_ipt} is belongs to vowel family")
else:
    print(f"{vowel_ipt} is not vowel") """

#----------------------------------------------------------------------------------------------------

# Exercise_3
# Write a program to check the number is positive or negative. User input.
""" 
get_num_ipt = int(input("Type any number to check the  number is positive or not\n"))
if get_num_ipt >= 0:
    print(f"{get_num_ipt} is a positive number")
elif get_num_ipt < 0:
    print(f"{get_num_ipt} is a negative number")
else:
    print(f"{get_num_ipt} is not an integer") """

#----------------------------------------------------------------------------------------------------

# Exercise_4
# Write a program to check whether a number is odd or even?
""" 
get_num_ipt = int(input("Type any number to check the number is even or odd\n"))
if get_num_ipt%2 == 0:
    print(f"{get_num_ipt} is an even number")
elif get_num_ipt%2 != 0:
    print(f"{get_num_ipt} is an odd number")
else:
    print(f"{get_num_ipt} is not an integer") """

#----------------------------------------------------------------------------------------------------

# Exercise_5
# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
""" 
total_marks = 100
obtained_marks = int(input("Type your obtained marks out of 100\n"))
percentage = (obtained_marks * 100) // total_marks
if percentage < 50:
    print("Sorry You are failed")
elif percentage >= 50 and percentage < 60:
    print("Grade C")
elif percentage >= 60 and percentage < 70:
    print("Grade B")
elif percentage >= 70 and percentage < 80:
    print("Grade A")
elif percentage >= 80 and percentage <= 100:
    print("Grade A+") """

#----------------------------------------------------------------------------------------------------

# Exercise_6
# Write a program to check whether a number is divisible by 7
""" 
divisible_by_7 = int(input("Type any number to check the number is divisible by 7\n"))
if divisible_by_7%7 == 0:
    print(f"{divisible_by_7} is divisible by 7")
else:
    print(f"{divisible_by_7} is not divisible by 7") """

#----------------------------------------------------------------------------------------------------

# Exercise_7
# Write a program to check if year is leap year.
""" 
is_leap_year = int(input("Type year to check the year is leap or not\n"))
if is_leap_year%4 == 0:
    print(f"{is_leap_year} is a leap year")
else:
    print(f"{is_leap_year} is not a leap year") """

#----------------------------------------------------------------------------------------------------

# Exercise_8
# Write a program to ask user its name and check whether name consists of 5 or more letters
""" 
user_name = input("Type your name\n")
if len(user_name) >= 5:
    print(f"{user_name} consist 5 or more characters")
else:
    print(f"{user_name} characters length is less than 5") """

#----------------------------------------------------------------------------------------------------

# Exercise_9
# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly
""" 
int_1 = int(input("Type you integer 1\n"))
int_2 = int(input("Type you integer 2\n"))
operator = input("Type your mathematical operator\n")
if operator == "+":
    print(f"Your answer is {int_1+int_2}")    
elif operator == "-":
    print(f"Your answer is {int_1-int_2}")    
elif operator == "*":
    print(f"Your answer is {int_1*int_2}")    
elif operator == "/":
    print(f"Your answer is {int_1/int_2}")
else:
    print("Some thing is wrong please check your input again")     """

#----------------------------------------------------------------------------------------------------

# Exercise_10
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
""" 
get_number = int(input("Type any number to check the number is divisible by 2 and 3\n"))
if get_number%2 == 0 and get_number%3 == 0:
    print(f"{get_number} is divisible by 2 and 3")
elif get_number%2 == 0 and get_number%3 != 0:
    print(f"{get_number} is divisible by 2")
elif get_number%2 != 0 and get_number%3 == 0:
    print(f"{get_number} is divisible by 3")
else:
    print(f"{get_number} is not divisible by 2 and 3")
 """

#----------------------------------------------------------------------------------------------------

# Exercise_11
# Write a program that accepts 2 inputs from user and check which number is largest.
""" 
get_number_1 = int(input("Type your number 1\n"))
get_number_2 = int(input("Type your number 2\n"))
if get_number_1 > get_number_2:
    print(f"{get_number_1} is larger than {get_number_2}")
elif get_number_1 < get_number_2:
    print(f"{get_number_2} is larger than {get_number_1}")
elif get_number_1 == get_number_2:
    print(f"{get_number_1} is equal to {get_number_2}")
else:
    print("Something wrong please check your inputs") """

#----------------------------------------------------------------------------------------------------
# Exercise_13
# Write a program that accepts 3 input from user and check which number is largest.
""" 
get_number_1 = int(input("Type your number 1\n"))
get_number_2 = int(input("Type your number 2\n"))
get_number_3 = int(input("Type your number 3\n"))

if get_number_1 > get_number_2 and get_number_1 > get_number_3:
    print(f"{get_number_1} is larger than {get_number_2} and {get_number_3}")

elif get_number_2 > get_number_1 and get_number_2 > get_number_3:
    print(f"{get_number_2} is larger than {get_number_1} and {get_number_3}")

elif get_number_3 > get_number_1 and get_number_3 > get_number_2:
    print(f"{get_number_3} is larger than {get_number_1} and {get_number_2}")

else:
    print("May be all numbers are equals or something wrong please check your inputs") """

#----------------------------------------------------------------------------------------------------
# Exercise_14
# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
""" 
signal_status = input("Type Signal Status Color\n")
if signal_status.lower() == "green":
    print("Car is allowed to go")
elif signal_status.lower() == "yellow":
    print("Car has to wait")
elif signal_status.lower() == "red":
    print("Car has to stop")
else:
    print("Invalid Input") """

#----------------------------------------------------------------------------------------------------
# Exercise_15

# Write a program to trace your subject mark. Your program should fulfill the following conditions:
# If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
# display "you are fail" if their mark is below 50.
# display "you are pass" if they score 50 and above.
# If subject mark is between 50 and 60, Remark: Good
# If subject mark is between 60 and 80, Remark: Very Good
# If subject mark is between 80 and 100, Remark: Outstanding
""" 
total_marks = 100
obtained_marks = int(input("Type your obtained marks out of 100\n"))

if obtained_marks >= 0 and obtained_marks <= 100:
    if obtained_marks < 50:
        print("You are failed")
    elif obtained_marks >= 50:
        print("You are passed")
        if obtained_marks >= 50 and obtained_marks < 60:
            print("Remark: Good")
        elif obtained_marks >= 60 and obtained_marks < 80:
            print("Remark: Very Good")
        elif obtained_marks >= 80 and obtained_marks <= 100 :
            print("Remark: Outstanding")
else:
    print("error: mark should be between 0 and 100 only")
 """