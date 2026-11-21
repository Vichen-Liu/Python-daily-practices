def swap_dict_keys_values(dct):
    swapped={}
    for key in dct:
        swapped[dct[key]]=key
    return swapped
n={'a':1,'b':2,'c':3}
print("result=",swap_dict_keys_values(n))