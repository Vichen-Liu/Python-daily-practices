class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=[]

    def add_grade(self,grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)

class StudentGradeManager:
    def __init__(self):
        self.students={}

    def add_student(self,name):
        if name not in self.students:
            self.students[name]=Student(name,[])
        else:
            print(f"学生{name}已存在！")

    def get_student(self,name):
        return self.students.get(name)

    def add_grade_to_student(self,name,grade):
        student=self.get_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"学生{name}不存在！")

    def show_average_grades(self):
         for name,student in self.students.items():
             print(f"{name}的平均成绩为：{student.average_grade():.2f}")

manager=StudentGradeManager()
manager.add_student("Vichen")
manager.add_student("JAY")
manager.add_student("JJ")
manager.add_grade_to_student("Vichen",90)
manager.add_grade_to_student("Vichen",95)
manager.add_grade_to_student("JAY",95)
manager.add_grade_to_student("JJ",88)
manager.show_average_grades()