from lecturer import Lecturer


class LecturerList:
    def __init__(self):
        self.lecturer_list = []

    # create lecturer_f and append lecturer_f list
    def add_lecturer(self, lecturer_tck, lecturer_name_surname):
        lecturer = Lecturer(lecturer_tck, lecturer_name_surname)
        self.lecturer_list.append(lecturer)

    # delete lecturer_f with tck no
    def remove_lecturer_tck_no(self, tckNo):
        for lecturer in self.lecturer_list:
            if lecturer.tck_no == tckNo:
                self.lecturer_list.remove(tckNo)

    # delete lecturer_f with name and surname
    def remove_lecturer_name_and_surname(self, name_surname):
        for lecturer in self.lecturer_list:
            if lecturer.name_surname == name_surname:
                self.lecturer_list.remove(name_surname)

    # display all Student object from student_list
    def display(self):
        if not self.lecturer_list:
            print("No lecturer_f in the list.")
        else:
            for lecturer in self.lecturer_list:
                print(lecturer.person)

