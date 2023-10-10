import re

def get_student_courses(data):

    # Define a regular expression pattern to match student names and their courses
    pattern = r'\s*(?P<student_name>\w+):\s*(?P<courses>[\w, ]+)'

    # Find all matches in the data using the pattern
    match = re.search(pattern, data)

    # Create a dictionary to store student-course mappings
    student_courses = {}

    if match:

        # Use the `groupdict()` method to extract the student name and the courses
        student_name = match.groupdict()['student_name']
        courses = match.groupdict()['courses']

        # Remove any spaces from the courses list
        courses = courses.split(',')
        courses = [course.strip() for course in courses]

        student_courses[student_name] = courses

    return student_courses


def main():

    while True:

        # Get the data from the user
        data = input("Enter the student data (or 'q' to quit): ")

        if data.lower() == 'q':
            break

        # Basic input validation
        if re.match(r'^\s*\w+:\s*[\w, ]+\s*$', data):

            # Get the student-course mappings
            student_courses = get_student_courses(data)

            valid = True  # Assume all students have at least one course

            # Validate the number of courses
            for student, courses in student_courses.items():
                if len(courses) < 1:
                    print(f"At least one course must be specified for {student}.")
                    valid = False
                    break

            if valid:

                # Print the extracted student-course mappings
                for student, courses in student_courses.items():
                    course_list = ', '.join(courses)
                    print(f"{student} is registered for courses: {course_list}")

            else:
                print("Invalid input format. Please follow the correct format or enter 'q' to quit.")

        else:
            print("Invalid input format. Please follow the correct format or enter 'q' to quit.")


if __name__ == "__main__":
    main()
