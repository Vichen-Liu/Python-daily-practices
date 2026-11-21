with open("text.txt","w",encoding="utf-8")as f:
    while True:
        message=input("请输入数据：").upper()
        f.write(message+"\n")
        if message=="#":
            break