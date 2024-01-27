arr1=[5,6,7,9]
arr2=[1,2,4]
k=13
print("Sum = ",k)
for i in range(len(arr1)):
    temp=arr1[i]
    for j in range(i+i,len(arr1)):
        if temp+arr1[j]==k:
            print("In Array 1 at index = ",i,"In Array 1 at index = ",j)
            print(temp,arr1[j])
            break
    for m in range(len(arr2)):
        if temp+arr2[m]==k:
            print("In Array 1 at index = ",i,"In Array 2 at index = ",m)
            print(temp,arr2[m])
            break
