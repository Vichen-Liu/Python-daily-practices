a=int(input("你要生成的数字:"))
n=int(input("生成的个数:"))
c_result=0
result=0
for i in range(1,n+1):
    result=result*10+a
    c_result+=result
print(c_result)