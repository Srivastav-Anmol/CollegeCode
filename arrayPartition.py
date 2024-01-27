arr=[4,1,2,5,6,8,1]
low=0
high=len(arr)-1
i=0
pivot=4
while(i<=high):
    if arr[i]<pivot:
        arr[i],arr[low]=arr[low],arr[i]
        low+=1
        i+=1
    elif arr[i]>pivot:
        arr[i],arr[high]=arr[high],arr[i]
        high-=1
    else:
        i+=1
print(arr)