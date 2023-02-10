N = int(input())
i = 1
while i <= N:
  j = 1
  while j <= i:
    print(chr(i+64), end="")
    j += 1
  print()
  i += 1
