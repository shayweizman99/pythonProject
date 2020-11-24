from Shay.Student import Student
from Shay.Course import Course

# dic = {"a": 10, "math": 20, "c": 30}
# for i in dic:
#     if i == "math":
#         dic[i] = 22
# print(dic)
#
# # for i in dic:
# #     print(dic)

# dic = {1: 20, 2: 40}
# sum(dic.values()))
# #
# shay=Student(123, "shay")
# shay.add_grade("math", 80)
# shay.add_grade("program", 50)
# shay.calc_factor(2, "math")
# print(shay.average())

# lst = [1, 2, 3]
# lst.append(4)
# print(lst)
#
# lst += [5]
# print(lst)

st = Student(123, "dolev")
st.add_grade("math", 50)
course = Course(1,"Py",5)
course.add_student(st)
course.add_factor("math", 10)
print(st.dic_grades)