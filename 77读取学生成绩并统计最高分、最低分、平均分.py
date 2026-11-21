def read_file():
    scores=[]
    with open("D:\\学习\\Python 100题\\grades","r",encoding="utf-8") as f:
        for line in f.readlines():
            line=line[:-1]
            line=line.split("，")
            scores.append(float(line[-1]))
        print(scores)

        highest=max(scores)
        print(f"最高分是：",highest)
        lowest=min(scores)
        print(f"最低分是：",lowest)
        total=0
        for score in scores:
            total+=score
        average_score=total/len(scores)
        print(f"平均分：",average_score)

read_file()


