
class Lecture:

    # Constructor to create new lecture
    def __init__(self, lecture_code, lecture_title, lecturer_tck):
        self.lecture = {
            'code': lecture_code,
            'title': lecture_title,
            'lecturer': lecturer_tck,
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


