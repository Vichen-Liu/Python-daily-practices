def sum_of_squares(n):
    result=0
    for i in range(1,n+1):
        result+=i**2
    return result
n=int(input("请输入一个整数:"))
print(f"1-{n}的数字的平方和为:",sum_of_squares(n))