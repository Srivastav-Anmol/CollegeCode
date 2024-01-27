x=int(input())
n=int(input())
m=int(input())
res=1
while(n>0):
    if n&1:
        res=(res)%m*(x)%m
    x=(x)%m*(x)%m
    n=n>>1
print(res)