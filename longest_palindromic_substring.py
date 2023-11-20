from typing import Tuple, List

# Longest Palindromic Substring (Medium)
# Given a string s, return the longest palindromic substring in s
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Time complexity: O(nˆ2)
# Space complexity: O(1) - 
def longestPalindrome(s: str) -> Tuple[int, List[str]]:
    length = 1
    longest = s[0] if s else None

    is_palindrome = [[False] * len(s) for i in range(len(s))]
    for i in range(len(s)):
        is_palindrome[i][i] = True

    for slen in range(2, len(s) + 1):
        for i in range(len(s) - slen + 1):
            j = i + slen - 1
            if s[i] == s[j] and (is_palindrome[i + 1][j - 1] or i + 1 > j - 1):
                is_palindrome[i][j] = True
                if j - i + 1 > length:
                    length = j - i + 1
                    longest = s[i:j+1]

    return longest


# Time complexity: O(n^2) - There are 2n - 1 possible centers from which we initiate
# checks. For odd length strings, there are n centers and for even length strings n -1
# centers. All in all, we have O(n) centers and each palindrome check costs O(n). This
# approach is faster, because most centers will not produce long palindromes, so most
# expand calls will cost far less than n comparisons
# Space complexity: O(1)
def longestPalindromeCenters(s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1
        
        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]
                
        i, j = ans
        return s[i:j + 1]


# Time complexity: O(n)
# Space complexity: O(n)
# https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
def longestPalindromeManacher(s: str) -> str:
    s_prime = '#' + '#'.join(s) + '#'
    n = len(s_prime)
    palindrome_radii = [0] * n
    center = radius = 0

    for i in range(n):
        mirror = 2 * center - i

        if i < radius:
            palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

        while (i + 1 + palindrome_radii[i] < n and 
                i - 1 - palindrome_radii[i] >= 0 and
                s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
            palindrome_radii[i] += 1

        if i + palindrome_radii[i] > radius:
            center = i
            radius = i + palindrome_radii[i]

    max_length = max(palindrome_radii)
    center_index = palindrome_radii.index(max_length)
    start_index = (center_index - max_length) // 2
    longest_palindrome = s[start_index: start_index + max_length]

    return longest_palindrome


if __name__ == "__main__":
    res = longestPalindrome("babad")
    assert res == "bab"

    res = longestPalindrome("cbbd")
    assert res == "bb"
