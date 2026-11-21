import os
size1=os.path.getsize("D:\\学习\\Python 100题\\Introduction of Jay Chou")
print(size1)
size2=0
for file in os.listdir("D:\\学习\\Python 100题"):
    if os.path.isfile(file):
        size2+=os.path.getsize(file)
size2=size2/1024
print(f"当前文件夹里所以文件大小是：{size2:.2f}kb")
