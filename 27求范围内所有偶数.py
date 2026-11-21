def get_even_numbers(start,end):
    result=0
    for i in range(start,end+1):
        if i%2==0:
            result+=i
    return result
n_start=int(input("start:"))
n_end=int(input("end:"))
print(f"The sum of the even numbers from {n_start} to {n_end} is:",get_even_numbers(n_start,n_end))