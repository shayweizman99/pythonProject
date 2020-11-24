
class Person:
    def __init__(self):
        self.name = None
        self.taz = None
        self.age = None

    def info(self):
        self.name=(input("what is your name?:"))
        self.taz=int(input("what is your id?:"))
        self.age=int(input("what is your age?:"))

    def __str__(self):
        return f"The person's details:name-{self.name},id-{self.taz},age-{self.age} "

    def __eq__(self, other):
        if self.taz==other:
            return True
        else:
            return False


