# Student Management System

students = []


# Add Student
def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


# View Students
def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("Roll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("Marks       :", student["marks"])


# Search Student
def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll Number :", student["roll_no"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Marks       :", student["marks"])
            return

    print("Student not found.")


# Update Student
def update_student():
    print("\n--- Update Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete Student
def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main Menu
while True:
    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")