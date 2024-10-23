import csv

from lecture import Lecture


class LectureList:
    def __init__(self):
        self.lecture_list = []

    # create lecture and append lecture list
    def add_lecture(self, lecture_code, lecture_title, lecturer_tck):
        l = Lecture(lecture_code=lecture_code, lecture_title=lecture_title, lecturer_tck=lecturer_tck)
        self.lecture_list.append(l)

    # delete lecture with code
    def remove_lecturer_tck_no(self, code):
        for lecture in self.lecture_list:
            if lecture.code == code:
                self.lecture_list.remove(lecture)

    # delete lecture with title
    def remove_lecturer_name_and_surname(self, title):
        for lecture in self.lecture_list:
            if lecture.title == title:
                self.lecture_list.remove(title)

    # display all Student object from student_list
    def display(self):
        if not self.lecture_list:
            print("No lecturer_f in the list.")
        else:
            for l in self.lecture_list:
                print(l.lecture)

    def save_lecture_to_csv(self, filename='lecture.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['TCK', 'Name and Surname', 'Role'])
            for lecture in self.lecture_list:
                csv_writer.writerow([lecture.code, lecture.title, lecture.lecturer])
        print(f'Lecturers saved to {filename}')

    def find_by_code(self, code):
        for lecture in self.lecture_list:
            if lecture.code == code:
                return lecture
            else:
                return


