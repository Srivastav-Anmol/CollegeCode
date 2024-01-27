arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]
copy=arr1
arr1.clear()
n,m=len(copy),len(arr2)
i,j=0,0
while(i<n and j<m):
    if copy[i]<arr2[j]:
        arr1.append(copy[i])
        i+=1
    else:
        arr1.append(arr2[j])
        j+=1
while(i<n):
    arr1.append(copy[i])
    i+=1
while(j<m):
    arr1.append(arr2[j])
    j+=1
print("Merged array = ",arr1)