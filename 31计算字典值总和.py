def sum_of_dict_values(dict):
    result=0
    for value in dict.values():
        result+=value
    return result
dict1={"agg1":100,"agg2":98,"agg3":79}
print("The sum is:",sum_of_dict_values(dict1))
        