def main():
    while True:
        choice = choose()
        menu = {
            "1": create_list,
            "2": create_tuple,
            "3": create_list_of_tuples,
            "4": create_tuple_of_lists,
            "5": type_conversion,
            "6": inbuilt_operations,
            "7": exit_program,
        }
        if choice in menu:
            menu[choice]()
        else:
            print("Oops! Wrong Choice")

        if not continue_program():
            break


def choose():
    print("Welcome to the menu-driven program!")
    print("1. Create list of e-learning courses")
    print("2. Create Tuples of e-learning courses")
    print("3. Create list of Tuples of students with grades")
    print("4. Create Tuple of lists of students with grades")
    print("5. Type Conversion from List to Tuple/from Tuple to list/from String to Tuple/from String to list")
    print("6. Try Built-in Functions of marks of students")
    print("7. Exit")

    return input("Enter your choice: ")


def create_list():
    print("You have chosen CREATION OF LIST")
    list_courses = list_courses_fn()
    print("The list of e-learning courses is", list_courses)


def create_tuple():
    print("You have chosen CREATION OF TUPLE")
    tuple_courses = tuple_courses_fn()
    print("The tuple of e-learning courses is", tuple_courses)


def list_courses_fn():
    list_courses = []
    while True:
        try:
            n = int(input("Enter the number of courses: "))
            if n <= 0:
                print("Number of courses must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for _ in range(n):
        name = input("Enter the name of the e-learning course: ")
        instructor = input("Enter the name of the instructor: ")
        price = input("Enter the price of the course: ")
        list_courses.append((name, instructor, price))

    return list_courses


def tuple_courses_fn():
    tuple_courses = []
    while True:
        try:
            tuple_items = int(input("Enter the number of courses: "))
            if tuple_items <= 0:
                print("Number of courses must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for _ in range(tuple_items):
        name = input("Enter the name of the course: ")
        tuple_courses.append(name)

    tuple1 = tuple(tuple_courses)
    return tuple1


def create_list_of_tuples():
    print("You have chosen CREATION LIST OF TUPLES")
    list_of_tuples = []
    for _ in range(1):
        tuple_elements = []
        n = int(input("Enter the number of students to be added: "))
        for i in range(n):
            while True:
                try:
                    student_id = int(input("Enter the student ID: "))
                    grade = int(input("Enter the grade: "))
                    if 60 <= grade <= 100:
                        tuple_elements.append((grade, student_id))
                        break
                    else:
                        print("Grade should be between 60 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        if tuple_elements:
            list_of_tuples.append(tuple(tuple_elements))
    print("The list of tuples is:", list_of_tuples)


def create_tuple_of_lists():
    print("You have chosen CREATION TUPLE OF LIST")
    tuple_of_lists = []
    for _ in range(1):
        list_elements = []
        n = int(input("Enter the number of students to be added: "))
        for i in range(n):
            while True:
                try:
                    student_id = int(input("Enter the student ID: "))
                    grade = int(input("Enter the grade: "))
                    if 60 <= grade <= 100:
                        list_elements.append((grade, student_id))
                        break
                    else:
                        print("Grade should be between 60 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        if list_elements:
            tuple_of_lists.append(list(list_elements))
    print("The list of tuples is:", tuple(tuple_of_lists))


def type_conversion():
    data = input("Enter the data: ")
    converted_data = None

    choice = input("Choose the type of conversion: "
                   "1. List to Tuple\n"
                   "2. Tuple to List\n"
                   "3. String to Tuple\n"
                   "4. String to List\n"
                   "Enter your choice: ")

    if choice == "1":
        converted_data = tuple(data)
    elif choice == "2":
        converted_data = list(data)
    elif choice == "3":
        converted_data = tuple([char for char in data])
    elif choice == "4":
        converted_data = list(data)
    else:
        print("Invalid choice!")

    print("The converted data is:", converted_data)


def inbuilt_operations():
    print("You have chosen TRY BUILT-IN FUNCTIONS")
    list_of_scores = []
    n = int(input("Enter the number of scores you want to input: "))
    for _ in range(n):
        score = int(input("Enter a score: "))
        list_of_scores.append(score)

    print("The length of the list is:", len(list_of_scores))
    print("The sum of all scores in the list is:", sum(list_of_scores))
    print("The maximum score in the list is:", max(list_of_scores))
    print("The minimum score in the list is:", min(list_of_scores))


def exit_program():
    print("Exiting program...")
    exit()


def continue_program():
    while True:
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() in ["yes", "no"]:
            return choice.lower() == "yes"
        print("Invalid choice! Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
