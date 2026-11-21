import csv
with open("D:\\学习\\Python 100题\\人员信息.csv",encoding="utf-8")as f:
    reader=csv.reader(f)
    data=[row for row in reader]

with open("人员信息[备份].csv","w",newline="",encoding="utf-8")as f:
    writer=csv.writer(f)
    writer.writerows(data)