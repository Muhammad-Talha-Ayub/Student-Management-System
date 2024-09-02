
class Student:
    def __init__(self, roll_no, name, marks, age, address, phone):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.age = age
        self.address = address
        self.phone = phone
        self.attendance = []  


def find_student_index(students, roll_no):
    for index in range(len(students)):
        if students[index].roll_no == roll_no:
            return index
    return -1


def Push(arr, top, Maxstk, item):
    if top[0] == Maxstk - 1:
        print("Stack is full")
    else:
        top[0] += 1
        arr.append(item)


def Pop(arr, index):
    if index == -1 or index >= len(arr):
        print("Index out of range or Stack is empty")
        return None
    else:
        item = arr[index]
    
        for i in range(index, len(arr) - 1):
            arr[i] = arr[i + 1]
        arr.pop() 
        return item



def delete_student(students, roll_no):
    index = find_student_index(students, roll_no)
    if index != -1:
        Pop(students, index)
        print("Student deleted successfully!")
    else:
        print("Student not found!")
    return students


def update_student(students, roll_no):
    index = find_student_index(students, roll_no)
    if index != -1:
        student = students[index]
        print("\nWhat do you want to update?")
        print("1. Roll Number")
        print("2. Name")
        print("3. Marks")
        print("4. Age")
        print("5. Address")
        print("6. Phone")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student.roll_no = int(input("Enter new Roll Number: "))
        elif choice == 2:
            student.name = input("Enter new Name: ")
        elif choice == 3:
            subjects = student.marks.keys()
            for subject in subjects:
                student.marks[subject] = int(input(f"Enter new marks for {subject}: "))
        elif choice == 4:
            student.age = int(input("Enter new Age: "))
        elif choice == 5:
            student.address = input("Enter new Address: ")
        elif choice == 6:
            student.phone = input("Enter new Phone Number: ")
        else:
            print("Invalid choice!")
        
        print("Student details updated successfully!")
    else:
        print("Student not found!")


def track_attendance(students, roll_no, date, status):
    index = find_student_index(students, roll_no)
    if index != -1:
        students[index].attendance.append((date, status))
        print("Attendance updated successfully!")
    else:
        print("Student not found!")


def display_attendance(students, roll_no):
    index = find_student_index(students, roll_no)
    if index != -1:
        student = students[index]
        print(f"Attendance for {student.name}:")
        for date, status in student.attendance:
            print(f"  Date: {date}, Status: {status}")
    else:
        print("Student not found!")


def linear_search_simple(names_array, target_name):
    i = 0
    for name in names_array:
        lower_name = name.lower()
        lower_target = target_name.lower()
        if lower_name == lower_target:
            return i
        i += 1
    return -1


def search_student_by_name(students, target_name):
    names_array = [student.name for student in students]
    index = linear_search_simple(names_array, target_name)
    if index != -1:
        return [students[index]]
    return []


def print_student_details(student):
    print(f"Roll Number: {student.roll_no}")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Address: {student.address}")
    print(f"Phone: {student.phone}")
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"  {subject}: {mark}")
    print("-------------------------")


def calculate_percentage(marks):
    total_marks = sum(marks.values())
    return (total_marks / (len(marks) * 100)) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

def detailed_report(students, roll_no=None):
    if roll_no is None:
        student_id = int(input("Enter Roll Number to show detailed report: "))
    else:
        student_id = roll_no

    index = find_student_index(students, student_id)
    if index != -1:
        print("\nStudent Found:")
        print_student_details(students[index])
        percentage = calculate_percentage(students[index].marks)
        grade = calculate_grade(percentage)
        print(f"Percentage: {percentage}%")
        print(f"Grade: {grade}")
    else:
        print("Student not found!")


# def selection_sort_students(students, key):
    # for i in range(len(students) - 1):
    #     min_index = i
    #     current = students.head
    #     for j in range(i + 1, len(students)):
    #         if key == 'roll_no':
    #             if current.student.roll_no < students[min_index].student.roll_no:
    #                 min_index = j
    #         elif key == 'name':
    #             if current.student.name < students[min_index].student.name:
    #                 min_index = j
    #         current = current.next
    #     if i != min_index:
    #         current = students.head
    #         for _ in range(min_index):
    #             current = current.next
    #         students[i].student, current.student = current.student, students[i].student
    # return students

def selection_sort_students(students, key):
    for i in range(len(students) - 1):
        min_index = i
        for j in range(i + 1, len(students)):
            if getattr(students[j], key) < getattr(students[min_index], key):
                min_index = j
        if i != min_index:
            students[i], students[min_index] = students[min_index], students[i]
    return students


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j].name > arr[j + 1].name:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

import os
from linked_list import UserBST, StudentBST


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


teacher_system = UserBST()
student_system = StudentBST()


MAX_STUDENTS = 100
students = []
top = [-1]

