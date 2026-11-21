def remove_duplicates(list1):
    result=[]
    for i in list1:
        if i not in result:
            result.append(i)
    return result
list1=[10,30,30,20,10]
print("The result is:",remove_duplicates(list1))
print("The result is:",list(set(list1)))