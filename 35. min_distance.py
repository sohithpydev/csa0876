# Insert, Delete, and Replace
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    # Initialize the dp array with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the first row and first column
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    # Fill the rest of the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1,  # Replace
                               dp[i - 1][j] + 1,  # Delete
                               dp[i][j - 1] + 1)  # Insert

    return dp[m][n]


# Example usage:
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3

word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))  # Output: 5
