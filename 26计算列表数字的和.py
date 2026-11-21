def sum_of_the_list(list):
    result=0
    for number in list:
        result+=number
    return result
list1=[3,46,8,3]
list2=[2,48,34]
print("The sum of the first list is:",sum_of_the_list(list1))
print("The sum of the second list is:",sum_of_the_list(list2))
print(sum(list1))
print(sum(list2))