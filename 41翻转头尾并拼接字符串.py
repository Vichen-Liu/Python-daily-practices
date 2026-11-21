def rotate_and_concat(s,d):
    n=len(s)
    if d<=0 or d>n:
        print("超出范围！")
        return

    head_flipped=s[:d][::-1]
    head_remaining=s[d:]
    head_result=head_flipped+head_remaining

    tail_flipped=s[-d:][::-1]
    tail_remaining=s[:-d]
    tail_result=tail_remaining+tail_flipped

    print("头部翻转结果：",head_result)
    print("尾部翻转结果：",tail_result)
    print("翻转结果：",head_result+tail_result)

string=input("请输入一串字符：")
distance=int(input("翻转个数："))
rotate_and_concat(string,distance)