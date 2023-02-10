#  pattern 1111
#          2222
#          3333
#          4444
# second pattern   1234
#                  1234
#                  1234
#                  1234
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(i , end="")   # for second que just replace i with j 
        j=j+1
    print()    
    i=i+1