import time
start=time.time()
for i in range(3000):
    print(i)
end=time.time()
spand_time=end-start
print("耗时:",spand_time)