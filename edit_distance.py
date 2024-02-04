

# Edit Distance (Medium)
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2. You have the following three operations
# permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Constraints:
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.


# Let K be the length of word1
# Let N be the length of word2
# Let M be max(K, N)
# TIME COMPLEXITY: O(3ˆM) - if letters do not match, we need to explore three possibilities
# SPACE COMPLEXITY: O(M) - recursion terminates when either word prefix is empty
def minDistanceBrute(word1: str, word2: str) -> int:
    if word1 == word2:
        return 0

    def editDistanceRecur(w1_p, w2_p):
        if w1_p == 0:
            return w2_p
        elif w2_p == 0:
            return w1_p
        
        if word1[w1_p - 1] == word2[w2_p - 1]:
            return editDistanceRecur(w1_p - 1, w2_p - 1)
        else:
            return min(
                editDistanceRecur(w1_p - 1, w2_p - 1),  # Replace
                editDistanceRecur(w1_p, w2_p - 1),  # Insert
                editDistanceRecur(w1_p - 1, w2_p),  # Delete
            ) + 1

    return editDistanceRecur(len(word1), len(word2))


# Dynamic programming solution
# Let dp(i, j) be minimum number of operations needed for word1 prefix of length i
# to match word2 prefix of length j
# 0                     if i == 0 and j == 0
# dp[i][j - 1] + 1      if i == 0 and j > 0
# dp[i - 1][j] + 1      if j == 0 and i > 0
# dp[i - 1][j - 1]      if word1[i] == word2[j]
# dp[i - 1][j - 1] + 1  if word1[i] is replaced with word2[j]
# dp[i - 1][j] + 1      if word1[i] is deleted
# dp[i][j - 1] + 1      if word2[j] is inserted after word1[i]
# TIME COMPLEXITY: O(m * n)
# SPACE COMPLEXITY: O(m * n)
def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    x = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        x[i][0] = x[i - 1][0] + 1
    for j in range(1, m + 1):
        x[0][j] = x[0][j - 1] + 1

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if word1[j - 1] != word2[i - 1]:
                x[i][j] = min(
                    x[i][j - 1],
                    x[i - 1][j],
                    x[i - 1][j - 1],
                ) + 1
            else:
                x[i][j] = x[i - 1][j - 1]

    return x[n][m]


if __name__ == "__main__":
    ret = minDistanceBrute("horse", "ros")
    print(ret)
    assert ret == 3

    ret = minDistanceBrute("intention", "execution")
    print(ret)
    assert ret == 5