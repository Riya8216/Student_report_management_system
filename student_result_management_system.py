from tkinter import *

# Function to calculate total, average and grade
def calculate():
    name = name_entry.get()
    password = pass_entry.get()
    try:
        m1 = int(m1_entry.get())
        m2 = int(m2_entry.get())
        m3 = int(m3_entry.get())

        # Validation
        if not name or not password:
            result_label.config(text="Please enter name and password!", fg="red")
            return
        if any(m < 0 or m > 100 for m in [m1, m2, m3]):
            result_label.config(text="Marks should be between 0 and 100!", fg="red")
            return

        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 90:
            grade = "A+"
            color = "green"
        elif avg >= 75:
            grade = "A"
            color = "blue"
        elif avg >= 60:
            grade = "B"
            color = "orange"
        elif avg >= 50:
            grade = "C"
            color = "purple"
        else:
            grade = "F"
            color = "red"

        result_label.config(
            text=f"Name: {name}\nTotal: {total}\nAverage: {avg:.2f}\nGrade: {grade}",
            fg=color
        )
    except ValueError:
        result_label.config(text="Please enter valid numeric marks!", fg="red")

# GUI Window
root = Tk()
root.title("Student Result System")
root.geometry("420x450")
root.configure(bg="#e6f2ff")  # Light blue background

# Title Label
Label(
    root,
    text="🎓 Student Result Management 🎓",
    font=("Arial", 16, "bold"),
    bg="#007acc",
    fg="white",
    pady=10
).pack(fill=X)

# Name
Label(root, text="Name:", font=("Arial", 12, "bold"), bg="#e6f2ff").pack(pady=5)
name_entry = Entry(root, width=30)
name_entry.pack()

# Password
Label(root, text="Password:", font=("Arial", 12, "bold"), bg="#e6f2ff").pack(pady=5)
pass_entry = Entry(root, show="*", width=30)
pass_entry.pack()

# Marks Input
Label(root, text="Enter Marks for 3 Subjects:", font=("Arial", 12, "bold"), bg="#e6f2ff").pack(pady=10)
m1_entry = Entry(root, width=10)
m1_entry.pack(pady=2)
m2_entry = Entry(root, width=10)
m2_entry.pack(pady=2)
m3_entry = Entry(root, width=10)
m3_entry.pack(pady=2)

# Button
Button(
    root,
    text="Calculate Result",
    command=calculate,
    bg="#007acc",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18,
    relief=GROOVE
).pack(pady=15)

# Result Display
result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#e6f2ff")
result_label.pack(pady=10)

# Footer
Label(
    root,
    text="Created by Riya Kashyap 💫",
    bg="#007acc",
    fg="white",
    font=("Arial", 10, "italic")
).pack(side=BOTTOM, fill=X, pady=5)

root.mainloop()