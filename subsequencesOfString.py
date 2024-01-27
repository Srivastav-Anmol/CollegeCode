st="abc"
s=[""]
for i in st:
    for j in range(len(s)):
        a=s[j]+i
        s.append(a)
print(s)