arr1=[1,2,3,4]
arr2=[6]
n=len(arr1)-1
m=len(arr2)-1
carry=0
i=n
j=m
ans=[]
while(i>=0 and j>=0):
    var1=arr1[i]
    var2=arr2[j]
    sum=var1+var2+carry
    carry=sum//10
    sum=sum%10
    ans.append(sum)
    i-=1
    j-=1
while(i>=0):
    sum=arr1[i]+carry
    carry=sum//10
    sum=sum%10
    ans.append(sum)
    i-=1
while(j>=0):
    sum=arr2[j]+carry
    carry=sum//10
    sum=sum%10
    ans.append(sum)
    j-=1
while(carry!=0):
    sum=carry
    carry=sum//10
    sum=sum%10
    ans.append(sum)
ans.reverse()
print("Sum of two arrays's = ",ans)
