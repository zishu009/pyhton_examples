'''
Mini Project: Student Grades Management System

✅ Features:
Store student’s name and marks (private).
Calculate grade automatically based on marks.
Use getter to view marks and grade safely.
Use setter to update marks with validation (marks must be between 0 and 100).

'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private variable

    # Getter for marks
    @property
    def marks(self):
        return self.__marks

    # Setter for marks (with validation)
    @marks.setter
    def marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Marks must be between 0 and 100.")

    # Method to calculate grade based on marks
    def get_grade(self):
        if self.__marks >= 90:
            return 'A'
        elif self.__marks >= 80:
            return 'B'
        elif self.__marks >= 70:
            return 'C'
        elif self.__marks >= 60:
            return 'D'
        else:
            return 'F'

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")


# Using the class
student1 = Student("Alice", 85)

# Display student info
student1.display_info()

# Update marks
student1.marks = 92  # Using setter
print("\nAfter updating marks:")

# Display updated info
student1.display_info() 

# Try setting invalid marks
student1.marks = 120  # Will show validation error
