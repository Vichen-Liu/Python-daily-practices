s=input("请输入一串字符:")
letter=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print(f"字母个数:{letter}")
print(f"空格个数:{space}")
print(f"数字个数:{digit}")
print(f"其他字符个数:{others}")