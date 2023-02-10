  #              *
  #             ***
   #           *****
    #         *******    star pattern
N=int(input())
i=1
while i<=N:
    space=1
    while space <= N-i:
        print( "",end="")
        space=space+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
            
