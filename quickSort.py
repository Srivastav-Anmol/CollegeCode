def partition(arr,s,e):
    pivot=arr[s]
    count=0
    for i in range(s+1,e+1):
        if arr[i]<=pivot:
            count+=1
    pivotIndex=s+count
    arr[pivotIndex],arr[s]=arr[s],arr[pivotIndex]
    i=s
    j=e
    while(i<pivotIndex and j>pivotIndex):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i<pivotIndex and j>pivotIndex):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return pivotIndex
def sort(arr,s,e):
    if s<e:
        p=partition(arr,s,e)
        sort(arr,s,p-1)
        sort(arr,p+1,e)
arr=[8,6,5,2,4,1]
n=len(arr)-1
sort(arr,0,n)
print(arr)