arr=[-2,3,4,5,6]
product=1
maxi=0
for i in range(len(arr)):
    product=product*arr[i]
    maxi=max(product,maxi)
    if product<0:
        product=1
print(maxi) 
