s="aababaab"
l=[]
i=0
while(i<len(s)):
    if len(s)!=0 and s[i]  in l:
        l.pop(-1)
        i+=1
    else:
        l.append(s[i])
        i+=1
print("".join(l))