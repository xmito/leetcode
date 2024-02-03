

# Wildcard Matching (Hard)
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial). 

# Constraints:
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.

# Dynamic programming solution:
# Let dp[i][j] be True if pattern prefix of length i matches word prefix of length j
# Recursive solution for dp[i][j] is as follows:
# dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]     if p[i] == '*'
# dp[i-1][j-1]                      if p[i] == '?'
# dp[i-1][j-1] and p[i] == s[j]     if p[i] not in ['*', '?']
# TIME COMPLEXITY: O(n * m)
# SPACE COMPLEXITY: O(n * m)
def isMatch(s: str, p: str) -> bool:
    n = len(p)
    m = len(s)
    t = [[False] * (m + 1) for _ in range(n + 1)]

    t[0][0] = True
    for i in range(1, m + 1):
        t[0][i] = False
    for i in range(1, n + 1):
        t[i][0] = t[i - 1][0] and p[i - 1] == '*'
    
    for pi in range(1, n + 1):
        for wi in range(1, m + 1):
            if p[pi - 1] == '*':
                t[pi][wi] = t[pi - 1][wi] or t[pi - 1][wi - 1] or t[pi][wi - 1]
            elif p[pi - 1] == '?':
                t[pi][wi] = t[pi - 1][wi - 1]
            else:
                t[pi][wi] = t[pi - 1][wi - 1] and p[pi - 1] == s[wi - 1]

    return t[n][m]


if __name__ == "__main__":
    ret = isMatch("aa", "a")
    assert ret == False

    ret = isMatch("aa", "*")
    assert ret == True

    ret = isMatch("cb", "?a")
    assert ret == False
