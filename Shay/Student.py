
class Student:
    def __init__(self,id,name ):
        self.id = id
        self.name = name
        self.dic_grades = {}

    def add_grade(self,title,grade):
        self.title=title
        self.grade=grade
        self.dic_grades[self.title] = self.grade

    def calc_factor(self,title, factor):
        self.title= title
        self.factor= factor/100
        for i in self.dic_grades:
            if i == self.title:
                self.dic_grades[i] = (self.dic_grades[i] + self.dic_grades[i]*self.factor)
            if self.dic_grades[i] > 100:
                self.dic_grades[i] = 100
        print(self.dic_grades)

    def average(self):
        num = len(self.dic_grades)
        sum_grades = self.dic_grades.values()
        sum_grades = sum(sum_grades)
        return (sum_grades/num)










