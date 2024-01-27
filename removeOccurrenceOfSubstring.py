s="daabcbaabcbc"
part="abc" 
n=len(s)
while(n!=0 and s.find(part)<n):
    s.replace(part,'')
print(s)