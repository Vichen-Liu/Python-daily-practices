import time
a1="2026-6-6 20:15:19"
time_array1=time.strptime(a1,"%Y-%m-%d %H:%M:%S")
timestamp=int(time.mktime(time_array1))
print(timestamp)

a2="2026/6/6 20:19:37"
time_array2=time.strptime(a2,"%Y/%m/%d %H:%M:%S")
time_string=time.strftime("%Y-%m-%d %H:%M:%S",time_array2)
print(time_string)