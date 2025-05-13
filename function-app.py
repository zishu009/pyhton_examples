'''
Mini Project: Student Management System (Function-Based)

We will create an app where you can:
Add a new student
View all students
Search for a student by name
Delete a student
Exit the program
'''

# Initialize an empty list to store students
students = []

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    students.append({'name': name, 'roll_no': roll_no})
    print(f"Student {name} added successfully!\n")

# Function to view all students
def view_students():
    if students:
        print("\n--- List of Students ---")
        for student in students:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}")
    else:
        print("\nNo students found.\n")

# Function to search for a student
def search_student():
    search_name = input("Enter name to search: ")
    found = False
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"Student Found: Name: {student['name']}, Roll No: {student['roll_no']}")
            found = True
            break
    if not found:
        print("Student not found.\n")

# Function to delete a student
def delete_student():
    delete_name = input("Enter name to delete: ")
    for student in students:
        if student['name'].lower() == delete_name.lower():
            students.remove(student)
            print(f"Student {delete_name} deleted successfully!\n")
            return
    print("Student not found.\n")

# Main menu function
def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main menu to start the program
menu()
