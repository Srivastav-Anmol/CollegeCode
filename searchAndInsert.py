arr=[1,3,5,3,4,7]
k=5
low=0
high=len(arr)-1
while(low<=high):
    mid=(low+high)//2
    if arr[mid]>k:
        high=mid-1
    elif arr[mid]<k:
        low=mid+1
    else:
        print(mid)
print(low)