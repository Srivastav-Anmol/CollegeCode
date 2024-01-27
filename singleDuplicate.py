arr=[1,3,4,2,4]
i=0
j=1
while(i<=j and j<=len(arr)-1):
    if arr[i]!=arr[j]:
        j+=1
    if arr[i]==arr[j]:
        print(arr[i],"is repeating")
        break
    i+=1
    j=i+1