def print_rhombus(rows):
    if rows%2==0:
        print("行数必须是奇数！")
        return
    for i in range(1,rows,2):
        space=" "*((rows-i)//2)
        star="*"*i
        print(space+star)
    for i in range(rows,0,-2):
        space=" "*((rows-i)//2)
        star="*"*i
        print(space+star)

n=int(input("请输入行数:"))
print_rhombus(n)