def student_management_system():
    global students, top
    while True:
        clear_console()
        print("\n-------- Student Management System --------\n")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by Roll Number")
        print("4. Search Student by Name")
        print("5. Detailed Report")
        print("6. Delete Student")
        print("7. Sort Students")
        print("8. Update Student")
        print("9. Track Attendance")
        print("10. Display Attendance")
        print("11. Logout")
        print("\nEnter your choice: ", end="")
        choice = int(input())

        if choice == 1:
            # Add Student
            if len(students) == MAX_STUDENTS:
                print("Error: Maximum number of students reached!")
            else:
                roll_no = int(input("Enter Roll Number: "))
                if find_student_index(students, roll_no) != -1:
                    print("Error: Student with this Roll Number already exists!")
                else:
                    name = input("Enter Name: ")
                    age = int(input("Enter Age: "))
                    address = input("Enter Address: ")
                    phone = input("Enter Phone Number: ")
                    marks = {}
                    print("Enter Marks out of 100 for each subject:")
                    subjects = [
                        "Linear Algebra",
                        "Principle of Management",
                        "Financial Accounting",
                        "Data Structures and Algorithm",
                        "Data Structures and Algorithm Lab",
                        "Software Requirement Engineering",
                        "Human Computer Interaction"
                    ]
                    for subject in subjects:
                        marks[subject] = int(input(f"{subject}: "))
                    new_student = Student(roll_no, name, marks, age, address, phone)
                    Push(students, top, MAX_STUDENTS, new_student)
                    student_system.signup(name, roll_no, phone)  
                    print("Student added successfully!")

        elif choice == 2:
            if len(students) == 0:
                print("No students found!")
            else:
                print("\nStudent List:")
                for student in students:
                    print_student_details(student)

        elif choice == 3:
            search_roll_no = int(input("Enter Roll Number to search: "))
            index = find_student_index(students, search_roll_no)
            if index != -1:
                print("\nStudent Found:")
                print_student_details(students[index])
            else:
                print("Student not found!")

        elif choice == 4:
            search_name = input("Enter name to search: ")
            matching_students = search_student_by_name(students, search_name)
            if matching_students:
                print("\nStudents Found:")
                for student in matching_students:
                    print_student_details(student)
            else:
                print("No students found with that name!")

        elif choice == 5:
            detailed_report(students)

        elif choice == 6:
            roll_no_to_delete = int(input("Enter Roll Number to delete: "))
            students = delete_student(students, roll_no_to_delete)

        elif choice == 7:
            print("Sort by:")
            print("1. Roll Number")
            print("2. Name")
            sort_choice = int(input("Enter your choice: "))
            if sort_choice == 1:
                students = selection_sort_students(students, 'roll_no')
            elif sort_choice == 2:
                students = bubble_sort(students)
            else:
                print("Invalid choice! Please enter 1 or 2.")
            print("Students sorted successfully!")

        elif choice == 8:
            roll_no_to_update = int(input("Enter Roll Number to update: "))
            update_student(students, roll_no_to_update)

        elif choice == 9:
            roll_no = int(input("Enter Roll Number: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            status = input("Enter Status (Present/Absent): ")
            track_attendance(students, roll_no, date, status)

        elif choice == 10:
            roll_no = int(input("Enter Roll Number to display attendance: "))
            display_attendance(students, roll_no)

        elif choice == 11:
            break  

        else:
            print("Invalid choice! Please enter a number between 1 and 11.")
        input("Press Enter to continue...")  

def student_portal(roll_no):
    while True:
        clear_console()
        print("\n-------- Student Portal --------\n")
        print("1. View Details")
        print("2. View Attendance")
        print("3. Logout")
        print("\nEnter your choice: ", end="")
        choice = int(input())

        if choice == 1:
            
            student = next((student for student in students if student.roll_no == roll_no), None)
            if student:
                detailed_report(students, roll_no)
            else:
                print("Student not found!")
        elif choice == 2:
            
            display_attendance(students, roll_no)
        elif choice == 3:
            
            break
        else:
            print("Invalid choice!")
        
        input("Press Enter to continue...")

def teacher_login_system():
    while True:
        clear_console()
        print("\n-------- Teacher Management --------\n")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        print("\nEnter your choice: ", end="")
        choice = int(input())

        if choice == 1:
            
            name = input("Enter Name: ")
            teacher_id = input("Enter Teacher ID: ")
            password = input("Enter Password: ")
            teacher_system.signup(name, teacher_id, password)

        elif choice == 2:
            
            teacher_id = input("Enter Teacher ID: ")
            password = input("Enter Password: ")
            if teacher_system.login(teacher_id, password):
                student_management_system()  

        elif choice == 3:
            break  

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
        input("Press Enter to continue...")  

def student_login_system():
    while True:
        clear_console()
        print("\n-------- Student Login --------\n")
        print("1. Login")
        print("2. Exit")
        print("\nEnter your choice: ", end="")
        choice = int(input())

        if choice == 1:
            # Login
            student_id = int(input("Enter Roll Number: "))  
            if find_student_index(students, student_id) != -1:
                student_portal(student_id)  
            else:
                print("Invalid Roll Number!")

        elif choice == 2:
            break  

        else:
            print("Invalid choice! Please enter 1 or 2.")
        input("Press Enter to continue...")  
# def student_login_system():
#     print("\n-------- Student Login --------\n")
#     roll_no = int(input("Enter Roll Number: "))
#     password = input("Enter Password: ")
#     if student_system.login(roll_no, password):
#         student_portal(roll_no)  # Enter the student portal
#     else:
#         print("Login failed! Incorrect roll number or password.")


if __name__ == "__main__":
    while True:
        clear_console()
        print("\n-------- Main Menu --------\n")
        print("1. Teacher")
        print("2. Student")
        print("3. Exit")
        print("\nEnter your choice: ", end="")
        choice = int(input())

        if choice == 1:
            teacher_login_system()

        elif choice == 2:
            student_login_system()

        elif choice == 3:
            print("Exiting program...")
            exit()

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
        input("Press Enter to continue...")  