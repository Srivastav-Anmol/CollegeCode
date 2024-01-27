def sumA(list,n):
    s=0
    if n==0:
        return 0
    elif n==1:
        return list[0]
    else:
        return list[n-1]+sumA(list,n-1)
list=[1,2,3]
n=len(list)
print(sumA(list,n))

