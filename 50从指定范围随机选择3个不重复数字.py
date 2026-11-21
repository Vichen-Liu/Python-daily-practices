import random
start=int(input("请输入开始范围:"))
end=int(input("请输入结束范围:"))
random_sample=random.sample(range(start,end+1),3)
print(random_sample)