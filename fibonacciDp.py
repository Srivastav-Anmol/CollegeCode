func=0
dp=[0]*40
def help(n):
    global func
    global dp
    func+=1
    if n==1 or n==2:
        return 1
    else:
        if dp[n]!=0:
            return dp[n]
        dp[n]=help(n-1)+help(n-2)
        return dp[n]
print(help(30))
print(func)
