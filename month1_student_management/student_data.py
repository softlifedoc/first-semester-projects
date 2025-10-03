

students = []


def add_student():
#todo: prompt the user to enter student name, age, and grade
    name= input("Enter student name: ")
    while True:
        try:
            grade = float(input("Enter student grade: "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    student= {"name": name, "grade": grade}
    students.append(student)
    print(f"{name} has been added with a grade of {grade}.")


    """
    TODO: Loop through the students list and print each student's info.
    """
    pass

def view_students():
    #todo: loop through the students list and print each student's info
    if not students:
        print("No students are registered yet.")
    else:
        print("\nstudent List:")
        for student in students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")


    """
    TODO: Return the average grade of all students.
    """
    pass

def get_average_grade():
    #todo: return the average grade of all students
    if not students:
        return 0.0
    total = sum(student['grade'] for student in students)
    return total / len(students)