

# Regualar Expression Matching (Hard)
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial)

# Constraints:
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

# Dynamic programming solution:
# d[i][j] is true if pattern prefix of length i matches string prefix of length j
# True                      if i==0 and j==0
# False                     if i==0 and j>0
# dp[i - 1][0]              if j==0 and (p[i - 1] == '*' or (i < n and p[i] == '*'))
# dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')  if p[i - 1] != '*'
# Let no_match = dp[i - 2][j]
# Let single_match = dp[i - 2][j - 1] and (p[i - 2] == s[j - 1] or p[i - 2] == '.')
# Let more_match = dp[i][j - 1] and (p[i - 2] == s[j - 1] or p[i - 2] == '.')
# no_match or single_match or more_match        if p[i - 1] == '*'
# TIME COMPLEXITY: O(n * m) - we fill matrix of size n * m and each value is computed in O(1)
# SPACE COMPLEXITY: O(n * m) - memoization
def isMatch(s: str, p: str) -> bool:
    n = len(p)
    m = len(s)
    t = [[False] * (m + 1) for _ in range(n + 1)]

    t[0][0] = True
    for i in range(1, m + 1):
        # Empty pattern cannot match non-empty string
        t[0][i] = False
    
    for i in range(1, n + 1):
        # Empty string can be matched only by empty pattern
        # or pattern that is a sequence of .* or <char>*
        if p[i - 1] == '*' or (i < n and p[i] == '*'):
            t[i][0] = t[i - 1][0]

    for pi in range(1, n + 1):
        for wi in range(1, m + 1):
            if p[pi - 1] == '*':
                no_match = t[pi - 2][wi]
                single_match = t[pi - 2][wi - 1] and (s[wi - 1] == p[pi - 2] or p[pi - 2] == '.')
                more_match = t[pi][wi - 1] and (s[wi - 1] == p[pi - 2] or p[pi - 2] == '.')
                t[pi][wi] = no_match or single_match or more_match
            else:
                t[pi][wi] = t[pi - 1][wi - 1] and (s[wi - 1] == p[pi - 1] or p[pi - 1] == '.')

    return t[n][m]


if __name__ == "__main__":
    ret = isMatch("aa", "a")
    assert ret == False

    ret = isMatch("aa", "a*")
    assert ret == True

    ret = isMatch("ab", ".*")
    assert ret == True
