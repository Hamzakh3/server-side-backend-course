# Exercise# 1
# Create a list of juices, add 5 items using append
""" 
juices = []
juices.append("Banana")
juices.append("Mango")
juices.append("Orange")
juices.append("Peach")
juices.append("Apple")
print(juices)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 2
# Create a list of cars, add 5 items using insert
""" 
cars = []
cars.insert(0,"McLaren")
cars.insert(1,"Ferrari")
cars.insert(2,"Bugati")
cars.insert(3,"Supra")
cars.insert(3,"Lamborghini")
print(cars) 
"""

# ------------------------------------------------------------------------------------------------
# Exercise# 3
# Remove last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]	using pop and len
""" 
furniture1 = ["bed", "table", "chair", "sofa"]
furniture2 = ["bed", "table", "chair", "sofa"]

furniture1.pop()
furniture2.pop(len(furniture2)-1)

print(furniture1)
print(furniture2)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 4
# Remove second last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] by len and index
""" 
furniture1 = ["bed", "table", "chair", "sofa"]
furniture2 = ["bed", "table", "chair", "sofa"]

furniture1.pop(len(furniture1)-2)
furniture2.pop(-2)

print(furniture1)
print(furniture2)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 5
# Remove first item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
""" 
furniture = ["bed", "table", "chair", "sofa"]
furniture.pop(0)
print(furniture)
 """
# ------------------------------------------------------------------------------------------------
# Exercise# 6
# Remove the item “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
""" 
furniture = ["bed", "table", "chair", "sofa"]
furniture.remove("chair")
print(furniture)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 7
# Remove all “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’, ‘chair’]
""" 
furniture = ["bed", "table", "chair", "sofa", "chair"]
furniture.remove("chair")
furniture.pop()
print(furniture)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 8
# Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]
""" 
list_1 = ["A", "B", "C"]
list_2 = ["D", "E", "F"]

list_1.append(list_2[0])
list_1.append(list_2[1])
list_1.append(list_2[2])

print(list_1)
 """

# ------------------------------------------------------------------------------------------------
# Exercise# 9
# Write a Python program to check if a list is empty or not.
""" 
list_1 = []
if len(list_1) == 0:
    print("list_1 is empty")
else:
    print("list_1 is not empty")
"""
