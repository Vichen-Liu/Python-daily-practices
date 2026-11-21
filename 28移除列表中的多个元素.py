def remove_elements(list1,list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
            list2.remove(i)
    return list1
def append_elements(list1,list2):
    for i in list2:
        if i not in list1:
            list1.append(i)
    return list1
list1=[25,21,3,9]
list2=[24,2,75,3]
print("Now list1 is:",remove_elements(list1,list2))
print("Now list1 is:",append_elements(list1,list2))