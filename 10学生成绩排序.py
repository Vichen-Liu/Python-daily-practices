students=[
    {'sno':101,'sname':"小张",'sgrade':88},
    {'sno':102,'sname':"小王",'sgrade':77},
    {'sno':103,'sname':"小李",'sgrade':99},
    {'sno':104,'sname':"小赵",'sgrade':66}
]
student_sort=sorted(students,key=lambda x:x["sgrade"],reverse=True)
print(student_sort)