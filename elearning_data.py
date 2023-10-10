import csv

# Load data from CSV into a list of dictionaries
def load_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Save updated data back to the CSV file
def save_data(data, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Function to calculate the average score for students
def calculate_average_score(data):
    total_score = 0
    student_count = 0

    for row in data:
        if row["Role"] == "Student" and row["Score"]:
            total_score += int(row["Score"])
            student_count += 1

    if student_count > 0:
        average_score = total_score / student_count
        return f"Average score for students: {average_score:.2f}"
    else:
        return "No student data available."

# Function to list teachers and the subjects they teach
def list_teachers_and_subjects(data):
    teachers_subjects = {}

    for row in data:
        if row["Role"] == "Teacher":
            if row["Name"] not in teachers_subjects:
                teachers_subjects[row["Name"]] = []
            teachers_subjects[row["Name"]].append(row["Subject"])

    report = "Teachers and their subjects:\n"
    for teacher, subjects in teachers_subjects.items():
        report += f"{teacher}: {', '.join(subjects)}\n"

    return report

# Function to search for a specific student or teacher by name
def search_by_name(data, name):
    results = []

    for row in data:
        if row["Name"].lower() == name.lower():
            results.append(row)

    return results

# Function to update a student's score
def update_student_score(data, student_name, new_score):
    for row in data:
        if row["Role"] == "Student" and row["Name"].lower() == student_name.lower():
            if new_score.isdigit():
                row["Score"] = int(new_score)
                return True
            else:
                return False
    return False

# Specify the file path for your elearning_data.csv file
filename = "elearning_data.csv"

# Load the data from the CSV file
data_list = load_data(filename)

# Interactive menu
while True:
    print("\nChoose an option:")
    print("1. Calculate average score for students")
    print("2. List teachers and their subjects")
    print("3. Search for a student or teacher by name")
    print("4. Update a student's score")
    print("5. Save and exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(calculate_average_score(data_list))
    elif choice == "2":
        report = list_teachers_and_subjects(data_list)
        print(report)
    elif choice == "3":
        search_name = input("Enter the name to search for: ")
        results = search_by_name(data_list, search_name)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No matching records found.")
    elif choice == "4":
        student_name = input("Enter the student's name to update score: ")
        new_score = input("Enter the new score: ")
        if update_student_score(data_list, student_name, new_score):
            print(f"Updated score for {student_name}.")
        else:
            print("Invalid input or student not found.")
    elif choice == "5":
        save_data(data_list, filename)
        print("Data saved. Exiting.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
