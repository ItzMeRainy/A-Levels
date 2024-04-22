# Create Class for student.
class Student:

    # Initialize attributes for object (Known as Constructor).
    def __init__(self, firstname, lastname, age, subjects):
        self.firstname = firstname
        self.lastname = lastname
        # Attributes with a dunder or "double underscore" are private attributes and can only be accessed using a getter.
        self.__age = age
        self.subjects = subjects

    # Method for First Name attribute.
    def GetFirstName(self):
        print(f"This student's first name is \"{self.firstname}\"") # This will output the object's attribute.

    # Getter for Age attribute.
    def GetAge(self):
        return int(self.__age)

    # Setter for Age attribute.
    def SetAge(self, new_age):
        self.age = new_age

# Created Object, in this case for student (An object is an instance of the class).
Student_1 = Student("Rayyan", "Yasir", "19", ["Math", "Computer Science", "Economics"])

# Calling defined method.
Student_1.GetFirstName()

# Using Age methods to increase Student's age by 1 year (Note how I did not use Student_1.__age because it is private.)
Student_1.SetAge(Student_1.GetAge() + 1)
print(f"This student's age is now: {Student_1.GetAge()}")