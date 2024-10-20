from person import Person


class Student(Person):  # Student class

    # Constructor to create new student
    def __init__(self, tck_no, name_surname):
        role = "student"
        super().__init__(tck_no, name_surname, role)
