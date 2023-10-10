import time
class lab4:
    def __init__(self): #a special method that gets called when you create an object of a class.
        self.course_progress = []

    def get_time_of_day(self):
        current_time = time.localtime().tm_hour
        if 5 <= current_time < 12:
            return "morning"
        elif 12 <= current_time < 17:
            return "afternoon"
        elif 17 <= current_time < 20:
            return "evening"
        else:
            return "night"

    def display_welcome_message(self):
        time_of_day = self.get_time_of_day()
        print(f"Good {time_of_day}, and Welcome to the E-Learning Platform!")

    def get_user_input(self):
        name = input("Enter your name: ")
        print(f"Hello, {name.capitalize()}!")

    def check_courses(self):
        available_courses = ["Mathematics", "History", "Science", "English", "Programming"]
        print("Available Courses:")
        for course in available_courses:
            print(f"- {course}")

    def enroll_in_course(self):
        available_courses = ["Mathematics", "History", "Science", "English", "Programming"]
        while True:
            course = input("Enter the name of the course you want to enroll in: ")
            if course in available_courses:
                print(f"You have successfully enrolled in the course '{course}'!")
                self.course_progress.append(course)
                return course
            else:
                print("Invalid course name. Please enter a valid course name from the list.")

    def show_progress(self):
        if not self.course_progress:
            print("No courses completed yet.")
        else:
            print("Completed Courses:")
            for course in self.course_progress:
                print(f"- {course}")
            print(f"Total completed courses: {len(self.course_progress)}")

    def check_alphanumeric(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' alphanumeric? {string.isalnum()}")

    def check_alpha(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' alphabetic? {string.isalpha()}")

    def check_lower_case(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' in lowercase? {string.islower()}")

    def check_space(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' consisting of only spaces? {string.isspace()}")

    def check_title_case(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' in title case? {string.istitle()}")

    def check_upper_case(self):
        string = input("Enter a string: ")
        print(f"Is '{string}' in uppercase? {string.isupper()}")

    def convert_to_lower_case(self):
        sentence = input("Enter a sentence: ")
        print(sentence.lower())

    def remove_whitespace(self):
        string = input("Enter a string: ")
        print(string.strip())

    def replace_word(self):
        sentence = input("Enter a sentence: ")
        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")
        new_sentence = sentence.replace(old_word, new_word)
        print(new_sentence)

    def display_menu(self):
        print("===== E-Learning Platform Menu =====")
        print("1. Get User Name")
        print("2. Check Available Courses")
        print("3. Enroll in a Course")
        print("4. Show Progress")
        print("5. Check Alphanumeric")
        print("6. Check Alphabetic")
        print("7. Check Lowercase")
        print("8. Check Whitespace")
        print("9. Check Title Case")
        print("10. Check Uppercase")
        print("11. Convert to Lowercase")
        print("12. Remove Whitespace")
        print("13. Replace Word in Sentence")
        print("14. Display Menu")
        print("0. Exit")

    def get_valid_choice(self):
        while True:
            choice = input("Enter your choice (0-14): ")
            if choice.isdigit() and 0 <= int(choice) <= 14:
                return int(choice)
            print("Invalid choice. Please enter a number between 0 and 14.")

    def main(self):
        self.display_welcome_message()
        while True:
            self.display_menu()
            choice = self.get_valid_choice()
            if choice == 1:
                self.get_user_input()
            elif choice == 2:
                self.check_courses()
            elif choice == 3:
                self.enroll_in_course()
            elif choice == 4:
                self.show_progress()
            elif choice == 5:
                self.check_alphanumeric()
            elif choice == 6:
                self.check_alpha()
            elif choice == 7:
                self.check_lower_case()
            elif choice == 8:
                self.check_space()
            elif choice == 9:
                self.check_title_case()
            elif choice == 10:
                self.check_upper_case()
            elif choice == 11:
                self.convert_to_lower_case()
            elif choice == 12:
                self.remove_whitespace()
            elif choice == 13:
                self.replace_word()
            elif choice == 14:
                time.sleep(1)  # Simulate thinking before displaying the menu again
                continue
            elif choice == 0:
                print("Exiting the E-Learning Platform. Goodbye!")
                break


if __name__ == "__main__":
    platform = lab4()
    platform.main()
