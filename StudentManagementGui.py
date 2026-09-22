import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

# Student list
students = []


# Add student
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    branch = branch_entry.get()

    if name == "" or roll == "" or branch == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    students.append({
        "name": name,
        "roll": roll,
        "branch": branch
    })

    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()
    display_students()


# Display students
def display_students():
    listbox.delete(0, tk.END)

    for student in students:
        data = f"Roll: {student['roll']} | Name: {student['name']} | Branch: {student['branch']}"
        listbox.insert(tk.END, data)


# Search student
def search_student():
    roll = roll_entry.get()

    for student in students:
        if student["roll"] == roll:
            messagebox.showinfo(
                "Student Found",
                f"Name: {student['name']}\n"
                f"Roll: {student['roll']}\n"
                f"Branch: {student['branch']}"
            )
            return

    messagebox.showerror("Not Found", "Student not found")


# Delete student
def delete_student():
    roll = roll_entry.get()

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            messagebox.showinfo("Success", "Student deleted")
            clear_fields()
            display_students()
            return

    messagebox.showerror("Error", "Student not found")


# Clear fields
def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)


# Title
title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# Name
tk.Label(root, text="Student Name:", font=("Arial", 12)).pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)


# Roll number
tk.Label(root, text="Roll Number:", font=("Arial", 12)).pack()
roll_entry = tk.Entry(root, width=40)
roll_entry.pack(pady=5)


# Branch
tk.Label(root, text="Branch:", font=("Arial", 12)).pack()
branch_entry = tk.Entry(root, width=40)
branch_entry.pack(pady=5)


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add Student",
    command=add_student,
    width=12
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="View Students",
    command=display_students,
    width=12
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Search",
    command=search_student,
    width=12
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Delete",
    command=delete_student,
    width=12
).grid(row=0, column=3, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=12
).grid(row=0, column=4, padx=5)


# Student list
tk.Label(
    root,
    text="Student Records",
    font=("Arial", 14, "bold")
).pack(pady=10)

listbox = tk.Listbox(root, width=75, height=10)
listbox.pack()


# Start application
root.mainloop()