

def merge(arr,start,end):
    mid=start+(end-start)//2
    n1=mid-start+1
    n2=end-mid
    left=[0]*n1
    right=[0]*n2
    for i in range(n1):
        left[i]=arr[start+i]
    for j in range(n2):
        right[j]=arr[mid+1+j]
    q=0
    w=0
    k=start
    while(q<n1 and w<n2):
        if left[q]<=right[w]:
            arr[k]=left[q]
            q+=1
        else:
            arr[k]=right[w]
            w+=1
        k+=1
    while(q<n1):
        arr[k]=left[q]
        q+=1
        k+=1
    while(w<n2):
        arr[k]=right[w]
        w+=1
        k+=1
def mergeSort(arr,start,end):
    if start<end:
        mid=start+(end-start)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,end)

arr=[3,5,3,2,1,9]
n=len(arr)-1
mergeSort(arr,0,n-1)
print(arr)      

