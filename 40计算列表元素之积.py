def product_of_list(numbers):
    result=1
    for number in numbers:
        result*=number
    return result
li=[3,5,72,3,5]
print("result=",product_of_list(li) )