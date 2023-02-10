#print pattern 1
#              23     
#              345 
#              4567
n=int(input())
i=1
while i<=n:
    p=i
    j=1
    while j<=i:
        print(p,end="")
        p=p+1
        j=j+1
    print()    
    i=i+1