def count_occurrence(lst,element):
    count=0
    for i in lst:
        if i==element:
            count+=1
    return count
li=[2,2,3,5,2,1,2,4]
print(f"这个列表中有{count_occurrence(li,2)}个2")