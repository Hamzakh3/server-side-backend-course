# 1. output the numbers from 1 to 10 using range function and for loop
for num in range(1, 11):
    print(num)

# 2. output the numbers from 35 to 50 using range function and for loop
for num in range(35, 51):
    print(num)

# 3. output the numbers from -15 to -25 using range function and for loop
for num in range(-15, -26, -1):
    print(num)

# 4. output the numbers from 5 to -10 using range function and for loop
for num in range(5, -11, -1):
    print(num)


# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
for num in range(0, 51, 3):
    print(num)

# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
for num in range(1, 11):
    print(f"2 X {num} = {2*num}")

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
total = 0
prices = [3, 5, 2, 1, 4]
for price in prices:
    total += price
print(total)

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
highPrice = 0
prices = [3, 5, 2, 1, 4]
for price in prices:
    if price > highPrice:
        highPrice = price
print(highPrice)
