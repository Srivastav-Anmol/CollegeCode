r=int(input("Enter number of rows = "))
c=int(input("Enter number of columns = "))
arr=[]
for i in range(r):
    col=[]
    for j in range(c):
        col.append(int(input("")))
    arr.append(col)
print('\n')
for k in range(c):
    if k&1:
        for e in range(r-1,-1,-1):
            print(arr[e][k])
    else:
        for e in range(r):
            print(arr[e][k])
