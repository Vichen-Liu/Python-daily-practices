def read_file():
    result=[]
    with open("D:\\学习\\Python 100题\\grades","r",encoding="utf-8") as f:
        for line in f.readlines():
            line=line[:-1]
            line=line.split("，")
            result.append(line)
    return result

def sort_grades(data):
    return sorted(data,key=lambda x:int(x[2]))

data=read_file()
print("读取文件内容：",data)
data=sort_grades(data)
print("排序后成绩：",data)