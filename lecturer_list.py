import csv

from lecturer import Lecturer


class LecturerList:
    def __init__(self):
        self.lecturer_list = []

    def add_lecturer(self, lecturer_tck, lecturer_name_surname):
        """
            create lecturer_f and append lecturer_f list
        :param lecturer_tck:
        :param lecturer_name_surname:
        :return:
        """
        for lecturer in self.lecturer_list:
            if lecturer.tck_no == lecturer_tck:
                print(f"Lecturer with TCK {lecturer_tck} already exists.")
                return
        lecturer = Lecturer(lecturer_tck, lecturer_name_surname)
        self.lecturer_list.append(lecturer)
        print(f"Lecturer {lecturer_name_surname} added.")

    def remove_lecturer_tck_no(self, tckNo):
        """
        delete lecturer_f with tck no
        :param tckNo: lecturer tckNo
        :return:
        """
        for lecturer in self.lecturer_list:
            if lecturer.tck_no == tckNo:
                self.lecturer_list.remove(lecturer)
                print(f"Lecturer with TCK {tckNo} removed.")
                return
        print(f"No lecturer found with TCK {tckNo}.")


    def remove_lecturer_name_and_surname(self, name_surname):
        """
            delete lecturer_f with name and surname
        :param name_surname: lecturer name, surname
        :return:
        """
        for lecturer in self.lecturer_list:
            if lecturer.name_surname == name_surname:
                self.lecturer_list.remove(lecturer)
                print(f"Lecturer {name_surname} removed.")
                return
        print(f"No lecturer found with name {name_surname}.")


    def display(self):
        """
            display all Student object from student_list
        :return: list of Lecturer object
        """
        if not self.lecturer_list:
            print("No lecturer_f in the list.")
        else:
            for lecturer in self.lecturer_list:
                print(lecturer.person)

    def save_lecturers_to_csv(self, filename='lecturers.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['TCK', 'Name and Surname', 'Role'])
            for lecturer in self.lecturer_list:
                csv_writer.writerow([lecturer.tck_no, lecturer.name_surname, lecturer.role])
        print(f'Lecturers saved to {filename}')

    def find_by_tck(self, lecturer_tck):
        for lecturer in self.lecturer_list:
            if lecturer.tck_no == lecturer_tck:
                return lecturer
            else:
                print(f"No lecturer found with TCK {lecturer_tck}.")

    def get_name_by_tck(self, lecturer):
        for temp_lecturer in self.lecturer_list:
            if temp_lecturer == lecturer:
                return lecturer
            else:
                return


