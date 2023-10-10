from abc import abstractmethod, ABC


class AbstractStudentAdmissionStack(ABC):
    def __init__(self):
        self.applications = []

    @abstractmethod
    def push(self, application):
        pass

    @abstractmethod
    def pop(self):
        pass

    def peek(self):
        if not self.is_empty():
            return self.applications[-1]
        else:
            return None

    def is_empty(self):
        return len(self.applications) == 0

    def size(self):
        return len(self.applications)


class RegularAdmissionStack(AbstractStudentAdmissionStack):
    def push(self, application):
        self.applications.append(application)

    def pop(self):
        if not self.is_empty():
            return self.applications.pop()
        else:
            print("Regular Admission Stack is empty.")
            return None


class EarlyDecisionStack(AbstractStudentAdmissionStack):
    def push(self, application):
        self.applications.append(application)

    def pop(self):
        if not self.is_empty():
            return self.applications.pop()
        else:
            print("Early Decision Admission Stack is empty.")
            return None


def validate_application(application):
    return "regular" in application.lower() or "early decision" in application.lower()
# only applications that are either regular or early decision can be added to a student admission stack.

def create_stack(stack_type):
    if stack_type == 1:
        return RegularAdmissionStack()
    elif stack_type == 2:
        return EarlyDecisionStack()
    else:
        return None


admission_stack = RegularAdmissionStack()  # Set to RegularAdmissionStack by default

admission_options = {
    "regular": ["Computer Science", "Biology", "Economics", "Psychology"],
    "early decision": ["Chemistry", "History", "Mathematics", "Sociology"]
}

while True:
    num_applications = int(input("Enter the number of applications to process (at least 2): "))
    if num_applications >= 2:
        break
    else:
        print("Please enter at least 2 applications.")

previous_application = ""
unique_applications = set()

for i in range(num_applications):
    if i == 0:
        application = input("Enter application description: ")
    else:
        application = input(f"Enter application description (press Enter to use previous application: '{previous_application}'): ")

    if not application:
        application = previous_application
    else:
        while not validate_application(application):
            print("Invalid application description. Please enter a valid application (regular or early decision).")
            application = input("Enter application description: ")

    application_type = "regular" if "regular" in application.lower() else "early decision"
    application_option_list = admission_options.get(application_type)

    print(f"{application_type.capitalize()} Admission Options:")
    for idx, option in enumerate(application_option_list, start=1):
        print(f"{idx}. {option}")

    while True:
        try:
            chosen_option = int(input(f"Enter the chosen {application_type} application number (1-{len(application_option_list)}): "))
            if 1 <= chosen_option <= len(application_option_list):
                application = f"{application_type.capitalize()} Admission: {application_option_list[chosen_option - 1]}"
                break
            else:
                print(f"Invalid {application_type} application option.")
        except ValueError:
            print("Invalid input. Please enter a valid integer choice.")

    admission_stack.push(application)
    unique_applications.add(application)
    previous_application = application

while True:
    print("Admission Options:")
    print("1. Peek at Last Application")
    print("2. Pop an Application")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        last_application = admission_stack.peek()
        if last_application:
            print("Last Application:", last_application)
        else:
            print("No applications in the stack.")
    elif choice == "2":
        if not admission_stack.is_empty():
            pop_choice = input("Do you want to pop an application? (yes/no): ")
            if pop_choice.lower() == "yes":
                admitted_application = admission_stack.pop()
                print("Student admitted with application:", admitted_application)
        else:
            print("No applications in the stack.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Unique Application Count:", len(unique_applications))
print("Final Stack Size:", admission_stack.size())
