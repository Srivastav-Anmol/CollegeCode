x=int(input("Enter Number of rounds = "))
c=0
z=[]
for i in range(x):
    p,q=input("Enter scores of both players ").split()
    a=int(p)
    b=int(q)
    if a>b:
        diff=a-b
        z.append(diff)
        c+=1
    else:
        diff=b-a
        z.append(diff)
t=max(z)
if(c>=1):
    print("Player1 wins with lead",max(z))
else:
    print("Player2 wins with lead",max(z))       