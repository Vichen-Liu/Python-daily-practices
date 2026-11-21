import time
start=time.perf_counter()
for i in range(10000):
    print(i)
end=time.perf_counter()
print(f"耗时:{end-start:.3f}秒")