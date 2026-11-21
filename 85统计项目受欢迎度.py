like_count={}
with open("D:\\学习\\Python 100题\\student_like",encoding="utf-8")as f:
    for line in f.readlines():
        line=line[:-1]
        name,likes=line.split(" ")
        like_list=likes.split("，")
        for like in like_list:
            if like not in like_count:
                like_count[like]=1
            else:
                like_count[like]+=1
print(like_count)