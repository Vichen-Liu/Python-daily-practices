import re
pattern=r"1[3-9]\d{9}"
with open("D:\\学习\\Python 100题\\webpage_phone_numbers",encoding="UTF-8")as f:
    file_content=f.read()

results=re.findall(pattern,file_content)
for result in results:
    print(result)