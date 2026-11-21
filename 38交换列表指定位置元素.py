def swap_elements_by_position(list1,pos1,pos2):
    if not(1<=pos1<=len(list1)) or not(1<=pos2<=len(list1)):
        print("超出范围！")
        return list1
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1
list1=[23,14,52,35,31,73]
pos1=int(input("交换的第一个位置:"))-1
pos2=int(input("交换的第二个位置:"))-1
print("result is:",swap_elements_by_position(list1,pos1,pos2) )