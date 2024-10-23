import student_list
from student import Student


class Lecture:

    # Constructor to create new lecture
    def __init__(self, lecture_code, lecture_title, lecturer_tck):
        self.lecture = {
            'code': lecture_code,
            'title': lecture_title,
            'lecturer': lecturer_tck,
            'studentList': student_list.StudentList()  # Initialize an empty StudentList object !!!
        }

    @property
    def code(self):
        return self.lecture['code']

    @code.setter
    def code(self, value):
        self.lecture['code'] = value

    @property
    def title(self):
        return self.lecture['title']

    @title.setter
    def title(self, value):
        self.lecture['title'] = value

    @property
    def lecturer(self):
        return self.lecture['lecturer']

    @lecturer.setter
    def lecturer(self, value):
        self.lecture['lecturer'] = value

    @property
    def studentList(self):
        return self.lecture['lecturer']

    @studentList.setter
    def studentList(self, value):
        self.lecture['studentList'] = value

    def add_student(self, student):
        """
        Adds a student to the lecture's student list.
        Ensures that only Student objects can be added.
        """
        if isinstance(student, Student):
            if student not in self.lecture['studentList']:
                self.lecture['studentList'].add_student(student)
            else:
                print(f"Student {student.name_surname} is already enrolled in this lecture.")
        else:
            print("Only students can be added to the student list.")

    def display_students(self):
        """
        Displays all students enrolled in the lecture.
        """
        if not self.lecture['studentList'].student_list:
            print("No students enrolled in this lecture.")
        else:
            for student in self.lecture['studentList'].student_list:
                print(f"Student TCK: {student.tck_no}, Name: {student.name_surname}")
