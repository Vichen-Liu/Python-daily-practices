def string_to_int():
    try:
        n=int(input("请输入一串数字:"))
    except:
        return "输入值无效！"
    else:
        return n
print(string_to_int() )