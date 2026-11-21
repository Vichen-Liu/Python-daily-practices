def sum_of_reciprocal_series(n):
    result=0
    if n%2==0:
        for i in range(2,n+1,2):
            result+=1/i
    else:
        for i in range(1,n+1,2):
            result+=1/i
    return result
num=int(input("Please enter a number:"))
print("The answer is:",sum_of_reciprocal_series(num))
