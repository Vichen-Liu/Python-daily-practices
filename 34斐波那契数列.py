def fibonacci(n):
    if n<=0:
        print("请输入一个正整数！")
        return
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("请输入第几个:"))
print(f"斐波那契数列的第{num}项是:",fibonacci(num) )