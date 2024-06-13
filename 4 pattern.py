def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Input: Replace 5 with the number of rows you want in the pattern
rows = 5

print_pattern(rows)
