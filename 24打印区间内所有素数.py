n_start=int(input("起始:"))
n_end=int(input("结束:"))
def is_prime(num):
    if num<=1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False

        return True

def print_numbers(start,end):
    for i in range(start,end+1):
        if is_prime(i):
            print(i)
print_numbers(n_start,n_end)