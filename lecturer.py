from person import Person


class Lecturer(Person):  # Lecturer Class

    # Constructor to create new lecturer_f
    def __init__(self, tck_no, name_surname):
        role = "lecturer"
        super().__init__(tck_no, name_surname, role)



