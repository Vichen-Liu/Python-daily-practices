num=int(input("请输入一个奇数："))
n=1
while True:
    n_9=int('9'*n)
    if n_9%num==0:
        print(n_9)
        break
    else:
        n+=1
