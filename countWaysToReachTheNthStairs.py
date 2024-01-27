def climb(n):
    if n<0: #base case
        return 0
    elif n==0:  # base case
        return 1
    else:
        return climb(n-1)+climb(n-2)
x=int(input("Enter number of stairs = "))
print("Number of ways can a climber can reach",climb(x))