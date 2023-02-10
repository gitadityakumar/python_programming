#print pattern  1
#               12
#               123
#               1234
#operation usi per hoga jisme change ho raha ho
n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        p=p+1
        j=j+1
    print()    
    i=i+1