# print pattern      1
##                  12
#                  123
#                 1234
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(" ", end="")
        spaces=spaces+1
    p=1
    j=1
    while j<=i:
        print(p, end="")
        j=j+1
        p=p+1
    print()
    i=i+1        