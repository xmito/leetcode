from typing import List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


# Write a function to find the longest common prefix string amongst an array
# of strings. If there is no common prefix, return an empty string "".
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


# Horizontal scanning solution that compares prefix over all strings
# LCP(S_1...S_n) = LCP(LCP(LCP(S_1, S_2), S_3),...S_n)
# Let n be number of strings
# Let m be the longest string length
# TIME COMPLEXITY: O(n * m)
# SPACE COMPLEXITY: O(1)
def commonPrefix(str1, str2):
    i = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            break
        i += 1
    return str1[:i]

def longestCommonPrefixHorizontal(strs: List[str]) -> str:
    if not strs:
        return ''

    cpref = strs[0]
    for string in strs[1:]:
        cpref = commonPrefix(cpref, string)
        if not cpref:
            break
    return cpref


# Vertical scanning solution that compares characters in a column in each iteration
# Let n be number of strings
# Let m be the longest string length
# TIME COMPLEXITY: O(n * m)
# In the best case, there are O(n * MIN_LEN) comparisons
# SPACE COMPLEXITY: O(1)
def longestCommonPrefixVertical(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        pchar = strs[0][i]
        for j in range(1, len(strs)):
            if pchar != strs[j][i]:
                return strs[0][:i]
        
    return strs[0]


# Divide and Conquer solution based on associative property of the longest common prefix
# LCP(S_1...S_n) = LCP(LCP(S_1...S_n/2), LCP(S_n/2+1..S_n))
# Let n be number of strings
# Let m be the longest string length
# TIME COMPLEXITY: O(m * n) - in case there are the same n strings of length m
# Consider recursion tree. For leaves, each string is the longest common prefix of
# itself and we don't need to do any comparisons. On tree level i, we need to do
# do (n / 2ˆlogn - i) * m comparisons. Overall when summed we need to do
# sum((n / 2ˆlogn - i) * m) comparisons for i from 0 to logn, which we can bound
# by n * m * sum((1 / 2)^i) for i from 0 to infinity. From this, we can derive
# time complexity bound O(n * m)
# In the best case, algorithm performs O(n * MIN_LEN) comparisons (every two consecutive
# strings need to have longest common prefix of length MIN_LEN)
# SPACE COMPLEXITY: O(m * logn) - logn recursive calls and m space to store prefix
def commonPrefix(a, b):
    prefix = min(len(a), len(b))
    for i in range(prefix):
        if a[i] != b[i]:
            return a[:i]

    return a[:prefix]

def longestCommonPrefixDQ(strs: List[str]):
    strings = len(strs)
    if strings == 0:
        return ""
    elif strings == 1:
        return strs[0]

    lcs_a = longestCommonPrefixDQ(strs[:strings // 2])
    lcs_b = longestCommonPrefixDQ(strs[strings // 2: ])
    return commonPrefix(lcs_a, lcs_b)


# Let n be number of strings
# Let m be the shortest string length
# Let k be the longest string length
# TIME COMPLEXITY: O(n * k * logm)
# n * k - bound for number of comparisons in each iteration
# logm - number of iterations in binary search
# SPACE COMPLEXITY: O(m)
# m - to hold prefix value
def haveCommonPrefix(strs: List[str], length: int):
    prefix = strs[0][:length]
    for word in strs:
        if not word.startswith(prefix):
            return False

    return True

def longestCommonPrefixBinary(strs: List[str]):
    if not strs:
        return ""

    min_length = min(len(s) for s in strs)
    lo, hi = 0, min_length
    while lo <= hi:
        middle = (lo + hi) // 2
        if haveCommonPrefix(strs, middle):
            lo = middle + 1
        else:
            hi = middle - 1

    return strs[0][:hi]


# Let n be number of strings and m be the longest string length
# TIME COMPLEXITY: O(n * m)
# O(n * m) for initializing Trie
# O(m) for searching the longest common prefix in Trie
# SPACE COMPLEXITY: O(n * m)
def longestCommonPrefixTrie(strs: List[str]):
    root = TrieNode()
    for word in strs:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    result = ""
    while root.children:
        if len(root.children) > 1 or root.is_word:
            return result
        
        char, root = next(iter(root.children.items()))
        result += char

    return result


if __name__ == "__main__":
    ret = longestCommonPrefixDQ(["flower", "flow", "flight"])
    print(ret)
    assert ret == "fl"

    ret = longestCommonPrefixDQ(["dog", "racecar", "car"])
    print(ret)
    assert ret == ""