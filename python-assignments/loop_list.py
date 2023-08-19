# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
items = [3, 5, 2, 1, 4]
muliplyItems = items[0]
for item in items:
    muliplyItems *= item
print(muliplyItems)


# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop
for num in range(0, 100):
    if num % 5 == 0:
        if num > 30 and num < 50:
            print(f"{num} divisible by 5. {num} greater than 30 and less than 50")
            continue
        if num > 80:
            print(
                f"{num} divisible by 5. {num} is greater than 80 that's why loop is stop")
            break


# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn
names = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
for name in names:
    if len(name) > 5:
        print(name)

# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colorLen = len(colors)
removeColors = []
for index in range(colorLen):
    if index == 0 or index == 4 or index == 5:
        removeColors.append(colors[index]) 
for removeColor in removeColors:
    colors.remove(removeColor)

print(colors)


# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

for oddNum in range(100):
    if oddNum%2 == 1:
        print(oddNum)


# 6. List contains 30 elements. Display first 5 and last 5 elements
elements = []
for num in range(1, 31):
    elements.append(f"element {num}")

for index in range(len(elements)):
    if index < 5 or index > (len(elements) - 1) - 5:
        print(elements[index])
    

# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# output should be 'helloworld' in one line
alphabets = [ 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
word = ''
for alphabet in alphabets:
    word += alphabet
print(word)

# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2
l1 = [1, 2, 3, 4, 5]
l2 = []

for item in l1:
    l2.append(item)

print(l2) 

# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3
words = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
search = 'hi'
count = 0
for word in words:
    if search == word:
        count += 1

print(count)