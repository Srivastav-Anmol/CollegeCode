def palin(str,i,j):
    if i>j:
        return True
    if str[i]!=str[j]:
        return False
    else:
        return palin(str,i+1,j-1)
s="jalaj"
i=0
j=len(s)-1
if palin(s,i,j):
    print("Palindrome")
else:
    print("Not palindrome")