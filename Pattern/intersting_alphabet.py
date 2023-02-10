N = int(input())  # number of rows

# iterate through the rows
i = 1
while i <= N:
    # initialize an empty string for the row
    row = ""
    
    # iterate through the columns
    j = 1
    while j <= i:
        # add the character to the row string
        row = chr(ord('A') + N - j) + row
        j += 1
    
    # print the row
    print(row)
    
    i += 1

