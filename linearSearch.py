def search(list,n,x):
    if n==0:
        return False
    elif list[0]==x:
        return True
    else:
        if list[n-1]==x:
            return True
    return search(list,n-1,x)
    
list=[1,2,3,4,5]
n=len(list)
x=3 
if search(list,n,x)==True:
    print("Found")
else:
    print("Not Found")