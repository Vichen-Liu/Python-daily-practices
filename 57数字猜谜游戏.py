import random
import time
target_number=random.randint(0,99)
print("欢迎来到数字猜谜游戏！")
print("我已经想好了一个0-99的数字，你能猜到它是什么吗？")
start_time=time.time()

while True:
    try:
        guess=int(input("请输入你的猜测:"))
    except ValueError:
        print("请输入一个有效的数字！")
    else:
        if guess<target_number:
            print("小了！")
        elif guess>target_number:
            print("大了！")
        else:
            print("恭喜你，猜对了！")
            end_time=time.time()
            break

total_time=end_time-start_time
print(f"总用时:{total_time}秒")