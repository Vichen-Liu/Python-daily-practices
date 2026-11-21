import time
print("按下回车键开始计时，中断程序则停止计时。")
input("准备...")
start_time=time.time()
print("开始计时...")

try:
    while True:
        elapsed_time=time.time()-start_time
        print(f"\r计时:{elapsed_time:.0f}秒",end="")
        time.sleep(1)
except KeyboardInterrupt:
    end_time=time.time()
    total_time=round(end_time-start_time,2)
    print(f"\n计时结束，总用时:{total_time}秒")
