# Write a program to create a function that takes two arguments, name and age. print them inside function.
def user_info(name, age):
    print(f"Name:{name}, Age: {age}")

user_info("Hamza", 26)



# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name, salary=9000):
    print(f"Name:{name}, Salary: {salary}")

show_employee("Hamza", 10000)


# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

def paramsList(a, b, c, d):
    list = [a,b,c,d]
    return list

list = paramsList(4,8,c=10,d=12)
print(list)

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.
def convert_km_to_miles(km_to_miles):
    miles = km_to_miles * 0.621371
    return miles

km_to_miles = convert_km_to_miles(345)
print(f"Miles: {km_to_miles}")

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.
def divisible_by_11(number=11):
    is_divisible = number%11
    if(is_divisible == 0):
        return f"{number} is divisible by 11"
    else:
        return f"{number} is not divisible by 11"
    
is_divisible = divisible_by_11(3299)
print(is_divisible)

# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.
def find_highest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    elif num1 == num2:
        return f"{num1} and {num2} both are equals"
    else:
        return "something wrong check your inputs"
    
print(find_highest(2233,54))


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg and "fuel_per_liter" as optional arg that has default value to 280. The function should return the cost in Rs.
def fuel_cost(distance, fuel_average, fuel_per_liter = 280):
    cost = (distance / fuel_average) * fuel_per_liter
    return cost

print("Fuel Cost",fuel_cost(230, 32))

