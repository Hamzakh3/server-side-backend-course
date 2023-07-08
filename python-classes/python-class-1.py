# Lesson 1 | Print Hello World
print("Hello World")

# Lesson 2 | Remove Line Break in command
print("A")
print("B")
print("C")
# Output
"""
A
B
C
"""
# Suppose you want to show all print result in one line like (ABC)
print("A", end="")
print("B", end="")
print("C")

# Lesson 3 | Print with Seperators
print("A", "B", "C")
# Output A B C
# if you want to show result in one line with your own seperator
print("A", "B", "C", sep="|")

# Lesson 4 | Print Numbers
print(2 + 2)
# Note: Dont do this with numbers i.e. print("2 + 2")

# Lesson 5 | Single Comment and Multiline Comment
# Single Line Comment (#)
# Multiline Comment ("""Your text""")

# Exercises
# Display 2 subject name and their score i.e. Math:50
# Display 2 subject name and their score i.e. Math: 50

print("Math:", end="")
print(50)
print("Math:", 50 )

# Display the word: There are three "chickens" in the house
print('There are three "chickens" in the house')