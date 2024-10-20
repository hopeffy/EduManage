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

