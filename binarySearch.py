def binary(list,low,high,x):
    mid=(low+high)//2
    if low>high:
        return False
    elif list[mid]==x:
        return True
    elif list[mid]<x:
        return binary(list,mid+1,high,x)
    elif list[mid]>x:
        return binary(list,low,mid-1,x)
list=[1,2,3,5,6]
low=0
high=len(list)-1
x=5
if binary(list,low,high,x)==True:
    print("Found")
else:
    print("Not Found")