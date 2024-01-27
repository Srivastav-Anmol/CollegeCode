a=int(input("Enter first number = "))

b=int(input("Enter second number = "))
c=0
while(a!=b):
    if a>b:
        a-=b
        c+=1
    else:
        b-=a
print(a)
print( c)