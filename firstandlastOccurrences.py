arr=[1,3,5,3,4,7]
first=0
last=0
k=3
for i in range(len(arr)):
    if arr[i]==k:
        if first==0:
            first=i
        last=i
print(first,last)
