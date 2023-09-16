# Todays Topics
""" 
Incapsulation
classmethod
staticmethod
variables start with __
variable start with _
getter and setter for _variable
get and set method for __variable
 """

 
""" 
Incapsulation: dont allow variables to direct access from outsidde of the class, if you want to use class 
property you need to create set or get method 

"name mangli" concept is a concept when we are merging classes so its make properties name unique if property name
are same.
"""

from datetime import datetime

class Employee():
    def __init__(self, fname, lname, salary, joining_date):
        self.fname = fname
        self.lname = lname
        # Way of make private variable but its not a good practice
        self.__salary = self.validate_salary(salary)
        self._age = 20
        self.year_of_salary = self.calculate_years_of_salary(joining_date)
        

    def validate_salary(self, salary):
        if salary <= 0:
            raise Exception("Salary can't be 0 or less than 0")
        else:
            return salary
        
    # There are two ways of get and set method
    
    # Below one is only use when you use private variables "__"
    # This is not a pythonic way so its not a good practice because __ using for name mangli
    def set_slaray(self, salary):
        self.__salary = self.validate_salary(salary)

    def get_salary(self):
        return self.__salary
    
    # Below getter and setter are only use when variable start single underscore "_"
    # If you want to make private varibale use single underscore "_" and its a good way.
    """ 
    But still you can access from outside the class but there is developer responsibility that didn't 
    use single underscore variables from out side
     """
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age


    # Use class instance
    # Suppose if you have shape class you want to create quick class withour any arguments so you can create it directly from outside
    @classmethod
    def create_quick_sqaure_shape(cls):
        print(cls) #return class name
        return cls(
            "Muhammad",
            "Umaid",
            20500
        )
    
    @classmethod
    def create_quick_sqaure_triangle(cls):
        print(cls) #return class name
        return cls(
            "Muhammad",
            "Umaid",
            20500
        )
    
    # Static Method | mostly use for helpers function and utility function
    @staticmethod
    def calculate_years_of_salary(joining_date):
        today_date = datetime.now().year
        join_date = datetime.fromisoformat(joining_date).year
        print(today_date, join_date)
        return today_date - join_date


emp_1 = Employee("Muhammad", "Hamza", 20000, "2013-10-23")
emp_2 = Employee("Muhammad", "Subhan", 2000, "2019-11-23")

print(emp_1)
print(emp_2)

print(emp_1.age)
emp_1.age = 24
print(emp_1.age)

print(emp_1.get_salary())
emp_1.set_slaray(40300)
print(emp_1.get_salary())


# Important Notes:
# Start with minimum scope then gradually expand your program scope
# If anything out of scope called  over engineering 


