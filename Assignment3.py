'''
Build a student grade management system using the following Python concepts:
- List of dictionaries
- Function with required arguments, *args, **kwargs
- Function decorator
- Loops and control statements

Requirements
1. Use a **decorator** to log function activity.
2. Use a function to **add student data** using `*args` and `**kwargs`.
3. Store student records in a **list of dictionaries**.
4. Use **loops and conditionals** to calculate and display results.
'''
import datetime
def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Finished: {func.__name__}\n")
        return result
    return wrapper

students = []
@log_activity
def add_student(name, roll_no, *marks, **extra_info):
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "extra_info": extra_info
    }
    students.append(student)

@log_activity
def display_student_results():
    for student in students:
        name = student["name"]
        roll_no = student["roll_no"]
        marks = student["marks"]
        total = sum(marks)
        avg = total / len(marks) if marks else 0

        if avg >= 90:
            grade = 'A+'
        elif avg >= 75:
            grade = 'A'
        elif avg >= 60:
            grade = 'B'
        elif avg >= 50:
            grade = 'C'
        else:
            grade = 'F'

        print(f"Student: {name} | Roll No: {roll_no}")
        print(f"Marks: {marks} | Total: {total} | Average: {avg:.2f} | Grade: {grade}")
        if student['extra_info']:
            print("Additional Info:", student["extra_info"])
        print("-" * 50)

add_student("Alice", 101, 95, 88, 92, city="Hyderabad", age=20)
add_student("Bob", 102, 65, 70, 72)
add_student("Charlie", 103, 45, 50, 48, city="Warangal", age=21)

display_student_results()
