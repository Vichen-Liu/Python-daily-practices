import random
num1=random.random()
print("生成一个0-1的随机小数:",num1)

num2=random.randint(1,9)
print("生成一个范围内随机整数:",num2)

list1=["剪刀","石头","布"]
num3=random.choice(list1)
print("生成一个列表中随机元素:",num3)

random.shuffle(list1)
print("将列表中元素随机排序:",list1)