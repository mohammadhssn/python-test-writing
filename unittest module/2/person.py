class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f'{self.fname} {self.lname}'

    def email(self):
        return f'{self.full_name()}@email.com'.replace(' ', '')
