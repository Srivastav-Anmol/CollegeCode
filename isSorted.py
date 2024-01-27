def isSorted(list,n):
    if n==0 or n==1:
        return True
    else:
        return (list[n-1]>=list[n-2] and isSorted(list,n-1))
list=[0,1,2,3]
n=len(list)
if isSorted(list,n):
    print("Yes")
else:
    print("No")