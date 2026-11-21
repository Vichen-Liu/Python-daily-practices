course_teacher={}
with open("D:\\学习\\Python 100题\\course_teacher",encoding="utf-8") as f:
    for line in f.readlines():
        line=line[:-1]
        course,teacher=line.split("，")
        course_teacher[course]=teacher

with open("D:\\学习\\Python 100题\\course_student_grade",encoding="utf-8") as f:
    for line in f.readlines():
        line=line[:-1]
        course,sid,name,grade=line.split("，")
        teacher=course_teacher.get(course)
        print(course,teacher,sid,name,grade)