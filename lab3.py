# Function to add a student to the dictionary
def add_student(student_dict):
    id_no = input("Enter ID Number: ")
    try:
        student_dict[id_no]
        print("Student ID already exists!")
        return
    except KeyError:
        name = input("Enter Name: ")
        grades = input("Enter Grades: ")
        while int(grades) < 0 or int(grades) > 100:
            grades = input("Grades should be between 0 and 100! Enter again: ")
        student_dict[id_no] = {'name': name, 'grade': grades}
        print("Student added successfully!")


# Function to display all student details
def display_all_students(student_dict):
    for id_no, details in student_dict.items():
        print("ID Number:", id_no)
        print("Name:", details['name'])
        print("Grades:", details['grade'])
        print()  # Add a line break after each student


# Function to access and display student details based on ID
def access_student_details(student_dict):
    id_no = input("Enter ID Number: ")
    if id_no in student_dict:
        print("ID Number:", id_no)
        print("Name:", student_dict[id_no]['name'])
        print("Grades:", student_dict[id_no]['grade'])
    else:
        print("Student not found!")


# Function to update student details based on ID
def update_student_details(student_dict):
    id_no = input("Enter ID Number: ")
    if id_no in student_dict:
        print("Update Student Details for ID Number", id_no)
        grades = input("Enter New Grades: ")
        if int(grades) < 0 or int(grades) > 100:
            print("Grades should be between 0 and 100!")
            return
        student_dict[id_no]['grade'] = grades
        print("Student details updated successfully!")
    else:
        print("Student not found!")


# Function to remove a student from the dictionary based on ID
def remove_student(student_dict):
    id_no = input("Enter ID Number: ")
    if id_no in student_dict:
        del student_dict[id_no]
        print("Student removed successfully!")
    else:
        print("Student not found!")


# Function to check if particular information is available in the student dictionary
def check_info(student_dict):
    check_att = input("Enter the key information regarding a student: ")
    if check_att in student_dict:
        print(check_att, "is present")
    else:
        print(check_att, "is not present")


# Function to retrieve the number of students enrolled in the course
def number_students(student_dict):
    count = len(student_dict)
    print("The number of students enrolled is", count)


# Function to iterate over the student dictionary and display all details
def iterate_student(student_dict):
    for key, value in student_dict.items():
        print(key, ":", value)


# Function to print all the keys of the student dictionary
def getting_keys(student_dict):
    print("The properties of the student: \n")
    keys = student_dict.keys()
    for key in keys:
        print(key)


# Function to print all the values of the student dictionary
def getting_values(student_dict):
    print("The details of the student: \n")
    values = student_dict.values()
    for value in values:
        print(value)


# Function to clear the student dictionary
def clear_student(student_dict):
    student_dict.clear()
    print("Student dictionary cleared successfully!")


# Function to create a copy of the student dictionary
def copy_student_dict(student_dict):
    student_copy = student_dict.copy()
    print("The copy of the student dictionary is", student_copy)


# Function to merge another student dictionary with the existing dictionary
def merge_student(student_dict):
    student1 = {}
    id_no1 = input("Enter ID Number: ")
    name1 = input("Enter Name: ")
    grades1 = input("Enter Grades: ")
    while int(grades1) < 0 or int(grades1) > 100:
        grades1 = input("Grades should be between 0 and 100! Enter again: ")
    if id_no1 in student_dict:
        print("Student ID already exists!")
        return
    student1[id_no1] = {'name': name1, 'grade': grades1}
    student_dict.update(student1)
    print("Student updated successfully!")


# Function to check if a particular student is present in the dictionary
def check_by_name(student_dict):
    check_att = input("Enter the student name to check if he/she has enrolled in the course: ")
    for details in student_dict.values():
        if details['name'] == check_att:
            print(check_att, "is present")
            return
    print(check_att, "is not present")


# Function to sort the student dictionary based on keys
def sort_dict(student_dict):
    sorted_keys = (sorted(student_dict))
    print("The sorted student dictionary is", sorted_keys)


# Function to find the minimum and maximum grades among the students
def minmax_dict(student_dict):
    grades = [student['grade'] for student in student_dict.values()]
    minimum = min(grades)
    maximum = max(grades)
    student_min = None
    student_max = None

    for id_no, details in student_dict.items():
        if details['grade'] == minimum:
            student_min = details['name']
        if details['grade'] == maximum:
            student_max = details['name']

    print('Minimum Grade:', minimum, "of student", student_min)
    print('Maximum Grade:', maximum, "of student", student_max)


student = {}  # Creating an empty Dictionary

while True:
    print("******* DICTIONARY OPERATIONS *******")
    print("1. Enroll a Student and Add them")
    print("2. Display Student Details")
    print("3. Access Student Details using ID")
    print("4. Update Student Grades")
    print("5. Remove Student from the Course")
    print("6. Check Availability of Student Information")
    print("7. Retrieve the Number of Enrolled Students")
    print("8. Iterate Over Students and Their Details")
    print("9. Get the Keys of the Student Dictionary")
    print("10. Get the Values of the Student Dictionary")
    print("11. Clear the Student Dictionary")
    print("12. Copy the Student Dictionary")
    print("13. Merge the Student Dictionary with Additional Attributes")
    print("14. Check if a Specific Student is Enrolled")
    print("15. Sort the Student Dictionary")
    print("16. Find Minimum and Maximum Grades")
    print("17. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student(student)
    elif choice == '2':
        display_all_students(student)
    elif choice == '3':
        access_student_details(student)
    elif choice == '4':
        update_student_details(student)
    elif choice == '5':
        remove_student(student)
    elif choice == '6':
        check_info(student)
    elif choice == '7':
        number_students(student)
    elif choice == '8':
        iterate_student(student)
    elif choice == '9':
        getting_keys(student)
    elif choice == '10':
        getting_values(student)
    elif choice == '11':
        clear_student(student)
    elif choice == '12':
        copy_student_dict(student)
    elif choice == '13':
        merge_student(student)
    elif choice == '14':
        check_by_name(student)
    elif choice == '15':
        sort_dict(student)
    elif choice == '16':
        minmax_dict(student)
    elif choice == '17':
        break
    else:
        print("Invalid choice! Please try again.")

print("Thank you for using the Dictionary program!")
