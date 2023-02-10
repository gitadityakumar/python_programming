#Pattern for N = 5
#E
#DE
#CDE
#BCDE
#ABCDE
N = int(input())
i = 1
while i <= N:
    j = 1
    start_char=chr(ord("A")+i-1)
    while j <= i+1:
        charp=chr(ord(start_char)+j-1)
        print(charp, end="")
        j = j+1
    print()
    i = i+1