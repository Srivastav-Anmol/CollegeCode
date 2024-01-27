arr=[1,2,3]
res=[[]]
for i in arr:
    for j in range(len(res)):
        a=res[j]+[i]
        res.append(a)
print(res)