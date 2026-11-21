def prime_factorization(n):
    if n<=0:
        print("请输入一个正整数:")
        return
    elif n==1:
        print(1)
        return
    else:
        i=2
        while i**2<=n:
            if n%i==0:
                print(i,end="*")
                n//=i
                i=2
            else:
                i+=1
        if n>1:
            print(n)

num=int(input("请输入一个正整数:"))
prime_factorization(num)
