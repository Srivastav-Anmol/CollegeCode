t=int(input("No. of test Cases = "))
p=[]
s=0
l=0
for i in range(t):
    a=int(input("Inputs = "))
    for j in range(a):
        p=list(map(str,input()))
    for k in p:
        if k=="START38":
            s+=1
        else:
            l+=1
    print (s,l)