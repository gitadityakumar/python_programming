n=int(input())
i=1
while i<=n:  # printing spaces 
    spaces=1
    while spaces<=n-i:
        print(" ", end="")
        spaces=spaces+1
    p=i
    j=1
    while j<=i:             #printing increasing order 
        print(p, end="")
        j=j+1
        p=p+1
        #printing increasing order 
    p=i-1
    while p>=1:          
        print( i ,end="")
        p=p-1
    print()
    i=i+1           