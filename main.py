import csv
import keyboard
from lecture import Lecture
from lecture_list import LectureList
from lecturer_list import LecturerList
from student import Student
from student_list import StudentList

# Utility function to save list to a CSV file
def save_to_csv_file(listA, headers, filename='lecture_list.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)
        for l in listA:
            csv_writer.writerow(l)

class MainApp:
    def __init__(self):
        self.student_list = StudentList()
        self.lecturer_list = LecturerList()
        self.lecture_list = LectureList()

        self.listen_for_shortcuts()
        self.main_menu()

    # Add a listener for Ctrl+Space to save and exit
    def listen_for_shortcuts(self):
        keyboard.add_hotkey('ctrl+space', self.save_and_exit)

    # Main menu for handling roles and actions
    def main_menu(self):
        while True:
            print("\nChoose an action:\n1 - Add Lecture\n2 - Add Lecturer to Lecture\n3 - Add Students to Lecture\n4 - Display All Lectures")
            action = input()

            if action == "1":
                self.add_lecture()
            elif action == "2":
                self.add_lecturer_to_lecture()
            elif action == "3":
                self.add_students_to_lecture()
            elif action == "4":
                self.display_lectures()
            else:
                print("Invalid choice, please try again.")

    # Add a new lecture to the list
    def add_lecture(self):
        print("Enter lecture code, title (comma-separated):")
        input_data = input().split(",")
        lecture_code, lecture_title = input_data[0], input_data[1]

        if self.lecture_list.find_by_code(lecture_code):
            print(f"Lecture {lecture_code} already exists.")
        else:
            # lecture = Lecture(lecture_code, lecture_title, None)  # Lecturer is None initially
            self.lecture_list.add_lecture(lecture_code, lecture_title, None)
            print(f"Lecture {lecture_title} added.")

    # Add a lecturer to a lecture
    def add_lecturer_to_lecture(self):
        self.display_lectures()

        print("Enter the lecture code to assign a lecturer:")
        lecture_code = input()

        lecture = self.lecture_list.find_by_code(lecture_code)
        if lecture:
            print("Enter Lecturer TCK and Name (comma-separated):")
            lecturer_data = input().split(",")
            lecturer_tck, lecturer_name = lecturer_data[0], lecturer_data[1]

            lecturer = self.lecturer_list.find_by_tck(lecturer_tck)
            if not lecturer:
                self.lecturer_list.add_lecturer(lecturer_tck, lecturer_name)
                lecturer = self.lecturer_list.find_by_tck(lecturer_tck)
                print(f"Lecturer {lecturer_name} added.")

            lecture.lecturer = lecturer.tck_no
            print(f"Lecturer {lecturer_name} assigned to {lecture.title}.")
        else:
            print(f"Lecture {lecture_code} not found.")

    # Add multiple students to a lecture
    def add_students_to_lecture(self):
        self.display_lectures()

        print("Enter the lecture code to assign students:")
        lecture_code = input()

        lecture = self.lecture_list.find_by_code(lecture_code)
        if lecture:
            print("Enter student TCK and Name (comma-separated), or 'done' to finish:")
            while True:
                student_data = input().strip()
                if student_data.lower() == 'done':
                    break
                student_tck, student_name = student_data.split(",")

                student = self.student_list.find_by_tck(student_tck)
                if not student:
                    student = Student(student_tck, student_name)
                    self.student_list.add_student(student)
                    print(f"Student {student_name} added.")

                # Ensure students are not duplicated in lecture's student list
                if student_tck not in lecture.students:
                    lecture.students.append(student_tck)
                    print(f"Student {student_name} added to {lecture.title}.")
                else:
                    print(f"Student {student_name} is already in {lecture.title}.")
        else:
            print(f"Lecture {lecture_code} not found.")

    # Display all lectures with their details
    def display_lectures(self):
        if not self.lecture_list.lecture_list:
            print("No lectures available.")
        else:
            for lecture in self.lecture_list.lecture_list:
                lecturer_name = self.lecturer_list.get_name_by_tck(lecture.lecturer)
                print(f"Lecture Code: {lecture.code}, Title: {lecture.title}, Lecturer: {lecturer_name}, Students: {lecture.display_students()}")

    # Save lectures to CSV and exit
    def save_and_exit(self):
        save_to_csv_file(self.lecture_list.lecture_list, ['code', 'title', 'lecturer_tck', 'students'], filename='lectures.csv')
        print("Lecture list saved to CSV file. Exiting.")
        exit()


# Ensure the app runs
if __name__ == "__main__":
    MainApp()
