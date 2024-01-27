def power(n):
   if n==0:
      return 1
   else:
      return 2*power(n-1)
print(power(6))

def count(n):
    if n==0:
        return
    else:
        print(n,end=" ")
        count(n-1)

count(5)
