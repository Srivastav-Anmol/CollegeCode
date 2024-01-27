def fibo(n):
    if n==1 or n==0:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
x=int(input("Enter nth term in fibonacci series = "))
print(fibo(x))