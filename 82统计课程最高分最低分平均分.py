course_grades={}
with open("D:\\学习\\Python 100题\\course_student_grade",encoding="utf-8") as f:
    for line in f.readlines():
        line=line[:-1]
        course,sid,name,grade=line.split("，")
        if course not in course_grades:
            course_grades[course]=[]
        course_grades[course].append(float(grade))

for course,grades in course_grades.items():
    print(course,max(grades),min(grades),sum(grades)/len(grades))

