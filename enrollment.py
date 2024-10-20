from lecture import Lecture
from student import Student


class Enrollment:
    def __init__(self, student, lecture):
        self.enrollment = {
            'student': student,
            'lecture': lecture
        }
        self.enrollment_list = []

    def enroll_student(self, student, lecture):
        if isinstance(student, Student):
            temp_enrollment = Enrollment(student, lecture)
            self.enrollment_list.append(temp_enrollment)
        else:
            print("not a student")

    def remove_enrollment(self, student):
        if isinstance(student, Student):
            for enrollment in self.enrollment_list:
                if enrollment.student == student:
                    self.enrollment_list.remove(enrollment)

