# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:22:50 2024

@author: soeze
"""

def load_data(filename): #Creating function to display student list file
    with open(filename, 'r') as file: #using file read format
        num_students = int(file.readline().strip())
        students = [] #list of the students
        for line in file:
            parts = line.strip().split(',')
            student_code = int(parts[0])
            name = parts[1]
            coursework = list(map(int, parts[2:5]))
            exam_mark = int(parts[5])
            students.append((student_code, name, coursework, exam_mark))
    return num_students, students

def calculate_total(coursework):
    return sum(coursework)

def calculate_percentage(coursework, exam_mark):
    total_coursework = calculate_total(coursework)
    total = total_coursework + exam_mark
    return (total / 160) * 100

def determine_grade(percentage): 
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def display_student_record(student): #creating function to display students record
    student_code, name, coursework, exam_mark = student
    total_coursework = calculate_total(coursework)
    percentage = calculate_percentage(coursework, exam_mark)
    grade = determine_grade(percentage)
    print(f"Name: {name}")
    print(f"Number: {student_code}")
    print(f"Total coursework mark: {total_coursework}")
    print(f"Exam Mark: {exam_mark}")
    print(f"Overall percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def view_all_students(students): #creating function to view all students
    total_percentage = 0
    for student in students:
        display_student_record(student)
        print()
        total_percentage += calculate_percentage(student[2], student[3])
    average_percentage = total_percentage / len(students)
    print(f"Number of students: {len(students)}")
    print(f"Average percentage: {average_percentage:.2f}%")

def view_individual_student(students):  #creating function to view individual student
    name_or_number = input("Enter student's name or number: ")
    for student in students:
        if name_or_number.lower() in student[1].lower() or name_or_number == str(student[0]):
            display_student_record(student)
            return
    print("Student not found.")

def student_with_highest_score(students): #creating function to view student with highest score
    highest_student = max(students, key=lambda x: calculate_total(x[2]) + x[3])
    display_student_record(highest_student)

def student_with_lowest_score(students): #creating function to view students with lowest score
    lowest_student = min(students, key=lambda x: calculate_total(x[2]) + x[3])
    display_student_record(lowest_student)

def main():#running the program using while loop
    filename = "studentMarks.txt"
    num_students, students = load_data(filename)

    while True:
        print("\nMenu:")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Quit")
        
        choice = int(input("Select an option: "))
        
        if choice == 1:
            view_all_students(students)
        elif choice == 2:
            view_individual_student(students)
        elif choice == 3:
            student_with_highest_score(students)
        elif choice == 4:
            student_with_lowest_score(students)
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
