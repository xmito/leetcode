
# Palindromic Substrings (Medium)
# Given a string s, return the number of palindromic substrings in it. A string is a
# palindrome when it reads the same backward as forward. A substring is a contiguous
# sequence of characters within the string.
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Number of palindromic substrings. Solution for s[i][j] (number of palindrome substrings in substring):
# s[i][j-1] + s[i+1][j] - s[i+1][j-1] + 1   if substring from i to j is palindrome
# s[i][j-1] + s[i+1][j] + s[i+1][j-1]       if substring from i to j is not palindrome
# Time complexity: O(nˆ2)
# Space complexity: O(nˆ2)
def countSubstringsInitial(s: str) -> int:
    sub = [[0] * len(s) for i in range(len(s))]
    is_palindrome = [[False] * len(s) for i in range(len(s))]
    for i in range(len(s)):
        sub[i][i] = 1
        is_palindrome[i][i] = True
    
    for slen in range(2, len(s) + 1):
        for i in range(len(s) - slen + 1):
            j = i + slen - 1
            sub[i][j] = sub[i][j - 1] + sub[i + 1][j] - sub[i + 1][j - 1]
            if s[i] == s[j] and (is_palindrome[i + 1][j - 1] or i + 1 > j - 1):
                sub[i][j] += 1
                is_palindrome[i][j] = True
            
    return sub[0][len(s) - 1]


# Base cases:
# dp[i][i] = True - Substrings of size 1 are all palindromes
# dp[i][i + 1] - Is substring from i to i + 1 palindrome
# True          if s[i] == s[i + 1]
# False         Otherwise
# For other cases:
# d[i][j] - Is substring from i to j palindrome
# True          if s[i] == s[j]
# False         Otherwise
# Time complexity: O(nˆ2) - For each of nˆ2 substrings compute whether it is
# palindrome in constant amount of time (we reuse results for smaller subproblems)
# Space complexity: O(nˆ2) - is_palindrome list. Also we need to store boolean list
# only for the previous two substring lengths. Thus it should be possible to get O(n)
def countSubstringsDynamic(s: str) -> int:
    is_palindrome = [[False] * len(s) for _ in range(len(s))]

    # Every single character is palindrome (Base case)
    count = len(s)
    for i in range(len(s)):
        is_palindrome[i][i] = True

    # Check every substring of length 2 (Base case)
    for i in range(len(s) - 1):
        is_palindrome[i][i + 1] = (s[i] == s[i + 1])
        count += is_palindrome[i][i + 1]
    
    # For substrings larger than 2
    for slen in range(3, len(s) + 1):
        for i in range(len(s) - slen + 1):
            j = i + slen - 1
            is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and (s[i] == s[j])
            count += is_palindrome[i][j]

    return count


# Time complexity: O(n^2) - There are 2n - 1 possible centers from which we initiate
# checks. For odd length strings, there are n centers and for even length strings n -1
# centers. All in all, we have O(n) centers and each palindrome check costs O(n). This
# approach is faster, because most centers will not produce long palindromes, so most
# expand calls will cost far less than n comparisons
# Space complexity: O(1)
def countSubstringsCenter(s: str) -> str:
        def countPalindromesAroundCenter(i, j):
            left, right = i, j
            count = 0
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
                
            return count
        
        count = 0
        for i in range(len(s)):
            count += countPalindromesAroundCenter(i, i)
            count += countPalindromesAroundCenter(i, i + 1)

        return count


if __name__ == "__main__":
    res = countSubstringsCenter("abc")
    assert res == 3

    res = countSubstringsCenter("aaa")
    assert res == 6


# Binary Search with a fast rolling hash algorithm (like Rabin-Karp). This approach tries
# to optimize Approach #3 by speeding up the time to figure out the largest palindrome
# for each of the 2N−1 centers in logarithmic time. This approach counts all palindromic
# substrings in O(NlogN) time. Here's a Quora answer by T.V. Raziman which explains this approach well.
# https://www.quora.com/How-can-we-find-the-number-of-palindromic-substrings-in-a-string-in-linear-time/answer/Raziman-T-V?ch=10&share=4957c9e6&srid=OVm2

# Palindromic trees (also known as EERTREE). It is a data structure invented by Mikhail
# Rubinchik which links progressively larger palindromic substrings within a string.
# The tree construction takes linear time, and the number of palindromic substrings can
# be counted while constructing the tree in O(N) time. Additionally, the tree can be
# used to compute how many distinct palindromic substrings are in a string (it's just
# the number of nodes in the tree) and how frequently each such palindrome occurs. This
# blog post does a good job of explaining the construction of a palindromic tree.
# https://arxiv.org/abs/1506.04862

# Suffix Arrays with quick Lowest common Ancestor (LCA) lookups. This approach utilizes
# Ukonnen's algorithm to build suffix trees for the input string and its reverse in linear
# time. Subsequently, quick LCA lookups can be used to find maximum palindromes, which
# are themselves composed of smaller palindromes. This approach can produce a count of
# all palindromic substrings in O(N) time. The original paper describes the algorithm,
# and this Quora answer demonstrates an example.
# https://www.quora.com/How-can-we-find-the-number-of-palindromic-substrings-in-a-string-in-linear-time/answer/Aniket-Alshi?ch=10&share=81e48fc8&srid=OVm2

# Manacher's algorithm. It's basically Approach #3, on steroids.TM The algorithm reuses
# computations done for previous palindromic centers to process new centers in sub-linear
# time (which reduces progressively for each new center). This algorithm counts all
# palindromic substrings in O(N) time. This e-maxx post provides a fairly simple
# implementation of this algorithm.
# https://cp-algorithms.com/string/manacher.html