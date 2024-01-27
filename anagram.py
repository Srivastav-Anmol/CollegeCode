x="abcbaa"
y="cabbaa"
dic1={}
dic2={}
for c in set(x):
    dic1[c]=x.count(c)
print(dic1)
for j in set(y):
    dic2[j]=y.count(j)
print(dic2)
for k in dic1:
    if dic1.get(k)!=dic2.get(k):
        print("no")
    else:
        print("Yes")
      
