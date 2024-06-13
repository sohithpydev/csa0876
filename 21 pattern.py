rows = 5

for i in range(1, rows + 1):
    # Inner loop to print '*' for each column
    for j in range(i):
        print("*", end=" ")
    
    # Move to the next line after printing '*' for each column
    print()
