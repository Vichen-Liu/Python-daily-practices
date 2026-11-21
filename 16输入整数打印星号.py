for i in range(7):
    num=int(input("请输入一个1-50的整数:"))
    if 1<=num<=50:
        print('*'*num)
    else:
        print("输入的数不符合要求！")