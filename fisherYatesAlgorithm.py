import random
arr=[1,2,3,4,5]
n=len(arr)-1
j=random.randint(0,n)
for i in range(n,0,-1):
    arr[i],arr[j]=arr[j],arr[i]
print(arr)