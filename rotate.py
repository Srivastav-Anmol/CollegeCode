arr=[1,3,5,7,9]
x=int(input("Enter the position ="))
n=len(arr)
temp=[0]*n
for i in range(n):
    temp[(i+x)%n]=arr[i]
arr=temp
print("Rotated array ",arr)