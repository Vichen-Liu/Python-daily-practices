with open("data.txt","a",encoding="utf_8")as f:
    while True:
        input_string=input("请输入数据：")
        if input_string=="#":
            print("输入结束，数据已保存至文件中")
            break
        f.write(input_string+"\n")