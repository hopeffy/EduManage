class Person:  # Person class

    # Constructor to create new person
    def __init__(self, tck_no, name_surname, role):
        self.person = {
            'tck_no': tck_no,
            'name_surname': name_surname,
            'role': role
        }

    def __str__(self):
        return f'TCK: {self.tck_no}, Name: {self.name_surname}, Role: {self.role}'

    @property
    def tck_no(self):
        return self.person["tck_no"]

    @property
    def name_surname(self):
        return self.person["name_surname"]

    @property
    def role(self):
        return self.person["role"]

    @tck_no.setter
    def tck_no(self, value):
        self.person["tck_no"] = value

    @name_surname.setter
    def name_surname(self, value):
        self.person["name_surname"] = value

    @role.setter
    def role(self, value):
        self.person["role"] = value

    def __str__(self):
        return f'{self.person["tck_no"]} {self.person["name_surname"]} {self.person["role"]}'


