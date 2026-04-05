students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print()

def search_student():
    name = input("Enter student name to search: ")
    
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found: Name: {student['name']}, Age: {student['age']}, Course: {student['course']}\n")
            return
    
    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
