num=[]
for i in range(3):
    num.append(float(input(f"请输入第{i+1}个数：")))
for k in range(2):
    if num[k]>num[k+1]:
        t=num[k]
        num[k]=num[k+1]
        num[k+1]=t
print(num)