class Student:
    def __init__(self,name,age,sid):
        self.name=name
        self.age=age
        self.sid=sid

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sid(self):
        return self.sid

student=Student("Vichen",19,14)
print(student.name)
print(student.age)
print(student.sid)