# Write a Python program to copy a list using for loop. consider a list
li = [1, 2, 3, 4]
li_2 = []
# use for loop and add al the items in li_2

for item in li:
    li_2.append(item)

print("li_2", li_2)

# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 3]


def isAnyItemMatch(list1, list2):
    for item in list1:
        for item2 in list2:
            if item == item2:
                return True


print(isAnyItemMatch(li, l2))


# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output:
# 0 100
# 1 200
# 2 300
# 3 400
list_1 = [100, 200, 300, 400]
for index, item in enumerate(list_1):
    print(f"Index:{index}, Value:{item}")

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop
l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']

lettersCount = {}

for alpha in l1:
    count = 0
    for alpha2 in l2:
        if alpha == alpha2:
            count += 1
    if count != 0:
        lettersCount[alpha] = count

print(lettersCount)


# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"


# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”
""" 
user_input = int(input("Type any number"))
while user_input != 0:
    user_input = int(input("Type any number"))
print("Finaly you type 0.")
 """
# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list
""" 
input_count = 0
input_list = []
while input_count < 5:
    user_input = int(input("Type any number for Sum"))
    input_list.append(user_input)
    input_count += 1
total_count = 0
for n in input_list:
    total_count += n
print("Total Count of your inputs are", total_count)
 """

# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
""" 
user_input = int(input("Type any number"))
user_inputs = []
while user_input >= 0:
    user_input = int(input("Type any number"))
    user_inputs.append(user_input)
total = 0
for n in user_inputs:
    total += n
print("Your sum of positive numbers are ", total )
 """

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
""" 
user_name = input("type names")
users = []
while user_name != "END":
    user_name = input("type names")
    if user_name != "END":
        users.append(user_name)

for user in users:
    print(user)

print("I am Done")
 """

# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"
""" 
l1 = [11, 33, 50]
number = ""
for n in l1:
    number+= str(n)
print(number)
 """

# Write a Python program to copy a dict using for loop. consider a dict
d1 = {
    "id": 1,
    "name": "your-name",
    "gender": "male"
}
d2 = {}
# use for loop and add al the items in d2
# hint: https://github.com/mdanish0320/teaching-class/blob/de18a6216425cde375c82a793480919af824a67c/JP-BE-PY-batch-1/loop/enumerate_.py#L12C1-L19C16

for x, y in enumerate(d1.items()):
    d2[y[0]] = y[1]
print(d2)
