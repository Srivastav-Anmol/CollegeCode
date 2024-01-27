arr=[0,1,0,3,12]
i=0
for j in range(0,len(arr)):
    if(arr[j]!=0):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1 
print("array",arr)