st="testsample"
print(st)
dic={}
for i in st:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
ma=0
for key,values in dic.items():
    if ma<=values:
        ma=values
        k=key
print(k,ma)
