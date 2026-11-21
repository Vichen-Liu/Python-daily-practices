def swap_first_last(new_list):
    new_list[0],new_list[-1]=new_list[-1],new_list[0]
    print(new_list)
list1=[1,3,6,3,2]
list2=['a','b','c']
swap_first_last(list1)
swap_first_last(list2)