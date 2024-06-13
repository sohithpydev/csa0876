def find_sum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    # Initialize sums for rows, columns, and diagonals
    row_sums = [sum(row) for row in matrix]
    column_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(columns)]
    diagonal_sum_1 = sum(matrix[i][i] for i in range(min(rows, columns)))
    diagonal_sum_2 = sum(matrix[i][columns - i - 1] for i in range(min(rows, columns)))

    return row_sums, column_sums, diagonal_sum_1, diagonal_sum_2

def main():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    row_sums, column_sums, diagonal_sum_1, diagonal_sum_2 = find_sum(a)

    print("Row sums:", row_sums)
    print("Column sums:", column_sums)
    print("Diagonal sum (top-left to bottom-right):", diagonal_sum_1)
    print("Diagonal sum (top-right to bottom-left):", diagonal_sum_2)

if __name__ == "__main__":
    main()
