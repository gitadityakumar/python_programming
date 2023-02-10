# print pattern      1
##                  121
#                  12321
#                 1234321
#this is isocelus pattern here is the apporch 
#first we need to print spaces then increasing order then decresing order 
n=int(input())
i=1
while i<=n:  # printing spaces 
    spaces=1
    while spaces<=n-i:
        print(" ", end="")
        spaces=spaces+1
    p=1
    j=1
    while j<=i:             #printing increasing order 
        print(p, end="")
        j=j+1
        p=p+1
        #printing increasing order 
    p=i-1
    while p>=1:          
        print(p,end="")
        p=p-1
    print()
    i=i+1           