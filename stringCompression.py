chars=["a","a","b","b","c","c","c"]
i=0
index=0
n=len(chars)
while(i<n):
    letter=chars[i]
    count=0
    while(i<n and chars[i]==letter):
        count+=1
        i+=1
    chars[index]=letter
    index+=1
    if count>1:
        for j in str(count):
            chars[index]=j
            index+=1
print(index)
print(chars)