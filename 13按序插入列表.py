li=[23,34,36,67,89]
num=int(input("请输入一个数:"))
for i in range(len(li)):
    if li[i]>num:
        li.insert(i,num)
        break
else:
    li.append(num)
print(li)
