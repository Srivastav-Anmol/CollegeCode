r=int(input("Enter number of rows = "))
c=int(input("Enter number of columns = "))
arr=[]
for i in range(r):
    col=[]
    for j in range(c):
        col.append(int(input("")))
    arr.append(col)
for k in range(len(arr)):
    print(arr[k],end="\n")
#row-wise sum
s=0
ma=0
for i in range(r):
    for j in range(c):
        s+=arr[i][j]
    print(s)
    ma=max(ma,s)
print("largest row sum=",ma)
