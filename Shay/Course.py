from Shay.Student import Student

class Course:


    def __init__(self, num_course, name_course, max_students):
        self.num_course = num_course
        self.name_course = name_course
        self.max_students = max_students
        self.dic_teachers = {}
        self.list_students = []

    def add_student(self, student):
        if len(self.list_students) < self.max_students:
            self.list_students.append(student)
            print("True")
        else:
            print("False")

    def add_factor(self, title, factor):
        for st in self.list_students:
            if type(st) is Student:
                st.calc_factor(title, factor)


