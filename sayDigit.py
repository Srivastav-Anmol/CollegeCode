def say(n):
    arr=["zero",'one','two','three','four','five','six','seven','eight','nine']
    if n==0:
        return 
    else:
        num=n%10
        n=n//10
        say(n)
        print(arr[num],end=" ")
        

say(413)