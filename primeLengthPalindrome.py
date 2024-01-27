s="abbba"
i=0
j=len(s)-1
n=len(s)
flag1=0
flag2=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag1=1
            break
else:
    while(i<=j):
        if s[i]==s[j]:
            i+=1
            j-=1
            flag2=1
        else:
            flag2=0
            break
if flag2==1 and flag1==0:
    print("True")
else:
    print("False")