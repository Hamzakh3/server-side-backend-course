# Lesson 24 | Dictionary
# How to create Dictionary

user = {
    "name": "Hamza",
    "age": 26,
    "gender": "male"
}


# How to get specific value from dictionary

print(user["name"])
print(user["age"])
# print(user.get("name")) #if key exist return key value otherwise return null
# print(user.get("name", "null")) #if key exist return key value otherwise return default value (second parameter is default value)


# Nestes Dictionary

user = {
    "name": "Hamza",
    "age": 26,
    "gender": "male",
    "address": {
        "city": "Karachi"
    }
}


# How to add new values in dictionary

user["phoneNumber"] = "03202313219"
user["address"]["country"] = "Pakistan"
print(user)


# How to get root length of keys

userKeyLength = len(user)
print(userKeyLength)


# How to update dictionary values

user["name"] = "Muhammad Hamza"
user["address"]["country"] = "Saudia"
user["address"]["city"] = "Madina"
# user.update({"address": {"city": "Madina"}}) # if key exisst update value otherwise add new key in dictionary
# user.update({"address": {"country": "Saudia"}}) 
print(user)


# How to Delete values from dictionary

del user["phoneNumber"]
print(user)


# How to clear dictionay

oldUserData = user.copy() #When a dictionary is copied through the copy() method, any change made in a new dictionary will not be reflected in the original dictionary.
# oldUserData = user #When a = operator is used to copy a dictionary, any change in the copied one will be reflected in the original dictionary.
user.clear()
# user = {}
print(user) 
print(oldUserData)


# How to get all keys of dictionary

user = {
    "name": "Hamza",
    "age": 26,
    "gender": "male",
    "address": {
        "city": "Karachi"
    }
}
print(user)


# How to get all keys of dictionary
print(user.keys())

# How to get all values of dictionary
print(user.values())

# How to merge two dictionary

d1 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
d2 = {
    "d": 1,
    "e": 2,
    "f": 3,
}
# d3 = d1 | d2

d3 = {**d1, **d2}
print(d3)



#  Dictionary Class Assignment
""" 
# Create a dictionary var d1 and add information with name, age, gender
d1 = {
    "name": "Hamza",
    "age": 26,
    "gender": "male"
}

# Update above dict using update function and add more information i.e. salary, deapartment, joining_date
d1.update({
    "salary": 30000,
    "department": "Production",
    "joining_data": "1/1/2023",
})
print(d1)

# remove the key 'age' from the dict
del d1["age"]
print(d1)

# add new key "dob" in above dict
d1.update({
    "dob": "20/06/1997"
})
print(d1)

# override above key "dob" with  "date_of_birth"
d1.update({
    "date_of_birth": d1["dob"] 
})

del d1["dob"]
print(d1)

# create another dictionary and merge with d1
d2 = {
    "address": "",
    "city": "",
    "country": ""
}

d3 = {**d1, **d2}
print(d3)
 """

#  Lesson 25 | Loop

user_friends = [101, 102, 103, 104, 105, 106, 107]
print(user_friends)
# Way 2 | using values
for user in user_friends:
    if user == 102:
        continue  # Skip current iteration
    if user == 106:
        break  # Break the loop means stop iteration loop will not execute after "break"
    print("user", user)

# Way 2 | using index
drinks = ["Sprite", "Due", "Coke", "7up", "Pepsi", "Fanta", "Marinda"]
total_length_of_drinks = len(drinks)
for index in range(total_length_of_drinks):
    if drinks[index].lower() == "coke":
        print(drinks[index], "available")
        break
else:  # when all iterations are executed then else block run other wise its not work
    print("Not available")

range(0, 5, 1)  # range(starting_point, length, increment)
for ind in range(1, 6, 1):
    print(ind*2)