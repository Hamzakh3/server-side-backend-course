#iterate over dictionaries

# obj = {
#     "id":1,
#     "name": "saad",
#     "is_employed": True,
#     "is_married": False
# }

# for v in obj:
#     print(obj[v])  # to aceess values(of keys on iterating)


# list_a = [100,200,300,400]

# for k,m in enumerate(list_a):
#     print(k,m)

## creating a list and appending in new list

# list_1 = [100,200,300,400]
# list_2 = []

# list_2.append(list_1[0])
# list_2.append(list_1[1])
# list_2.append(list_1[2])

## now using loop

# for a in list_1:
#     list_2.append(a)

# print(list_2) 


# a = {
#     "id":1,
#     "name": "saad",
#     "is_employed": True,
#     "is_married": False
# },
# {   "id":2,
#     "name": "abc",
#     "is_employed": True,
#     "is_married": False
# }

# for obj in a:
#     if obj.get("name")==("saad"):
#         print(obj)
    

# s = "hello-world"

# for i in s:
#     print(i)

# for i in s:
#     if i =="e" or i =="o":
#         print(i)


## Nested Loop

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# for i in range(1,5):
#     for j in range(i):
#         print(j)

# for i in range(1,10):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(1,10):
#     for j in range(i):
#         print(j,end="")
#     print()

# for i in range(1,10):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(10,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()



## while loop

# x = 10
# while x>0:
#     print(x)
#     x-=1


# user_input = input("Enter a number between 1 and 10 \n")
# user_input = int(user_input)

# while user_input<0 or user_input>10:
#     user_input = input("please enter a number between 1 and 10 \n")
#     user_input = int(user_input)

# print("valid number is: ", user_input)



## write a program that increment variable value by 1 and it keeps incrementing the value
## unless the value reaches 20 using while loop 

# a = 1
# while a<=20:
#     print(a)
#     a+=1


## write a program to remove items from the list inside while loop

# list_a = [1,2,3,4,5]
# _len = len(list_a)

# while _len >0:
#     list_a.pop()
#     _len-=1
#     print(list_a)


# x = [1,2,3,4]                 ## answer by sir done below

# while len(x)>0:
#     print(x)
#     x.pop()



## Functions

# def func_name():
#     print("Hello World")

# func_name()

# def get_user_input():
#     user_input = input("Enter a number between 1 and 10 \n")
#     user_input = int(user_input)

#     return user_input

# user_input = get_user_input()

# while user_input>10:
#     user_input = get_user_input()


# def sum():
#     print(4 + 4)

# sum()

# def sum(a,b):
#     print(a + b)

# x=3
# y=5
# sum(x,y)


# # position independent (jab aap ko position pe dependent nahi hona ho yeh use kar sakte hain)

# def diff(x,y):
#     print(x-y)

# value_1=10
# value_2=5

# #positional argument
# diff(
#     value_2,
#     value_1
# )

# #keyword argument
# diff(
#     y=value_2,
#     x=value_1
# )



# #position independent (jab aap ko position pe dependent nahi hona ho yeh use kar sakte hain)
# def diff(x,y):
#     print(x-y)

# value_1=10
# value_2=5

# diff(
#     x=value_2,
#     y=value_1
# )

# diff(
#     y=value_2,
#     x=value_1
# )


## warna jo hum call karwate hue arguments dete hain wo upar function men same hi jaate hain
## jese call karte waqt (value_1,value_2) jaega function ke (x,y) men



# def sum (x=100,y=20):
#     print(x-y)

# value_1 = 40
# value_2 = 5

# sum(value_1)
# sum(50)


# ##neeche wala code chal jaega kyun ke humne x ki value di hui hai
# def sum (x=100,y=20):
#     print(x-y)

# value_1 = 40
# value_2 = 5

# sum(y=value_1)

# # agar value hata denge toh error dega(keyword argument bana rahe hain aese)
# def sum (x,y=20):
#     print(x-y)

# value_1 = 40
# value_2 = 5

# sum(y=value_1)


## mixing positional and keyword argument
## positional argument must come first before keyword argument if mixing

# def sum (x,y=20):
#     print(x-y)

# value_1 = 40
# value_2 = 5

# # sum(y=value_2) # error
# # sum(y=value_2,value_1) # error
# sum(value_1,y=value_2)


## function men se value bahar nikalne ke liye return use karte hain
# def sum(x,y):
#     x = x + y
#     return x

# x = sum(1,2)
# print(x)


# ## create a list of dict

# list_a = [
#     {
#         "id":1,
#         "name":"saad",
#         "gender": "male"
#     },
#     {
#         "id": 2,
#         "name": "abc",
#         "gender": "male"
#     }
# ]

# def get_employee_by_id(id):
#     print(id)
#     for i in list_a:
#         if i.get("id") == id:
#             return i
        
# i = get_employee_by_id(2)
# print(i)

# print(get_employee_by_id(1))