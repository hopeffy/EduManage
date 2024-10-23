import csv

from student import Student


class StudentList:  # StudentList class

    # Constructor to create new student list
    def __init__(self):
        self.student_list = []

    # create student and append student list
    def add_student(self, student):
        self.student_list.append(student)

    # delete student with tck no
    def remove_student_with_tck_no(self, tckNo):
        for student in self.student_list:
            if student.tck_no == tckNo:
                self.student_list.remove(student)

    # delete student with name and surname
    def remove_student_with_name_and_surname(self, name_surname):
        for student in self.student_list:
            if student.name_surname == name_surname:
                self.student_list.remove(student)

    # display all Student object from student_list
    def display(self):
        if not self.student_list:
            print("No students in the list.")
        else:
            for student in self.student_list:
                print(student.person)

    def save_students_to_csv(self, filename='students.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['TCK', 'Name and Surname', 'Role'])
            for student in self.student_list:
                csv_writer.writerow([student.tck_no, student.name_surname, student.role])
        print(f'Lecturers saved to {filename}')

    def find_by_tck(self, student_tck):
        for student in self.student_list:
            if student.tck_no == student_tck:
                return student
            else:
                return




