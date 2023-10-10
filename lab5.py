class SelectionSort:
    def set_data(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j]['grade'] < self.data[min_index]['grade']:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def display(self):
        for student in self.data:
            print(f"Name: {student['name']}, Course: {student['course']}, Grade: {student['grade']}")


class IntegerSelectionSort(SelectionSort):
    def set_data(self, data):
        if all(isinstance(item['grade'], int) for item in data):
            super().set_data(data)
        else:
            raise ValueError("This class is designed for sorting student data with integer grades only.")


# Example usage:
def main():
    student_data = []

    # Get the number of students
    num_students = 0
    while num_students < 2:
        num_students = int(input("Enter the number of students: "))
        if num_students < 2:
            print("Please try again since the number of students should be atleast 2.")

    course = None
    while True:
        for i in range(num_students):
            name = input("Enter student name: ")
            if course is None:
                while True:
                    course = input("Enter course name: ")
                    if course.isalpha():
                        break
                    else:
                        print("Course name must not contain numbers.")
            else:
                new_course = input("Enter course name (or press Enter to use the previous course): ")
                while new_course and not new_course.isalpha():
                    print("Course name must not contain numbers.")
                    new_course = input("Enter course name (or press Enter to use the previous course): ")
                if new_course:
                    course = new_course
            grade = int(input("Enter student grade: "))
            student_data.append({'name': name, 'course': course, 'grade': grade})

        # Validate the number of students
        if len(student_data) < 2:
            print("There should be at least two students.")
            student_data.clear()
            continue

        # Using IntegerSelectionSort with inheritance
        int_sorter = IntegerSelectionSort()
        try:
            int_sorter.set_data(student_data)
            int_sorter.sort()
            print("Sorted student data by grade:")
            int_sorter.display()
            break
        except ValueError as e:
            print(e)
            student_data.clear()

if __name__ == "__main__":
    main()