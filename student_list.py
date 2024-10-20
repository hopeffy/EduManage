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



