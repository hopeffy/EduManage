import csv

from lecture import Lecture
from lecture_list import LectureList
from lecturer_list import LecturerList
from student import Student
from student_list import StudentList
import keyboard


class Main:
    def __init__(self):
        self.student_list = StudentList()
        self.lecturer_list = LecturerList()
        while True:
            print("Whats up buddy. U student or lecturer_f\nSelect your role:\n1-student\n2-lecturer_f\n3-display list")
            role_number = input()
            if role_number == "1":
                print("tck")
                student_tck = input()
                print("name and surname")
                student_name_and_surname = input()
                student = Student(student_tck, student_name_and_surname)
                self.student_list.add_student(student)

            elif role_number == "2":
                print("tck")
                l_tck = input()
                print("name and surname")
                l_name_and_surname = input()
                lecturer = (l_tck, l_name_and_surname)
                self.lecturer_list.add_lecturer(lecturer)

            elif role_number == "3":
                self.student_list.display()


def save_to_csv_file(listA):
    with open('lecture_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(['code', 'title'])
        for l in listA:
            csv_writer.writerow(l)


class Use:
    def __init__(self):
        self.sList = StudentList()
        self.lList = LecturerList()
        self.lecList = LectureList()

        print("Ders listesi: ")
        self.lecList.display()
        print("Yeni ders eklemek için ctr'a basıp virgülle ayrılmış şekilde code, ismini gir")

        keyboard.add_hotkey('ctrl+space', self.save_file)

        while True:
            keyboard.read_key()
            if keyboard.is_pressed("ctrl+space"):
                print("ctrl+space basıldı")
                save_to_csv_file(self.lecList.lecture_list)
                print("dosya kaydedildi")
                break
            if keyboard.is_pressed("CTRL"):
                print("ctrlye bastın hll")
                nl = input()
                l = nl.split(",")
                lecture = Lecture(lecture_code=l[0], lecture_title=l[1], lecturer_tck=l[2])  # code - title - lecturer_f tck
                self.lecList.add_lecture(lecture_code=lecture.code, lecture_title=lecture.title, lecturer_tck=lecture.lecturer)
                self.lecList.display()
                print("yeniden ders eklemek için ctrle bas, devam etmek için tab'a bas.")







    def save_file(self):
        save_to_csv_file(self.lecList.lecture_list)
        print("dosya kaydedildi")
        exit()


# Make sure to instantiate and run Main
if __name__ == "__main__":
    Use()
