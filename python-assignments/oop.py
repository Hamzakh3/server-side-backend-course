"""
In this exercise, you will create a Python class coursesd Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

 

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll 
in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses
"""

class Student():
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]
    student_id = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        self.student_id += 1

    def display_info(self):
        info = {
            "name":self.name,
            "age": self.age
        }
        return info

    def enroll(self, selected_course):
        for course in self.available_courses:
            if course == selected_course:
                self.courses.append(course)
                return True
            
        return False

    def list_courses(self):
        return self.courses

    def list_available_courses(self):
        return self.available_courses
    

std_1 = Student("Hamza", 26)
std_2 = Student("Waleed", 26)
std_3 = Student("Subhan", 25)

std_1.enroll("English")
std_1.enroll("Urdu")
std_2.enroll("Urdu")
std_2.enroll("Math")
std_3.enroll("Physics")
std_3.enroll("Chemistry")
std_3.enroll("English")

print(std_1.list_courses())
print(std_2.list_courses())
print(std_3.list_courses())

print(Student.available_courses)

